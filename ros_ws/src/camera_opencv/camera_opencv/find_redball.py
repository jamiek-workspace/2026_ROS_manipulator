import cv2
import numpy as np
import rclpy
from action_msgs.msg import GoalStatus
from control_msgs.action import (
    FollowJointTrajectory,
    FollowJointTrajectory_GetResult_Response,
    GripperCommand,
    GripperCommand_GetResult_Response,
)
from cv_bridge import CvBridge
from rclpy.action import ActionClient
from rclpy.node import Node
from rclpy.task import Future
from sensor_msgs.msg import Image, JointState
from trajectory_msgs.msg import JointTrajectoryPoint


class Manipulator_pub(Node):
    def __init__(self):
        super().__init__("manipulator_pub")  # 노드 이름
        self.joint_client = ActionClient(
            self, FollowJointTrajectory, "/arm_controller/follow_joint_trajectory"
        )
        self.gripper_client = ActionClient(self, GripperCommand, "/gripper_controller/gripper_cmd")
        self.joint_state_subscription = self.create_subscription(
            JointState, "joint_states", self.joint_callback, 10
        )
        self.current_joint_position = [0.0, 0.0, 0.0, 0.0]
        self.current_gripper_position = 0.0
        self.joint_state_received = False
        self.count = True
        self.duration_sec = 1
        self.brige = CvBridge()
        self.motion_in_progress = False
        self.pixel_tolerance = 20
        self.horizontal_step = 0.03
        self.vertical_step = 0.02
        self.image_subscription = self.create_subscription(
            Image,
            "/gripper_camera/image_raw",
            self.image_callback,
            10,
        )

    def image_callback(self, msg: Image):
        img_sub = self.brige.imgmsg_to_cv2(msg, desired_encoding="bgr8")

        hsv = cv2.cvtColor(img_sub, cv2.COLOR_BGR2HSV)

        lower = np.array([0, 40, 40], dtype=np.uint8)
        upper = np.array([10, 255, 255], dtype=np.uint8)
        mask = cv2.inRange(hsv, lower, upper)

        contours, _ = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE,
        )

        if contours:
            contour = max(contours, key=cv2.contourArea)
            area = cv2.contourArea(contour)

            if area > 20:
                # 반환 순서: x, y, width, height
                x, y, w, h = cv2.boundingRect(contour)

                center_x = x + w // 2
                center_y = y + h // 2

                image_center_x = img_sub.shape[1] // 2
                image_center_y = img_sub.shape[0] // 2

                error_x = center_x - image_center_x
                error_y = center_y - image_center_y

                cv2.rectangle(
                    img_sub,
                    (x, y),
                    (x + w, y + h),
                    (0, 255, 0),
                    2,
                )
                cv2.circle(
                    img_sub,
                    (center_x, center_y),
                    5,
                    (0, 255, 0),
                    -1,
                )
                cv2.circle(
                    img_sub,
                    (image_center_x, image_center_y),
                    5,
                    (255, 0, 0),
                    -1,
                )

                self.get_logger().info(
                    f"공=({center_x}, {center_y}), "
                    f"오차=({error_x}, {error_y})"
                )

                # joint_states를 받았고, 이전 동작이 완료됐을 때만 전송
                if self.joint_state_received and not self.motion_in_progress:
                    target = list(self.current_joint_position)

                    # 공이 화면 오른쪽에 있는 경우
                    if error_x > self.pixel_tolerance:
                        target[0] -= self.horizontal_step

                    # 공이 화면 왼쪽에 있는 경우
                    elif error_x < -self.pixel_tolerance:
                        target[0] += self.horizontal_step

                    # 중심 범위를 벗어났을 때만 움직임
                    if abs(error_x) > self.pixel_tolerance:
                        point = JointTrajectoryPoint()
                        point.positions = target
                        point.velocities = [0.0, 0.0, 0.0, 0.0]
                        point.time_from_start.sec = 1

                        self.motion_in_progress = True

                        self.get_logger().info(
                            f"관절 목표 전송: {target}"
                        )
                        self.get_logger().info("move_joint 호출")
                        self.move_joint(point)

        cv2.imshow("img", img_sub)
        cv2.imshow("mask", mask)
        cv2.waitKey(10)
        # x 좌표를 기반으로 해서 좌우로 움직이기 joint 1
        # y 좌표를 기반으로 해서 위아래로 움직이기 joint2~4
        # joint_state subscription -> 변화.
        # 공의 거리를 추측 area 기반으로 공의 거리를 로깅을 찍으세요.
        # self.move_gripper(-0.01)
        # self.move_joint(point)

    def joint_callback(self, msg: JointState):
        joint_map = dict(zip(msg.name, msg.position))

        required = ["joint1", "joint2", "joint3", "joint4"]

        if all(name in joint_map for name in required):
            self.current_joint_position = [
                joint_map["joint1"],
                joint_map["joint2"],
                joint_map["joint3"],
                joint_map["joint4"],
            ]
            self.joint_state_received = True

    def move_gripper(self, position: float, max_effort=10.0, timeout_sec=5.0):
        if not self.gripper_client.wait_for_server(timeout_sec=timeout_sec):
            self.get_logger().info("gripper_controller Action 서버를 찾지 못햇습니다.")
        goal = GripperCommand.Goal()
        goal.command.position = float(position)
        goal.command.max_effort = float(max_effort)
        send_goal_future = self.gripper_client.send_goal_async(goal)
        send_goal_future.add_done_callback(self.goal_callback)

    def goal_callback(self, future: Future):
        self.goal_handle = future.result()  # type: ignore
        self.get_result_future = self.goal_handle.get_result_async()  # type: ignore
        self.get_result_future.add_done_callback(self.get_result_callback)

    def feedback_callback(
        self,
        msg: GripperCommand.Impl.FeedbackMessage,
    ):
        feedback: GripperCommand.Feedback = msg.feedback
        self.get_logger().info(f"{feedback.position}")

    def get_result_callback(self, future: Future):
        result: GripperCommand_GetResult_Response = (
            future.result()  # type: ignore
        )
        if result.status == GoalStatus.STATUS_SUCCEEDED:
            self.get_logger().info(f"succeeded result: {result.result.position}")
        elif result.status == GoalStatus.STATUS_ABORTED:
            self.get_logger().info("aborted!!")
        elif result.status == GoalStatus.STATUS_CANCELED:
            self.get_logger().info("canceled!!")

    def move_joint(self, point: JointTrajectoryPoint):
        if not self.joint_client.wait_for_server(timeout_sec=1.0):
            self.get_logger().error(
                "arm_controller Action 서버를 찾지 못했습니다."
            )
            self.motion_in_progress = False
            return

        goal = FollowJointTrajectory.Goal()

        # frame_id는 비워두어도 됨
        goal.trajectory.header.stamp = self.get_clock().now().to_msg()
        goal.trajectory.joint_names = [
            "joint1",
            "joint2",
            "joint3",
            "joint4",
        ]
        goal.trajectory.points.append(point)

        send_goal_future = self.joint_client.send_goal_async(goal)
        send_goal_future.add_done_callback(self.goal_joint_callback)

    def goal_joint_callback(self, future: Future):
        try:
            self.goal_handle = future.result()
        except Exception as error:
            self.get_logger().error(f"Goal 전송 실패: {error}")
            self.motion_in_progress = False
            return

        if not self.goal_handle.accepted:
            self.get_logger().error("관절 이동 Goal이 거절되었습니다.")
            self.motion_in_progress = False
            return

        self.get_logger().info("관절 이동 Goal 승인")

        self.get_result_future = self.goal_handle.get_result_async()
        self.get_result_future.add_done_callback(
            self.get_joint_result_callback
        )

    def feedback_joint_callback(
        self,
        msg: FollowJointTrajectory.Impl.FeedbackMessage,
    ):
        feedback: FollowJointTrajectory.Feedback = msg.feedback
        self.get_logger().info(f"{feedback.actual.positions}")

    def get_joint_result_callback(self, future: Future):
        self.motion_in_progress = False

        try:
            result: FollowJointTrajectory_GetResult_Response = (
                future.result()
            )
        except Exception as error:
            self.get_logger().error(f"관절 이동 결과 오류: {error}")
            return

        if result.status == GoalStatus.STATUS_SUCCEEDED:
            self.get_logger().info(
                f"관절 이동 성공: {result.result.error_string}"
            )
        elif result.status == GoalStatus.STATUS_ABORTED:
            self.get_logger().error(
                f"관절 이동 중단: {result.result.error_string}"
            )
        elif result.status == GoalStatus.STATUS_CANCELED:
            self.get_logger().warning("관절 이동 취소")
        else:
            self.get_logger().warning(
                f"알 수 없는 결과 상태: {result.status}"
            )


def main(args=None):
    rclpy.init(args=args)  # rmw 활성화
    node = Manipulator_pub()
    try:
        rclpy.spin(node)  # 블럭 (무한 루프)
    except KeyboardInterrupt:
        print("키보드 인터럽트")
    finally:
        node.destroy_node()


if __name__ == "__main__":
    main()