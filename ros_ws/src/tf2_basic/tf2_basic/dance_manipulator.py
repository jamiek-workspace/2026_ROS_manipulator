# 과제
# 로봇팔을 움직여서 춤추는 동작을 구현하시오.
# random 함수를 활용
# position 정보는 data 파일을 로드해서 구현(txt, yaml, sqlite...)

import random
from pathlib import Path
from typing import Any

import rclpy
import yaml
from action_msgs.msg import GoalStatus
from ament_index_python.packages import get_package_share_directory
from control_msgs.action import (
    GripperCommand,
    GripperCommand_GetResult_Response,
)
from rclpy.action import ActionClient
from rclpy.node import Node
from rclpy.task import Future
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint


class DanceManipulator(Node):
    def __init__(self):
        super().__init__("dance_manipulator")

        # 관절 명령 퍼블리셔
        self.arm_publisher = self.create_publisher(
            JointTrajectory,
            "/arm_controller/joint_trajectory",
            10,
        )

        # 그리퍼 액션 클라이언트
        self.gripper_client = ActionClient(
            self,
            GripperCommand,
            "/gripper_controller/gripper_cmd",
        )

        self.duration_sec = 2.0
        self.timer_period_sec = 2.5

        self.joint_names: list[str] = []
        self.poses: list[dict[str, Any]] = []
        self.previous_pose_index: int | None = None

        self.load_dance_positions()

        # YAML을 정상적으로 읽은 뒤 타이머 시작
        self.timer = self.create_timer(
            self.timer_period_sec,
            self.timer_callback,
        )

        self.get_logger().info(
            f"춤 동작 {len(self.poses)}개를 불러왔습니다."
        )

    def load_dance_positions(self):
        """설치된 패키지의 YAML 파일에서 춤 동작을 읽는다."""

        package_share_directory = Path(
            get_package_share_directory("tf2_basic")
        )

        yaml_path = (
            package_share_directory
            / "data"
            / "dance_positions.yaml"
        )

        if not yaml_path.exists():
            raise FileNotFoundError(
                f"춤 동작 파일을 찾을 수 없습니다: {yaml_path}"
            )

        with yaml_path.open("r", encoding="utf-8") as file:
            dance_data = yaml.safe_load(file)

        if not isinstance(dance_data, dict):
            raise ValueError("YAML 최상위 데이터는 dictionary여야 합니다.")

        joint_names = dance_data.get("joint_names")
        poses = dance_data.get("poses")

        if not isinstance(joint_names, list):
            raise ValueError("joint_names가 올바르지 않습니다.")

        if len(joint_names) != 4:
            raise ValueError(
                f"joint_names는 4개여야 합니다. 현재: {len(joint_names)}개"
            )

        if not isinstance(poses, list) or len(poses) == 0:
            raise ValueError("poses에 춤 동작이 하나 이상 필요합니다.")

        for pose_index, pose in enumerate(poses):
            if not isinstance(pose, dict):
                raise ValueError(
                    f"poses[{pose_index}]가 dictionary가 아닙니다."
                )

            positions = pose.get("positions")

            if not isinstance(positions, list):
                raise ValueError(
                    f"poses[{pose_index}].positions가 올바르지 않습니다."
                )

            if len(positions) != len(joint_names):
                raise ValueError(
                    f"poses[{pose_index}]의 관절값 개수가 "
                    f"{len(joint_names)}개가 아닙니다."
                )

            # 모든 관절값을 float로 변환
            pose["positions"] = [
                float(position) for position in positions
            ]

            if "gripper" in pose:
                pose["gripper"] = float(pose["gripper"])

        self.joint_names = joint_names
        self.poses = poses

    def select_random_pose(self) -> tuple[int, dict[str, Any]]:
        """직전 자세와 다른 자세를 무작위로 선택한다."""

        if len(self.poses) == 1:
            return 0, self.poses[0]

        available_indices = [
            index
            for index in range(len(self.poses))
            if index != self.previous_pose_index
        ]

        # random 함수를 이용해 후보 중 하나 선택
        selected_index = random.choice(available_indices)
        selected_pose = self.poses[selected_index]

        self.previous_pose_index = selected_index

        return selected_index, selected_pose

    def timer_callback(self):
        """타이머마다 무작위 춤 동작 하나를 실행한다."""

        pose_index, pose = self.select_random_pose()

        pose_name = pose.get("name", f"pose_{pose_index}")
        positions = pose["positions"]

        trajectory_message = JointTrajectory()
        trajectory_message.header.stamp = (
            self.get_clock().now().to_msg()
        )
        trajectory_message.header.frame_id = "dance_manipulator"
        trajectory_message.joint_names = self.joint_names

        point = JointTrajectoryPoint()
        point.positions = positions

        seconds = int(self.duration_sec)
        nanoseconds = int(
            (self.duration_sec - seconds) * 1_000_000_000
        )

        point.time_from_start.sec = seconds
        point.time_from_start.nanosec = nanoseconds

        trajectory_message.points.append(point)
        self.arm_publisher.publish(trajectory_message)

        self.get_logger().info(
            f"춤 동작 실행: {pose_name} | "
            f"positions={positions}"
        )

        # 해당 자세에 gripper 값이 있을 때만 동작
        gripper_position = pose.get("gripper")

        if gripper_position is not None:
            self.move_gripper(gripper_position)

    def move_gripper(
        self,
        position: float,
        max_effort: float = 10.0,
        timeout_sec: float = 1.0,
    ):
        if not self.gripper_client.wait_for_server(
            timeout_sec=timeout_sec
        ):
            self.get_logger().warning(
                "gripper_controller 액션 서버를 찾지 못했습니다."
            )
            return

        goal = GripperCommand.Goal()
        goal.command.position = float(position)
        goal.command.max_effort = float(max_effort)

        send_goal_future = self.gripper_client.send_goal_async(goal)
        send_goal_future.add_done_callback(
            self.gripper_goal_response_callback
        )

    def gripper_goal_response_callback(self, future: Future):
        try:
            goal_handle = future.result()
        except Exception as error:
            self.get_logger().error(
                f"그리퍼 목표 전송 실패: {error}"
            )
            return

        if not goal_handle.accepted:
            self.get_logger().warning(
                "그리퍼 목표가 거부되었습니다."
            )
            return

        result_future = goal_handle.get_result_async()
        result_future.add_done_callback(
            self.gripper_result_callback
        )

    def gripper_result_callback(self, future: Future):
        try:
            response: GripperCommand_GetResult_Response = (
                future.result()
            )
        except Exception as error:
            self.get_logger().error(
                f"그리퍼 결과 처리 실패: {error}"
            )
            return

        if response.status == GoalStatus.STATUS_SUCCEEDED:
            self.get_logger().info(
                f"그리퍼 동작 완료: "
                f"{response.result.position:.4f}"
            )
        elif response.status == GoalStatus.STATUS_ABORTED:
            self.get_logger().warning(
                "그리퍼 동작이 중단되었습니다."
            )
        elif response.status == GoalStatus.STATUS_CANCELED:
            self.get_logger().warning(
                "그리퍼 동작이 취소되었습니다."
            )


def main(args=None):
    rclpy.init(args=args)

    node = None

    try:
        node = DanceManipulator()
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("\n춤 동작을 종료합니다.")
    except Exception as error:
        print(f"실행 중 오류가 발생했습니다: {error}")
    finally:
        if node is not None:
            node.destroy_node()

        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()