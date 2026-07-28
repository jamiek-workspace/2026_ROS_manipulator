"""기록된 OpenManipulator-X 동작을 재생하는 노드."""

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
from trajectory_msgs.msg import (
    JointTrajectory,
    JointTrajectoryPoint,
)


def find_recording_file() -> Path:
    """recorded_dance.yaml 파일을 찾는다."""

    source_data = (
        Path.home()
        / "2026_ROS_manipulator"
        / "ros_ws"
        / "src"
        / "tf2_basic"
        / "data"
    )

    source_file = source_data / "recorded_grip.yaml"

    # 개발 중에는 src/tf2_basic/data 파일을 우선 사용
    if source_file.is_file():
        return source_file.resolve()

    # 설치된 패키지의 data 폴더 확인
    try:
        share_data = (
            Path(get_package_share_directory("tf2_basic"))
            / "data"
        )

        installed_file = share_data / "recorded_grip.yaml"

        if installed_file.is_file():
            return installed_file.resolve()

    except Exception:
        pass

    raise FileNotFoundError(
        "recorded_dance.yaml을 찾을 수 없습니다.\n"
        f"확인할 위치: {source_file}"
    )


class RecordedDancePlayer(Node):
    """recorded_dance.yaml에 저장된 동작을 순서대로 재생한다."""

    JOINT_NAMES = [
        "joint1",
        "joint2",
        "joint3",
        "joint4",
    ]

    def __init__(self) -> None:
        super().__init__("play_recorded_dance")

        default_file = find_recording_file()

        # 실행할 YAML 파일을 ROS 파라미터로 지정 가능
        self.declare_parameter(
            "dance_file",
            str(default_file),
        )

        # 마지막 동작 후 다시 처음부터 반복할지 결정
        self.declare_parameter(
            "loop",
            False,
        )

        selected_file = str(
            self.get_parameter("dance_file").value
        )
        self.loop = bool(
            self.get_parameter("loop").value
        )

        self.dance_file = Path(selected_file).expanduser()

        self.arm_publisher = self.create_publisher(
            JointTrajectory,
            "/arm_controller/joint_trajectory",
            10,
        )

        self.gripper_client = ActionClient(
            self,
            GripperCommand,
            "/gripper_controller/gripper_cmd",
        )

        self.joint_names: list[str] = []
        self.steps: list[dict[str, Any]] = []

        self.current_step_index = 0
        self.waiting = False
        self.finished = False

        self.load_recorded_dance()

        # 첫 실행을 약간 늦춰 bringup이 준비될 시간을 줌
        self.timer = self.create_timer(
            0.1,
            self.timer_callback,
        )

        self.next_execution_time = (
            self.get_clock().now().nanoseconds
            + int(1.0 * 1_000_000_000)
        )

        self.get_logger().info(
            f"녹화 동작 파일: {self.dance_file}"
        )
        self.get_logger().info(
            f"총 {len(self.steps)}개 동작을 불러왔습니다."
        )
        self.get_logger().info(
            f"반복 재생: {self.loop}"
        )
        self.get_logger().warning(
            "재생 전에 모터 토크가 ON인지 확인하고 "
            "로봇 주변을 비우세요."
        )

    def load_recorded_dance(self) -> None:
        """recorded_dance.yaml을 읽고 검증한다."""

        if not self.dance_file.is_file():
            raise FileNotFoundError(
                f"녹화 동작 파일을 찾을 수 없습니다: "
                f"{self.dance_file}"
            )

        with self.dance_file.open(
            "r",
            encoding="utf-8",
        ) as file:
            dance_data = yaml.safe_load(file)

        if not isinstance(dance_data, dict):
            raise ValueError(
                "recorded_dance.yaml이 비어 있거나 "
                "최상위 데이터가 dictionary가 아닙니다."
            )

        joint_names = dance_data.get("joint_names")

        if not isinstance(joint_names, list):
            raise ValueError(
                "joint_names 항목이 없거나 list가 아닙니다."
            )

        if len(joint_names) != 4:
            raise ValueError(
                "joint_names에는 관절 이름 4개가 필요합니다. "
                f"현재: {len(joint_names)}개"
            )

        patterns = dance_data.get("patterns")

        if not isinstance(patterns, list) or not patterns:
            raise ValueError(
                "patterns 항목에 동작이 하나 이상 필요합니다."
            )

        loaded_steps: list[dict[str, Any]] = []

        for pattern_index, pattern in enumerate(patterns):
            if not isinstance(pattern, dict):
                raise ValueError(
                    f"patterns[{pattern_index}]가 "
                    "dictionary가 아닙니다."
                )

            pattern_name = pattern.get(
                "name",
                f"pattern_{pattern_index}",
            )

            steps = pattern.get("steps")

            if not isinstance(steps, list):
                raise ValueError(
                    f"patterns[{pattern_index}].steps가 "
                    "list가 아닙니다."
                )

            for step_index, step in enumerate(steps):
                if not isinstance(step, dict):
                    raise ValueError(
                        f"patterns[{pattern_index}]"
                        f".steps[{step_index}]가 "
                        "dictionary가 아닙니다."
                    )

                positions = step.get("positions")

                if (
                    not isinstance(positions, list)
                    or len(positions) != 4
                ):
                    raise ValueError(
                        f"{pattern_name}의 "
                        f"steps[{step_index}].positions에는 "
                        "관절값 4개가 필요합니다."
                    )

                try:
                    positions = [
                        float(value)
                        for value in positions
                    ]
                except (TypeError, ValueError) as error:
                    raise ValueError(
                        f"{pattern_name}의 "
                        f"steps[{step_index}] 관절값이 "
                        "숫자가 아닙니다."
                    ) from error

                gripper = step.get("gripper")

                # teach_manipulator가 [0.01]처럼
                # 리스트로 저장하는 경우 처리
                if isinstance(gripper, list):
                    if gripper:
                        gripper = gripper[0]
                    else:
                        gripper = None

                if gripper is not None:
                    try:
                        gripper = float(gripper)
                    except (TypeError, ValueError) as error:
                        raise ValueError(
                            f"{pattern_name}의 "
                            f"steps[{step_index}].gripper가 "
                            "숫자가 아닙니다."
                        ) from error

                try:
                    duration = float(
                        step.get("duration", 1.0)
                    )
                    pause = float(
                        step.get("pause", 0.2)
                    )
                except (TypeError, ValueError) as error:
                    raise ValueError(
                        f"{pattern_name}의 "
                        f"steps[{step_index}]에서 "
                        "duration 또는 pause가 "
                        "숫자가 아닙니다."
                    ) from error

                if duration <= 0.0:
                    raise ValueError(
                        f"{pattern_name}의 "
                        f"steps[{step_index}].duration은 "
                        "0보다 커야 합니다."
                    )

                if pause < 0.0:
                    raise ValueError(
                        f"{pattern_name}의 "
                        f"steps[{step_index}].pause는 "
                        "0 이상이어야 합니다."
                    )

                loaded_steps.append(
                    {
                        "name": (
                            f"{pattern_name}_"
                            f"{step_index + 1}"
                        ),
                        "positions": positions,
                        "gripper": gripper,
                        "duration": duration,
                        "pause": pause,
                    }
                )

        if not loaded_steps:
            raise ValueError(
                "recorded_dance.yaml에 재생할 동작이 없습니다."
            )

        self.joint_names = joint_names
        self.steps = loaded_steps

    def timer_callback(self) -> None:
        """정해진 시간이 되면 다음 동작을 실행한다."""

        if self.finished or self.waiting:
            return

        now_nanoseconds = (
            self.get_clock().now().nanoseconds
        )

        if now_nanoseconds < self.next_execution_time:
            return

        if self.current_step_index >= len(self.steps):
            if self.loop:
                self.get_logger().info(
                    "처음부터 다시 재생합니다."
                )
                self.current_step_index = 0
            else:
                self.finished = True
                self.get_logger().info(
                    "모든 녹화 동작의 재생이 완료되었습니다."
                )
                return

        step = self.steps[self.current_step_index]

        self.execute_step(step)

        duration = float(step["duration"])
        pause = float(step["pause"])

        self.next_execution_time = (
            now_nanoseconds
            + int(
                (duration + pause)
                * 1_000_000_000
            )
        )

        self.current_step_index += 1

    def execute_step(
        self,
        step: dict[str, Any],
    ) -> None:
        """관절과 그리퍼 목표를 전송한다."""

        positions = step["positions"]
        duration = float(step["duration"])

        trajectory_message = JointTrajectory()
        trajectory_message.header.stamp = (
            self.get_clock().now().to_msg()
        )
        trajectory_message.header.frame_id = (
            "play_recorded_dance"
        )
        trajectory_message.joint_names = (
            self.joint_names
        )

        point = JointTrajectoryPoint()
        point.positions = positions

        seconds = int(duration)
        nanoseconds = int(
            (duration - seconds)
            * 1_000_000_000
        )

        point.time_from_start.sec = seconds
        point.time_from_start.nanosec = nanoseconds

        trajectory_message.points.append(point)

        self.arm_publisher.publish(
            trajectory_message
        )

        self.get_logger().info(
            f"[{self.current_step_index + 1}/"
            f"{len(self.steps)}] "
            f"{step['name']} 실행 | "
            f"positions={positions} | "
            f"duration={duration:.2f}s"
        )

        gripper_position = step.get("gripper")

        if gripper_position is not None:
            self.move_gripper(
                float(gripper_position)
            )

    def move_gripper(
        self,
        position: float,
        max_effort: float = 10.0,
    ) -> None:
        """그리퍼 액션 목표를 전송한다."""

        if not self.gripper_client.wait_for_server(
            timeout_sec=1.0
        ):
            self.get_logger().warning(
                "gripper_controller 액션 서버를 "
                "찾지 못했습니다."
            )
            return

        goal = GripperCommand.Goal()
        goal.command.position = position
        goal.command.max_effort = max_effort

        send_goal_future = (
            self.gripper_client.send_goal_async(
                goal
            )
        )

        send_goal_future.add_done_callback(
            self.gripper_goal_response_callback
        )

    def gripper_goal_response_callback(
        self,
        future: Future,
    ) -> None:
        """그리퍼 목표 수락 여부를 처리한다."""

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

        result_future = (
            goal_handle.get_result_async()
        )

        result_future.add_done_callback(
            self.gripper_result_callback
        )

    def gripper_result_callback(
        self,
        future: Future,
    ) -> None:
        """그리퍼 액션 결과를 처리한다."""

        try:
            response: (
                GripperCommand_GetResult_Response
            ) = future.result()
        except Exception as error:
            self.get_logger().error(
                f"그리퍼 결과 처리 실패: {error}"
            )
            return

        if (
            response.status
            == GoalStatus.STATUS_SUCCEEDED
        ):
            self.get_logger().info(
                "그리퍼 동작 완료"
            )

        elif (
            response.status
            == GoalStatus.STATUS_ABORTED
        ):
            self.get_logger().warning(
                "그리퍼 동작이 중단되었습니다."
            )

        elif (
            response.status
            == GoalStatus.STATUS_CANCELED
        ):
            self.get_logger().warning(
                "그리퍼 동작이 취소되었습니다."
            )


def main(
    args: list[str] | None = None,
) -> None:
    """노드를 실행한다."""

    rclpy.init(args=args)
    node = None

    try:
        node = RecordedDancePlayer()
        rclpy.spin(node)

    except (
        FileNotFoundError,
        ValueError,
        yaml.YAMLError,
    ) as error:
        if node is not None:
            node.get_logger().fatal(str(error))
        else:
            print(
                "play_recorded_dance 설정 오류: "
                f"{error}"
            )

    except KeyboardInterrupt:
        print(
            "\n녹화 동작 재생을 종료합니다."
        )

    except Exception as error:
        if node is not None:
            node.get_logger().fatal(
                f"실행 중 오류: {error}"
            )
        else:
            print(
                f"실행 중 오류가 발생했습니다: {error}"
            )

    finally:
        if node is not None:
            node.destroy_node()

        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()