import rclpy
from action_msgs.msg import GoalStatus
from control_msgs.action import (
    FollowJointTrajectory,
    FollowJointTrajectory_GetResult_Response,
    GripperCommand,
)
from rclpy.action import ActionClient
from rclpy.node import Node
from rclpy.task import Future
from trajectory_msgs.msg import JointTrajectoryPoint


class DanceManipulatorAction(Node):
    def __init__(self):
        super().__init__("dance_manipulator_action")

        self.joint_client = ActionClient(
            self,
            FollowJointTrajectory,
            "/arm_controller/follow_joint_trajectory",
        )

        self.gripper_client = ActionClient(
            self,
            GripperCommand,
            "/gripper_controller/gripper_cmd",
        )

        self.arm_goal_handle = None
        self.started = False

        # 노드가 spin에 진입한 뒤 한 번만 춤을 시작한다.
        self.start_timer = self.create_timer(
            1.0,
            self.start_dance,
        )

    def start_dance(self):
        if self.started:
            return

        self.started = True
        self.start_timer.cancel()

        if not self.joint_client.wait_for_server(
            timeout_sec=5.0
        ):
            self.get_logger().error(
                "joint_controller 액션 서버를 찾지 못했습니다."
            )
            return

        self.send_dance_goal()

    def make_point(
        self,
        positions: list[float],
        time_from_start: float,
    ) -> JointTrajectoryPoint:
        point = JointTrajectoryPoint()
        point.positions = positions

        seconds = int(time_from_start)
        nanoseconds = int(
            (time_from_start - seconds) * 1_000_000_000
        )

        point.time_from_start.sec = seconds
        point.time_from_start.nanosec = nanoseconds

        return point

    def send_dance_goal(self):
        goal = FollowJointTrajectory.Goal()

        goal.trajectory.header.stamp = (
            self.get_clock().now().to_msg()
        )
        goal.trajectory.header.frame_id = (
            "dance_manipulator_action"
        )
        goal.trajectory.joint_names = [
            "joint1",
            "joint2",
            "joint3",
            "joint4",
        ]

        dance_points = [
            # 준비 자세
            self.make_point(
                [0.00, -0.60, 0.05, 0.55],
                2.0,
            ),

            # 왼쪽으로 회전
            self.make_point(
                [0.45, -0.60, 0.05, 0.55],
                3.5,
            ),

            # 왼쪽 까딱 2번
            self.make_point(
                [0.45, -0.80, 0.20, 0.70],
                4.3,
            ),
            self.make_point(
                [0.45, -0.45, -0.05, 0.40],
                5.1,
            ),
            self.make_point(
                [0.45, -0.80, 0.20, 0.70],
                5.9,
            ),
            self.make_point(
                [0.45, -0.45, -0.05, 0.40],
                6.7,
            ),

            # 오른쪽으로 회전
            self.make_point(
                [-0.45, -0.60, 0.05, 0.55],
                8.2,
            ),

            # 오른쪽 까딱 2번
            self.make_point(
                [-0.45, -0.80, 0.20, 0.70],
                9.0,
            ),
            self.make_point(
                [-0.45, -0.45, -0.05, 0.40],
                9.8,
            ),
            self.make_point(
                [-0.45, -0.80, 0.20, 0.70],
                10.6,
            ),
            self.make_point(
                [-0.45, -0.45, -0.05, 0.40],
                11.4,
            ),

            # 가운데에서 아래로 바운스
            self.make_point(
                [0.00, -0.88, 0.30, 0.75],
                12.8,
            ),

            # 위로 튕기기
            self.make_point(
                [0.00, -0.38, -0.25, 0.38],
                13.7,
            ),

            # 좌우 흔들기
            self.make_point(
                [0.32, -0.55, 0.00, 0.50],
                14.4,
            ),
            self.make_point(
                [-0.32, -0.55, 0.00, 0.50],
                15.1,
            ),
            self.make_point(
                [0.32, -0.55, 0.00, 0.50],
                15.8,
            ),
            self.make_point(
                [-0.32, -0.55, 0.00, 0.50],
                16.5,
            ),

            # 마무리 자세
            self.make_point(
                [0.00, -0.48, -0.12, 0.45],
                18.0,
            ),
        ]

        goal.trajectory.points.extend(dance_points)

        self.get_logger().info(
            f"{len(dance_points)}개의 포인트로 "
            "춤 액션 목표를 전송합니다."
        )

        send_goal_future = self.joint_client.send_goal_async(
            goal,
            feedback_callback=self.feedback_joint_callback,
        )
        send_goal_future.add_done_callback(
            self.goal_joint_callback
        )

    def goal_joint_callback(self, future: Future):
        try:
            goal_handle = future.result()
        except Exception as error:
            self.get_logger().error(
                f"액션 목표 전송 실패: {error}"
            )
            return

        if not goal_handle.accepted:
            self.get_logger().error(
                "춤 액션 목표가 거부되었습니다."
            )
            return

        self.arm_goal_handle = goal_handle

        self.get_logger().info(
            "춤 액션 목표가 수락되었습니다."
        )

        result_future = goal_handle.get_result_async()
        result_future.add_done_callback(
            self.get_joint_result_callback
        )

    def feedback_joint_callback(
        self,
        msg: FollowJointTrajectory.Impl.FeedbackMessage,
    ):
        feedback = msg.feedback

        # 너무 많은 로그가 나오지 않게 debug로 출력
        if feedback.actual.positions:
            positions = [
                round(value, 3)
                for value in feedback.actual.positions
            ]

            self.get_logger().debug(
                f"현재 관절 위치: {positions}"
            )

    def get_joint_result_callback(self, future: Future):
        result: FollowJointTrajectory_GetResult_Response = (
            future.result()
        )

        if result.status == GoalStatus.STATUS_SUCCEEDED:
            self.get_logger().info(
                "춤 동작 1회 완료. 다음 춤을 시작합니다."
            )

            # 약간 쉬었다가 다시 실행
            self.repeat_timer = self.create_timer(
                1.0,
                self.repeat_dance_once,
            )

        elif result.status == GoalStatus.STATUS_ABORTED:
            self.get_logger().error(
                "춤 동작이 중단되었습니다. "
                f"error_code={result.result.error_code}, "
                f"error_string={result.result.error_string}"
            )

        elif result.status == GoalStatus.STATUS_CANCELED:
            self.get_logger().warning(
                "춤 동작이 취소되었습니다."
            )

    def cancel_dance(self):
        if self.arm_goal_handle is None:
            return

        self.arm_goal_handle.cancel_goal_async()

    def repeat_dance_once(self):
        self.repeat_timer.cancel()
        self.send_dance_goal()


def main(args=None):
    rclpy.init(args=args)

    node = DanceManipulatorAction()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        node.get_logger().info(
            "키보드 인터럽트로 춤 동작을 취소합니다."
        )
        node.cancel_dance()

    finally:
        node.destroy_node()

        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()