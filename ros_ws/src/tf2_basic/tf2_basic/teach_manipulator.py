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
from std_srvs.srv import SetBool


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
        super().__init__("teach_manipulaotr")
        self.joint_state_subscription = self.create_subscription(
            JointState, "/joint_states", self.joint_state_callback, 10
        )
        # service call code
        self.torqu_service_client = self.create_client(
            SetBool, "dynamixel_hardware_interface/set_dxl_torque"
        )
        self.torqu_service_client.wait_for_service(timeout_sec=1.0)
        request = SetBool.Request()
        request.data = False
        future = self.torqu_service_client.call_async(request)
        future.add_done_callback(self.toque_response_callback)
        self.create_timer(0.3, self.poll_keyboard)

        self._latest_positions: dict[str, float] = {}
        self._stdin_fd = None
        self._quit_requested = False
        self._steps = []
        self._step_duration = 1.0
        self._step_pause = 0.2
        self._pattern_name = "test"
        self._stdin_fd = sys.stdin.fileno()
        self._terminal_settings = termios.tcgetattr(self._stdin_fd)
        tty.setcbreak(self._stdin_fd)

    def joint_state_callback(self, msg: JointState):
        # self.get_logger().info(f"{msg.position}")
        available = {
            name: float(msg.position[index])
            for index, name in enumerate(msg.name)
            if index < len(msg.position)
        }
        self._latest_positions = {
            name: available[name] for name in self.JOINT_NAMES + [self.GRIPPER_JOINT]
        }

    def toque_response_callback(self, future):
        response = future.result()
        if response is None or response.success:
            self.get_logger().info("실패")
        else:
            self.get_logger().info("성공")

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
        required = self.JOINT_NAMES + [self.GRIPPER_JOINT]
        positions = [round(self._latest_positions[name], 6) for name in self.JOINT_NAMES]
        gripper = [round(self._latest_positions[self.GRIPPER_JOINT], 6)]
        self._steps.append(
            {
                "positions": positions,
                "gripper": gripper,
                "duration": self._step_duration,
                "pause": self._step_pause,
            }
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

        output_path = os.path.join(output_dir, "teach_data.yaml")

        with open(output_path, "w", encoding="utf-8") as f:
            yaml.safe_dump(
                document,
                f,
                allow_unicode=True,
                sort_keys=False,
            )

        self.get_logger().info(f"YAML 저장 완료: {output_path}")

    def request_quit(self):
        print("exit")


def main(args=None):
    rclpy.init(args=args)
    node = TeachManipulator()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.try_shutdown()


if __name__ == "__main__":
    main()