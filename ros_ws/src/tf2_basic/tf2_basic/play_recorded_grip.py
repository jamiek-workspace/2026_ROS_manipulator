# yaml 로 녹화 하는 모드
# ros2 service call \
#   /dynamixel_hardware_interface/set_dxl_torque \
#   std_srvs/srv/SetBool \
#   "{data: false}"
# 스페이스바 인식. 완료
# yaml 파일을 저장

import os
import select
import sys
import termios
import tty

import rclpy
import yaml
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from sensor_msgs.msg import JointState


class TeachManipulator(Node):
    JOINT_NAMES = ["joint1", "joint2", "joint3", "joint4"]
    GRIPPER_JOINT = "gripper_left_joint"
    JOINT_LIMITS = {
        "joint1": [-3.14159265359, 3.14159265359],
        "joint2": [-1.5, 1.5],
        "joint3": [-1.5, 1.4],
        "joint4": [-1.7, 1.97],
    }
    GRIPPER_LIMITS = [-0.011, 0.02]

    def __init__(self):
        super().__init__("record_grip_with_teleop")

        self.joint_state_subscription = self.create_subscription(
            JointState,
            "/joint_states",
            self.joint_state_callback,
            10,
        )

        self._latest_positions: dict[str, float] = {}
        self._quit_requested = False
        self._steps = []

        self._step_duration = 1.0
        self._step_pause = 0.2
        self._pattern_name = "test"

        self._stdin_fd = sys.stdin.fileno()
        self._terminal_settings = termios.tcgetattr(
            self._stdin_fd
        )
        tty.setcbreak(self._stdin_fd)

        self.create_timer(
            0.1,
            self.poll_keyboard,
        )

        self.get_logger().info(
            "Teleop 기록 모드가 시작되었습니다."
        )
        self.get_logger().info(
            "다른 터미널에서 Teleop으로 로봇을 움직인 뒤 "
            "이 터미널에서 Space를 누르세요."
        )
        self.get_logger().info(
            "종료하려면 q를 누르세요."
        )

    def joint_state_callback(
        self,
        msg: JointState,
    ):
        available = {
            name: float(msg.position[index])
            for index, name in enumerate(msg.name)
            if index < len(msg.position)
        }

        required = (
            self.JOINT_NAMES
            + [self.GRIPPER_JOINT]
        )

        self._latest_positions = {
            name: available[name]
            for name in required
            if name in available
        }


    def poll_keyboard(self):
        if self._stdin_fd is None or self._quit_requested:
            return
        readable, _, _ = select.select([self._stdin_fd], [], [], 0.0)
        if not readable:
            return
        key = os.read(self._stdin_fd, 1)
        if key == b" ":
            self.capture_pose()
        if key.lower() == b"q":
            self.request_quit()

    def capture_pose(self):
        required = (
            self.JOINT_NAMES
            + [self.GRIPPER_JOINT]
        )

        missing = [
            name
            for name in required
            if name not in self._latest_positions
        ]

        if missing:
            self.get_logger().warning(
                "아직 joint_states에서 다음 관절을 "
                f"받지 못했습니다: {missing}"
            )
            return

        positions = [
            round(
                self._latest_positions[name],
                6,
            )
            for name in self.JOINT_NAMES
        ]

        gripper_position = round(
            self._latest_positions[
                self.GRIPPER_JOINT
            ],
            6,
        )

        self._steps.append(
            {
                "positions": positions,
                "gripper": [gripper_position],
                "duration": self._step_duration,
                "pause": self._step_pause,
            }
        )

        self.get_logger().info(
            f"{len(self._steps)}번째 자세 기록 완료 | "
            f"positions={positions} | "
            f"gripper={gripper_position}"
        )

        self._write_yaml()

    def _write_yaml(self):
        document = {
            "joint_names": self.JOINT_NAMES,
            "joint_limits": self.JOINT_LIMITS,
            "patterns": [
                {
                    "name": self._pattern_name,
                    "steps": self._steps,
                }
            ],
        }

        output_dir = os.path.expanduser(
            "~/2026_ROS_manipulator/ros_ws/src/tf2_basic/data"
        )
        os.makedirs(output_dir, exist_ok=True)

        output_path = os.path.join(output_dir, "recorded_grip.yaml")

        with open(output_path, "w", encoding="utf-8") as f:
            yaml.safe_dump(
                document,
                f,
                allow_unicode=True,
                sort_keys=False,
            )

        self.get_logger().info(f"YAML 저장 완료: {output_path}")

    def request_quit(self):
        self._quit_requested = True
        self.get_logger().info("녹화를 종료합니다.")
        rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    node = TeachManipulator()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if node._stdin_fd is not None:
            termios.tcsetattr(
                node._stdin_fd,
                termios.TCSADRAIN,
                node._terminal_settings,
    )


if __name__ == "__main__":
    main()