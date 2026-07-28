import random
import rclpy
from action_msgs.msg import GoalStatus
from control_msgs.action import (
    FollowJointTrajectory,
    FollowJointTrajectory_GetResult_Response,
    GripperCommand,
    GripperCommand_GetResult_Response,
)
from rclpy.action import ActionClient
from rclpy.node import Node
from rclpy.task import Future
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectoryPoint


class DanceManipulatorAction(Node):
    def __init__(self):
        super().__init__("dance_manipulator_action2")  # 노드 이름 설정

        # 1. 하드웨어 보호를 위한 소프트웨어 조인트 안전 한계치 고정 (라디안 단위)
        self.joint_limits = [
            {"min": -0.8, "max": 0.8},  # joint1
            {"min": -0.8, "max": 0.8},  # joint2
            {"min": -0.8, "max": 0.8},  # joint3
            {"min": -0.8, "max": 0.8},  # joint4
        ]

        # 2. 코드 내부 고정형 안전 댄스 포즈 데이터셋 (YAML 대체)
        # 모든 포즈는 이미 안전 한계치 내부의 완만한 각도로 설계되었습니다.
        self.pose_list = [
            [ 0.4, -0.3,  0.2, -0.4],
            [-0.4, -0.5,  0.3,  0.4],
            [ 0.2, -0.2, -0.3,  0.2],
            [-0.3, -0.4,  0.4, -0.2],
            [ 0.0, -0.5,  0.2,  0.3],
            [ 0.3, -0.1, -0.2, -0.3],
            [-0.5, -0.3,  0.1,  0.2],
            [ 0.2, -0.4,  0.3, -0.1],
        ]

        # 관절 및 그리퍼 제어를 위한 액션 클라이언트 등록
        self.joint_client = ActionClient(
            self, FollowJointTrajectory, "/arm_controller/follow_joint_trajectory"
        )
        self.gripper_client = ActionClient(
            self, GripperCommand, "/gripper_controller/gripper_cmd"
        )
        
        # 실제 로봇 관절 상태 업데이트를 위한 구독
        self.joint_state_subscription = self.create_subscription(
            JointState, "joint_states", self.joint_callback, 10
        )
        
        self.current_joint_position = [0.0, 0.0, 0.0, 0.0]
        self.duration_sec = 1.5  # 목표 지점까지 이동할 가속 버퍼 시간 (초)

        # 2.0초 간격으로 무작위 댄스 스텝을 호출하는 타이머 가동
        self.create_timer(2.0, self.timer_callback)
        self.get_logger().info("단일 코드 기반 안전 랜덤 댄스 노드가 시작되었습니다.")

    def timer_callback(self):
        """2초 주기로 코드 내부 배열에서 무작위 포즈를 선택하고 실행하는 콜백"""
        if not self.pose_list:
            return

        # [random.choice] 내부 포즈 데이터셋에서 무작위 1개 스텝 추첨
        random_pose = random.choice(self.pose_list)
        
        # 내부 하드코딩 데이터라도 런타임 오동작 방지를 위한 실시간 클리핑 보강
        safe_pose = []
        for i in range(min(len(random_pose), 4)):
            clipped_val = max(self.joint_limits[i]["min"], min(random_pose[i], self.joint_limits[i]["max"]))
            safe_pose.append(clipped_val)

        # Trajectory 궤적 생성 및 시간 설정
        point = JointTrajectoryPoint()
        point.positions = safe_pose
        seconds = int(self.duration_sec)
        nanoseconds = int((self.duration_sec - seconds) * 1_000_000_000)
        point.time_from_start.sec = seconds
        point.time_from_start.nanosec = nanoseconds
        
        # 충돌 및 모터 부하 방지를 위해 그리퍼 간격을 0.012m ~ 0.018m 범위 내에서 무작위 제어
        random_gripper_pos = random.uniform(0.012, 0.018)

        # 관절 액션 서버 및 그리퍼 액션 서버로 명령 동시 전송
        self.move_joint(point)
        self.move_gripper(random_gripper_pos)

    def joint_callback(self, msg: JointState):
        self.current_joint_position = msg.position

    # --- 그리퍼 제어 비동기 액션 구현 부 ---
    def move_gripper(self, position: float, max_effort=10.0, timeout_sec=1.0):
        if not self.gripper_client.wait_for_server(timeout_sec=timeout_sec):
            return
        goal = GripperCommand.Goal()
        goal.command.position = float(position)
        goal.command.max_effort = float(max_effort)
        
        send_goal_future = self.gripper_client.send_goal_async(goal)
        send_goal_future.add_done_callback(self.goal_callback)

    def goal_callback(self, future: Future):
        self.goal_handle = future.result()
        self.get_result_future = self.goal_handle.get_result_async()
        self.get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future: Future):
        result: GripperCommand_GetResult_Response = future.result()
        if result.status == GoalStatus.STATUS_SUCCEEDED:
            self.get_logger().info(f"[그리퍼] 이동 완료: {result.result.position:.4f}m")

    # --- 관절 Trajectory 제어 비동기 액션 구현 부 ---
    def move_joint(self, point: JointTrajectoryPoint):
        if not self.joint_client.wait_for_server(timeout_sec=1.0):
            self.get_logger().warn("joint_controller 액션 서버를 찾지 못했습니다.")
            return
        
        goal = FollowJointTrajectory.Goal()
        goal.trajectory.header.stamp = self.get_clock().now().to_msg()
        goal.trajectory.header.frame_id = "move_manipulator"
        goal.trajectory.joint_names = ["joint1", "joint2", "joint3", "joint4"]
        goal.trajectory.points.append(point)

        send_goal_future = self.joint_client.send_goal_async(goal)
        send_goal_future.add_done_callback(self.goal_joint_callback)

    def goal_joint_callback(self, future: Future):
        self.goal_handle = future.result()
        self.get_result_future = self.goal_handle.get_result_async()
        self.get_result_future.add_done_callback(self.get_joint_result_callback)

    def get_joint_result_callback(self, future: Future):
        result: FollowJointTrajectory_GetResult_Response = future.result()
        if result.status == GoalStatus.STATUS_SUCCEEDED:
            formatted_pose = ", ".join([f"{p:.3f}" for p in self.current_joint_position[:4]])
            self.get_logger().info(f"[로봇팔] 댄스 스텝 성공! 현재 각도: [{formatted_pose}]")
        elif result.status == GoalStatus.STATUS_ABORTED:
            self.get_logger().error("[로봇팔] 조인트 궤적 추종 액션이 중단되었습니다.")


def main(args=None):
    rclpy.init(args=args)
    node = DanceManipulatorAction()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("\n[인터럽트] 사용자의 요청으로 댄스 제어를 종료합니다.")
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()