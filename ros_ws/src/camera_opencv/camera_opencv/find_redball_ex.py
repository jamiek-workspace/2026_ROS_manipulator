"""빨간 공을 검출하고 OpenMANIPULATOR-X 관절을 제어한다."""

import math

import cv2
import numpy as np
import rclpy
from action_msgs.msg import GoalStatus
from builtin_interfaces.msg import Duration
from control_msgs.action import FollowJointTrajectory, GripperCommand
from cv_bridge import CvBridge
from rclpy.action import ActionClient
from rclpy.node import Node
from rclpy.task import Future
from sensor_msgs.msg import Image, JointState
from trajectory_msgs.msg import JointTrajectoryPoint


class ManipulatorPub(Node):
    """카메라 영상에서 빨간 공을 추적하는 노드."""

    JOINT_NAMES = ["joint1", "joint2", "joint3", "joint4"]

    JOINT_LIMITS = {
        "joint1": (-math.pi, math.pi),
        "joint2": (-1.5, 1.5),
        "joint3": (-1.5, 1.4),
        "joint4": (-1.7, 1.97),
    }

    def __init__(self):
        super().__init__("manipulator_pub")

        # ---------------------------------------------------------
        # Action Client
        # ---------------------------------------------------------
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

        # ---------------------------------------------------------
        # Subscription
        # ---------------------------------------------------------
        self.joint_state_subscription = self.create_subscription(
            JointState,
            "/joint_states",
            self.joint_callback,
            10,
        )

        self.image_subscription = self.create_subscription(
            Image,
            "/gripper_camera/image_raw",
            self.image_callback,
            10,
        )

        self.bridge = CvBridge()

        # ---------------------------------------------------------
        # 현재 관절 상태
        # ---------------------------------------------------------
        self.current_joint_position = {
            "joint1": 0.0,
            "joint2": 0.0,
            "joint3": 0.0,
            "joint4": 0.0,
        }

        self.current_gripper_position = 0.0
        self.joint_state_received = False

        # ---------------------------------------------------------
        # 영상 추적 설정
        # ---------------------------------------------------------
        self.pixel_dead_zone_x = 5
        self.pixel_dead_zone_y = 5

        self.minimum_ball_area = 100.0

        # 한 번에 움직일 최대 관절각
        self.max_joint_step = 0.04

        # 픽셀 오차를 관절각으로 변환하는 게인
        self.joint1_gain = 0.00035
        self.joint2_gain = 0.00025
        self.joint4_gain = 0.00015

        # 카메라 방향에 따라 부호를 변경한다.
        self.joint1_direction = -1.0
        self.joint2_direction = 1.0
        self.joint4_direction = -1.0

        # ---------------------------------------------------------
        # Action 제어 설정
        # ---------------------------------------------------------
        self.duration_sec = 1.0
        self.control_interval_sec = 1.2

        self.last_control_time = self.get_clock().now()

        self.joint_goal_active = False
        self.joint_goal_start_time = self.get_clock().now()
        self.joint_goal_timeout_sec = 5.0

        self.send_joint_goal_future = None
        self.joint_goal_handle = None
        self.joint_result_future = None

        # ---------------------------------------------------------
        # 거리 추정 설정
        # ---------------------------------------------------------
        self.reference_distance_m = 0.30
        self.reference_area = 5000.0

        self.last_distance_log_time = self.get_clock().now()

        # ---------------------------------------------------------
        # OpenCV Window
        # ---------------------------------------------------------
        cv2.namedWindow("img", cv2.WINDOW_NORMAL)
        cv2.namedWindow("mask", cv2.WINDOW_NORMAL)

        cv2.resizeWindow("img", 640, 480)
        cv2.resizeWindow("mask", 640, 480)

        self.get_logger().info("빨간 공 추적 노드가 시작되었습니다.")

    def image_callback(self, msg: Image):
        """카메라 영상에서 빨간 공을 검출한다."""

        try:
            img_sub = self.bridge.imgmsg_to_cv2(
                msg,
                desired_encoding="bgr8",
            )
        except Exception as error:
            self.get_logger().error(f"영상 변환 실패: {error}")
            return

        hsv = cv2.cvtColor(img_sub, cv2.COLOR_BGR2HSV)

        # HSV 빨간색 영역 1
        lower_red1 = np.array([0, 80, 60], dtype=np.uint8)
        upper_red1 = np.array([10, 255, 255], dtype=np.uint8)

        # HSV 빨간색 영역 2
        lower_red2 = np.array([170, 80, 60], dtype=np.uint8)
        upper_red2 = np.array([179, 255, 255], dtype=np.uint8)

        mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
        mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

        mask = cv2.bitwise_or(mask1, mask2)

        # 노이즈 제거
        kernel = np.ones((5, 5), dtype=np.uint8)

        mask = cv2.morphologyEx(
            mask,
            cv2.MORPH_OPEN,
            kernel,
            iterations=1,
        )

        mask = cv2.morphologyEx(
            mask,
            cv2.MORPH_CLOSE,
            kernel,
            iterations=2,
        )

        contours, _ = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE,
        )

        image_height, image_width = img_sub.shape[:2]

        image_center_x = image_width // 2
        image_center_y = image_height // 2

        # 영상 중앙점
        cv2.circle(
            img_sub,
            (image_center_x, image_center_y),
            5,
            (255, 0, 0),
            -1,
        )

        # 데드존 표시
        cv2.rectangle(
            img_sub,
            (
                image_center_x - self.pixel_dead_zone_x,
                image_center_y - self.pixel_dead_zone_y,
            ),
            (
                image_center_x + self.pixel_dead_zone_x,
                image_center_y + self.pixel_dead_zone_y,
            ),
            (255, 255, 0),
            2,
        )

        if contours:
            contour = max(contours, key=cv2.contourArea)
            area = float(cv2.contourArea(contour))

            if area >= self.minimum_ball_area:
                x, y, width, height = cv2.boundingRect(contour)

                center_x = x + width // 2
                center_y = y + height // 2

                error_x = center_x - image_center_x
                error_y = center_y - image_center_y

                estimated_distance = self.estimate_distance_from_area(area)

                cv2.rectangle(
                    img_sub,
                    (x, y),
                    (x + width, y + height),
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

                cv2.line(
                    img_sub,
                    (image_center_x, image_center_y),
                    (center_x, center_y),
                    (0, 255, 255),
                    2,
                )

                cv2.putText(
                    img_sub,
                    f"center=({center_x}, {center_y})",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 0),
                    2,
                )

                cv2.putText(
                    img_sub,
                    f"area={area:.0f}",
                    (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 0),
                    2,
                )

                cv2.putText(
                    img_sub,
                    f"distance={estimated_distance:.3f} m",
                    (10, 90),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 0),
                    2,
                )

                self.log_ball_information(
                    center_x=center_x,
                    center_y=center_y,
                    area=area,
                    estimated_distance=estimated_distance,
                    error_x=error_x,
                    error_y=error_y,
                )

                if self.joint_state_received:
                    self.track_ball(error_x, error_y)
                else:
                    self.get_logger().warn(
                        "/joint_states를 기다리는 중입니다.",
                        throttle_duration_sec=2.0,
                    )

        cv2.imshow("img", img_sub)
        cv2.imshow("mask", mask)

        # OpenCV GUI 이벤트 처리
        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            self.get_logger().info("q 키가 입력되었습니다.")
            rclpy.shutdown()

    def estimate_distance_from_area(self, area: float) -> float:
        """영상에서 검출된 공 면적으로 거리를 추정한다."""

        if area <= 0.0:
            return float("inf")

        return self.reference_distance_m * math.sqrt(self.reference_area / area)

    def log_ball_information(
        self,
        center_x: int,
        center_y: int,
        area: float,
        estimated_distance: float,
        error_x: int,
        error_y: int,
    ):
        """공의 위치와 거리 정보를 0.5초 간격으로 출력한다."""

        now = self.get_clock().now()

        elapsed = (now - self.last_distance_log_time).nanoseconds / 1e9

        if elapsed < 0.5:
            return

        self.last_distance_log_time = now

        self.get_logger().info(
            f"공 중심=({center_x}, {center_y}), "
            f"오차=({error_x}, {error_y}), "
            f"면적={area:.1f} px^2, "
            f"추정 거리={estimated_distance:.3f} m"
        )

    def track_ball(self, error_x: int, error_y: int):
        """공이 영상 중앙에 오도록 관절 목표값을 생성한다."""

        now = self.get_clock().now()

        # 이전 액션이 실행 중이면 새 목표를 보내지 않는다.
        if self.joint_goal_active:
            goal_elapsed = (now - self.joint_goal_start_time).nanoseconds / 1e9

            if goal_elapsed < self.joint_goal_timeout_sec:
                return

            self.get_logger().warn("관절 액션 결과가 오지 않아 상태를 초기화합니다.")

            self.joint_goal_active = False

        control_elapsed = (now - self.last_control_time).nanoseconds / 1e9

        if control_elapsed < self.control_interval_sec:
            return

        x_needs_control = abs(error_x) > self.pixel_dead_zone_x

        y_needs_control = abs(error_y) > self.pixel_dead_zone_y

        if not x_needs_control and not y_needs_control:
            return

        target = [
            self.current_joint_position["joint1"],
            self.current_joint_position["joint2"],
            self.current_joint_position["joint3"],
            self.current_joint_position["joint4"],
        ]

        # 좌우 이동
        if x_needs_control:
            joint1_delta = self.clamp(
                error_x * self.joint1_gain * self.joint1_direction,
                -self.max_joint_step,
                self.max_joint_step,
            )

            target[0] += joint1_delta

        # 상하 이동
        if y_needs_control:
            joint2_delta = self.clamp(
                error_y * self.joint2_gain * self.joint2_direction,
                -self.max_joint_step,
                self.max_joint_step,
            )

            joint4_delta = self.clamp(
                error_y * self.joint4_gain * self.joint4_direction,
                -self.max_joint_step,
                self.max_joint_step,
            )

            target[1] += joint2_delta
            target[3] += joint4_delta

        target = self.apply_joint_limits(target)

        point = JointTrajectoryPoint()

        # position controller이므로 positions만 지정한다.
        point.positions = [float(position) for position in target]

        point.time_from_start = Duration(
            sec=int(self.duration_sec),
            nanosec=int((self.duration_sec - int(self.duration_sec)) * 1_000_000_000),
        )

        self.get_logger().info(
            "관절 목표값: "
            f"joint1={target[0]:.3f}, "
            f"joint2={target[1]:.3f}, "
            f"joint3={target[2]:.3f}, "
            f"joint4={target[3]:.3f}"
        )

        self.last_control_time = now

        self.move_joint(point)

    def joint_callback(self, msg: JointState):
        """현재 관절 위치를 관절 이름 기준으로 저장한다."""

        position_by_name = dict(zip(msg.name, msg.position))

        received_count = 0

        for joint_name in self.JOINT_NAMES:
            if joint_name in position_by_name:
                self.current_joint_position[joint_name] = float(position_by_name[joint_name])

                received_count += 1

        self.joint_state_received = received_count == len(self.JOINT_NAMES)

        if "gripper_left_joint" in position_by_name:
            self.current_gripper_position = float(position_by_name["gripper_left_joint"])

    def apply_joint_limits(
        self,
        positions: list[float],
    ) -> list[float]:
        """관절 목표값을 제한 범위 안으로 조정한다."""

        result = []

        for joint_name, position in zip(
            self.JOINT_NAMES,
            positions,
        ):
            lower, upper = self.JOINT_LIMITS[joint_name]

            result.append(self.clamp(position, lower, upper))

        return result

    @staticmethod
    def clamp(
        value: float,
        minimum: float,
        maximum: float,
    ) -> float:
        return max(minimum, min(value, maximum))

    def move_joint(
        self,
        point: JointTrajectoryPoint,
    ):
        """FollowJointTrajectory Action 목표를 전송한다."""

        if self.joint_goal_active:
            return

        if not self.joint_client.server_is_ready():
            self.get_logger().warn("관절 Action 서버 연결을 기다립니다.")

            if not self.joint_client.wait_for_server(timeout_sec=2.0):
                self.get_logger().error(
                    "Action 서버를 찾지 못했습니다: /arm_controller/follow_joint_trajectory"
                )
                return

        goal = FollowJointTrajectory.Goal()

        # stamp를 0으로 설정하면 서버가 수신한 즉시 실행한다.
        goal.trajectory.header.stamp.sec = 0
        goal.trajectory.header.stamp.nanosec = 0

        goal.trajectory.joint_names = list(self.JOINT_NAMES)

        goal.trajectory.points = [point]

        goal.goal_time_tolerance = Duration(
            sec=2,
            nanosec=0,
        )

        self.get_logger().info(
            "Action 목표 전송: "
            f"positions="
            f"{[round(v, 4) for v in point.positions]}, "
            f"time_from_start="
            f"{point.time_from_start.sec}."
            f"{point.time_from_start.nanosec:09d}s"
        )

        self.joint_goal_active = True
        self.joint_goal_start_time = self.get_clock().now()

        try:
            self.send_joint_goal_future = self.joint_client.send_goal_async(
                goal,
                feedback_callback=(self.feedback_joint_callback),
            )

            self.send_joint_goal_future.add_done_callback(self.goal_joint_callback)

        except Exception as error:
            self.joint_goal_active = False

            self.get_logger().error(f"Action 목표 전송 예외: {error!r}")

    def goal_joint_callback(self, future: Future):
        """관절 Action 목표 수락 여부를 확인한다."""

        try:
            goal_handle = future.result()

        except Exception as error:
            self.joint_goal_active = False

            self.get_logger().error(f"관절 목표 Future 예외: {error!r}")
            return

        if goal_handle is None:
            self.joint_goal_active = False

            self.get_logger().error("GoalHandle이 None입니다.")
            return

        if not goal_handle.accepted:
            self.joint_goal_active = False

            self.get_logger().error("관절 Action 목표가 거부되었습니다.")
            return

        self.get_logger().info("관절 Action 목표가 수락되었습니다.")

        self.joint_goal_handle = goal_handle

        try:
            self.joint_result_future = goal_handle.get_result_async()

            self.joint_result_future.add_done_callback(self.get_joint_result_callback)

        except Exception as error:
            self.joint_goal_active = False

            self.get_logger().error(f"관절 결과 요청 예외: {error!r}")

    def feedback_joint_callback(
        self,
        msg: FollowJointTrajectory.Impl.FeedbackMessage,
    ):
        """관절 Action 피드백을 처리한다."""

        feedback = msg.feedback

        self.get_logger().debug(
            f"actual={list(feedback.actual.positions)}, "
            f"desired={list(feedback.desired.positions)}, "
            f"error={list(feedback.error.positions)}"
        )

    def get_joint_result_callback(
        self,
        future: Future,
    ):
        """관절 Action 최종 결과를 처리한다."""

        self.joint_goal_active = False

        try:
            response = future.result()

        except Exception as error:
            self.get_logger().error(f"관절 결과 Future 예외: {error!r}")
            return

        result = response.result

        self.get_logger().info(
            "관절 Action 결과: "
            f"status={response.status}, "
            f"error_code={result.error_code}, "
            f"error_string='{result.error_string}'"
        )

        if response.status == GoalStatus.STATUS_SUCCEEDED:
            if result.error_code == FollowJointTrajectory.Result.SUCCESSFUL:
                self.get_logger().info("관절 이동 성공")
            else:
                self.get_logger().error(
                    f"Action은 종료됐지만 trajectory 오류가 있습니다. code={result.error_code}"
                )

        elif response.status == GoalStatus.STATUS_ABORTED:
            self.get_logger().error(
                f"관절 이동 중단: code={result.error_code}, message='{result.error_string}'"
            )

        elif response.status == GoalStatus.STATUS_CANCELED:
            self.get_logger().warn("관절 이동 취소")

        else:
            self.get_logger().warn(f"알 수 없는 Action 상태: {response.status}")

    def move_gripper(
        self,
        position: float,
        max_effort: float = 10.0,
    ):
        """그리퍼 목표를 전송한다."""

        if not self.gripper_client.server_is_ready():
            if not self.gripper_client.wait_for_server(timeout_sec=2.0):
                self.get_logger().error("그리퍼 Action 서버를 찾지 못했습니다.")
                return

        goal = GripperCommand.Goal()

        goal.command.position = float(position)
        goal.command.max_effort = float(max_effort)

        try:
            future = self.gripper_client.send_goal_async(
                goal,
                feedback_callback=self.feedback_gripper_callback,
            )

            future.add_done_callback(self.goal_gripper_callback)

        except Exception as error:
            self.get_logger().error(f"그리퍼 목표 전송 예외: {error!r}")

    def goal_gripper_callback(
        self,
        future: Future,
    ):
        """그리퍼 목표 수락 여부를 확인한다."""

        try:
            goal_handle = future.result()

        except Exception as error:
            self.get_logger().error(f"그리퍼 목표 Future 예외: {error!r}")
            return

        if goal_handle is None or not goal_handle.accepted:
            self.get_logger().error("그리퍼 목표가 거부되었습니다.")
            return

        self.get_logger().info("그리퍼 목표가 수락되었습니다.")

        result_future = goal_handle.get_result_async()

        result_future.add_done_callback(self.get_gripper_result_callback)

    def feedback_gripper_callback(
        self,
        msg: GripperCommand.Impl.FeedbackMessage,
    ):
        """그리퍼 피드백을 처리한다."""

        feedback = msg.feedback

        self.get_logger().debug(f"그리퍼 현재 위치={feedback.position}")

    def get_gripper_result_callback(
        self,
        future: Future,
    ):
        """그리퍼 실행 결과를 처리한다."""

        try:
            response = future.result()

        except Exception as error:
            self.get_logger().error(f"그리퍼 결과 Future 예외: {error!r}")
            return

        if response.status == GoalStatus.STATUS_SUCCEEDED:
            self.get_logger().info(f"그리퍼 이동 성공: position={response.result.position}")

        elif response.status == GoalStatus.STATUS_ABORTED:
            self.get_logger().error("그리퍼 이동 중단")

        elif response.status == GoalStatus.STATUS_CANCELED:
            self.get_logger().warn("그리퍼 이동 취소")


def main(args=None):
    rclpy.init(args=args)

    node = ManipulatorPub()

    try:
        # SingleThreadedExecutor를 사용하는 rclpy.spin().
        # image_callback과 imshow가 메인 스레드에서 실행된다.
        rclpy.spin(node)

    except KeyboardInterrupt:
        print("키보드 인터럽트")

    finally:
        # ROS context가 유효할 때 먼저 노드를 제거한다.
        node.destroy_node()

        cv2.destroyAllWindows()

        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()