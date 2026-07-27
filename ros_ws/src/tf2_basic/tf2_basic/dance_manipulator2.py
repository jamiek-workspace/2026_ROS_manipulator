import rclpy
from action_msgs.msg import GoalStatus
from control_msgs.action import GripperCommand, GripperCommand_GetResult_Response
from rclpy.action import ActionClient
from rclpy.node import Node
from rclpy.task import Future
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from ament_index_python.packages import get_package_share_directory

import random
import os
import yaml

class DanceManipulator(Node):
    def __init__(self):
        super().__init__("dance_manipulator2")  # 노드 이름 설정
        
        # 1. 외부 YAML 파일에서 춤 포즈 데이터 로드
        self.pose_list = self.load_position_data()
        
        # 2. 퍼블리셔, 액션 클라이언트, 서브스크립션 설정
        self.pub = self.create_publisher(JointTrajectory, "arm_controller/joint_trajectory", 10)
        self.gripper_client = ActionClient(self, GripperCommand, "/gripper_controller/gripper_cmd")
        self.joint_state_subscription = self.create_subscription(
            JointState, "joint_states", self.joint_callback, 10
        )
        
        # 상태 변수 초기화
        self.current_joint_position = [0.0, 0.0, 0.0, 0.0]
        self.duration_sec = 2.0
        
        # 3. 타이머 등록 (2초마다 무작위 춤 동작 수행)
        self.create_timer(self.duration_sec, self.timer_callback)

    def load_position_data(self):
        """외부 YAML 파일에서 로봇팔 춤 포즈 데이터를 로드한다."""

        package_share_dir = get_package_share_directory("tf2_basic")

        file_path = os.path.join(
            package_share_dir,
            "data",
            "dance_positions2.yaml",
        )

        if not os.path.exists(file_path):
            self.get_logger().warning(
                f"데이터 파일({file_path})을 찾을 수 없어 "
                "기본 포즈를 사용합니다."
            )

            return [
                [
                    0.8995922516973869,
                    -0.5832234352774157,
                    -0.26300971181849175,
                    -0.6258641614575486,
                ],
                [
                    0.4795922516973865,
                    -0.883223435277416,
                    0.3969902881815083,
                    0.8941358385424522,
                ],
            ]

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = yaml.safe_load(file)

            poses = data.get("dance_poses", [])

            self.get_logger().info(
                f"{file_path}에서 "
                f"{len(poses)}개의 춤 포즈를 로드했습니다."
            )

            return poses

        except Exception as error:
            self.get_logger().error(
                f"파일을 읽는 중 오류가 발생했습니다: {error}"
            )
            return [[0.0, 0.0, 0.0, 0.0]]

    def timer_callback(self):
        msg = JointTrajectory()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "move_manipulator"
        msg.joint_names = ["joint1", "joint2", "joint3", "joint4"]
        
        point = JointTrajectoryPoint()
        
        # 4. random 함수를 활용한 무작위 춤 포즈 결정
        random_pose = random.choice(self.pose_list)
        point.positions = [float(val) for val in random_pose]
        
        # 그리퍼의 벌림 정도(0.01m ~ 0.02m)도 무작위로 연산하여 전달
        random_gripper_pos = random.uniform(0.01, 0.02)
        self.move_gripper(random_gripper_pos)
        
        self.get_logger().info(f"랜덤 춤 실행 중 -> 포즈: {point.positions} | 그리퍼: {random_gripper_pos:.3f}")

        # 시간 정보 계산 및 주입
        seconds = int(self.duration_sec)
        nanoseconds = int((self.duration_sec - seconds) * 1_000_000_000)
        point.time_from_start.sec = seconds
        point.time_from_start.nanosec = nanoseconds

        msg.points.append(point)  # type: ignore
        self.pub.publish(msg)

    def joint_callback(self, msg: JointState):
        self.current_joint_position = msg.position

    def move_gripper(self, position: float, max_effort=10.0, timeout_sec=5.0):
        if not self.gripper_client.wait_for_server(timeout_sec=timeout_sec):
            self.get_logger().info("gripper_controller Action 서버를 찾지 못했습니다.")
            return
        goal = GripperCommand.Goal()
        goal.command.position = float(position)
        goal.command.max_effort = float(max_effort)
        send_goal_future = self.gripper_client.send_goal_async(goal)
        send_goal_future.add_done_callback(self.goal_callback)

    def goal_callback(self, future: Future):
        self.goal_handle = future.result()  # type: ignore
        self.get_result_future = self.goal_handle.get_result_async()  # type: ignore
        self.get_result_future.add_done_callback(self.get_result_callback)

    def feedback_callback(self, msg: GripperCommand.Impl.FeedbackMessage):
        feedback: GripperCommand.Feedback = msg.feedback
        self.get_logger().info(f"{feedback.position}")

    def get_result_callback(self, future: Future):
        result: GripperCommand_GetResult_Response = future.result()  # type: ignore
        if result.status == GoalStatus.STATUS_SUCCEEDED:
            pass  # 반복적인 춤 동작 콘솔창을 깨끗하게 유지하기 위해 성공 로그 생략
        elif result.status == GoalStatus.STATUS_ABORTED:
            self.get_logger().info("그리퍼 구동 실패(Aborted)!!")
        elif result.status == GoalStatus.STATUS_CANCELED:
            self.get_logger().info("그리퍼 구동 취소(Canceled)!!")


def main(args=None):
    rclpy.init(args=args)  # rmw 활성화
    node = DanceManipulator()
    try:
        rclpy.spin(node)  # 무한 루프 구동
    except KeyboardInterrupt:
        print("키보드 인터럽트로 춤 동작을 종료합니다.")
    finally:
        node.destroy_node()


if __name__ == "__main__":
    main()