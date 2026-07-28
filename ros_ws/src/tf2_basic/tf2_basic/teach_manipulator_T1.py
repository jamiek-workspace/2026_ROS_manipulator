# """손으로 만든 OpenManipulator-X 자세를 춤 YAML로 녹화하는 노드."""

from datetime import datetime
import os
from pathlib import Path
import select
import sys
import termios
import tty
from typing import Any

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from sensor_msgs.msg import JointState
from std_srvs.srv import SetBool
import yaml


class TeachManipulator(Node):
    """토크를 끄고 스페이스바로 현재 관절 자세를 기록한다."""

    JOINT_NAMES = ['joint1', 'joint2', 'joint3', 'joint4']
    GRIPPER_JOINT = 'gripper_left_joint'
    JOINT_LIMITS = {
        'joint1': [-3.14159265359, 3.14159265359],
        'joint2': [-1.5, 1.5],
        'joint3': [-1.5, 1.4],
        'joint4': [-1.7, 1.97],
    }
    GRIPPER_LIMITS = [-0.011, 0.02]

    def __init__(self) -> None:
        super().__init__('teach_manipulator')

        self.declare_parameter('output_file', '')
        self.declare_parameter(
            'torque_service',
            '/dynamixel_hardware_interface/set_dxl_torque',
        )
        self.declare_parameter('pattern_name', 'taught_motion')
        self.declare_parameter('step_duration', 1.0)
        self.declare_parameter('step_pause', 0.15)
        self.declare_parameter('variation_ratio', 0.0)
        self.declare_parameter('overwrite', False)

        self._output_path = self._resolve_output_path()
        self._pattern_name = str(self.get_parameter('pattern_name').value).strip()
        self._step_duration = float(
            self.get_parameter('step_duration').value
        )
        self._step_pause = float(self.get_parameter('step_pause').value)
        self._variation_ratio = float(
            self.get_parameter('variation_ratio').value
        )
        self._validate_parameters()

        self._latest_positions: dict[str, float] = {}
        self._steps: list[dict[str, Any]] = []
        self._torque_disabled = False
        self._torque_request_in_flight = False
        self._service_wait_count = 0
        self._terminal_settings: list[Any] | None = None
        self._stdin_fd: int | None = None
        self._quit_requested = False

        if not sys.stdin.isatty():
            raise RuntimeError(
                '키보드 입력이 가능한 터미널에서 실행해야 합니다.'
            )
        self._stdin_fd = sys.stdin.fileno()
        self._terminal_settings = termios.tcgetattr(self._stdin_fd)
        tty.setcbreak(self._stdin_fd)

        self._joint_state_subscription = self.create_subscription(
            JointState,
            '/joint_states',
            self._joint_state_callback,
            10,
        )
        service_name = str(self.get_parameter('torque_service').value)
        self._torque_client = self.create_client(SetBool, service_name)
        self._startup_timer = self.create_timer(
            0.2, self._disable_torque_when_ready
        )
        self._keyboard_timer = self.create_timer(0.03, self._poll_keyboard)

        self.get_logger().info(f'저장 예정 파일: {self._output_path}')
        self.get_logger().warning(
            '토크 서비스를 기다리는 중입니다. 로봇을 아직 손으로 움직이지 마세요.'
        )

    def _resolve_output_path(self) -> Path:
        configured = str(self.get_parameter('output_file').value).strip()
        if configured:
            path = Path(os.path.expandvars(configured)).expanduser()
            if not path.is_absolute():
                path = Path.cwd() / path
        else:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            path = Path.home() / f'recorded_dance_{timestamp}.yaml'
        path = path.resolve()
        overwrite = bool(self.get_parameter('overwrite').value)
        if path.exists() and not overwrite:
            raise FileExistsError(
                f'파일이 이미 존재합니다: {path} '
                '(-p overwrite:=true로 명시해야 덮어씁니다.)'
            )
        return path

    def _validate_parameters(self) -> None:
        if not self._pattern_name:
            raise ValueError('pattern_name은 비어 있을 수 없습니다.')
        if self._step_duration <= 0.0:
            raise ValueError('step_duration은 0보다 커야 합니다.')
        if self._step_pause < 0.0:
            raise ValueError('step_pause는 0 이상이어야 합니다.')
        if not 0.0 <= self._variation_ratio <= 0.05:
            raise ValueError('variation_ratio는 0.0~0.05여야 합니다.')

    def _joint_state_callback(self, message: JointState) -> None:
        available = {
            name: float(message.position[index])
            for index, name in enumerate(message.name)
            if index < len(message.position)
        }
        required = set(self.JOINT_NAMES + [self.GRIPPER_JOINT])
        if required.issubset(available):
            self._latest_positions = {
                name: available[name]
                for name in self.JOINT_NAMES + [self.GRIPPER_JOINT]
            }

    def _disable_torque_when_ready(self) -> None:
        if self._torque_disabled or self._torque_request_in_flight:
            return
        if not self._torque_client.service_is_ready():
            self._service_wait_count += 1
            if self._service_wait_count % 25 == 1:
                self.get_logger().info('토크 OFF 서비스를 기다리는 중...')
            return
        request = SetBool.Request()
        request.data = False
        self._torque_request_in_flight = True
        future = self._torque_client.call_async(request)
        future.add_done_callback(self._torque_off_response)

    def _torque_off_response(self, future: Any) -> None:
        self._torque_request_in_flight = False
        try:
            response = future.result()
        except Exception as error:
            self.get_logger().error(f'토크 OFF 서비스 호출 실패: {error}')
            return
        if response is None or not response.success:
            message = '응답 없음' if response is None else response.message
            self.get_logger().error(f'토크 OFF 실패: {message}')
            return
        self._torque_disabled = True
        self._startup_timer.cancel()
        self.destroy_timer(self._startup_timer)
        self.get_logger().warning(
            '토크가 OFF 되었습니다. 로봇팔을 반드시 손으로 지지하세요.'
        )
        self.get_logger().info(
            '[SPACE] 현재 자세 저장  [H] 도움말  [Q] 저장 종료'
        )

    def _poll_keyboard(self) -> None:
        if self._stdin_fd is None or self._quit_requested:
            return
        readable, _, _ = select.select([self._stdin_fd], [], [], 0.0)
        if not readable:
            return
        key = os.read(self._stdin_fd, 1)
        if key == b' ':
            self._capture_pose()
        elif key.lower() == b'h':
            self.get_logger().info(
                '[SPACE] 현재 자세 저장  [H] 도움말  [Q] 저장 종료'
            )
        elif key.lower() == b'q':
            self._request_quit()

    def _capture_pose(self) -> None:
        if not self._torque_disabled:
            self.get_logger().warning(
                '토크 OFF가 확인되지 않아 자세를 저장하지 않았습니다.'
            )
            return
        required = self.JOINT_NAMES + [self.GRIPPER_JOINT]
        if not all(name in self._latest_positions for name in required):
            self.get_logger().warning(
                '/joint_states에서 모든 관절값을 아직 받지 못했습니다.'
            )
            return

        positions = [
            round(self._latest_positions[name], 6)
            for name in self.JOINT_NAMES
        ]
        gripper = round(
            self._latest_positions[self.GRIPPER_JOINT], 6
        )
        self._steps.append(
            {
                'positions': positions,
                'gripper': gripper,
                'duration': self._step_duration,
                'pause': self._step_pause,
            }
        )
        self._write_yaml()
        values = ', '.join(f'{value:+.4f}' for value in positions)
        self.get_logger().info(
            f'자세 {len(self._steps)} 저장: '
            f'joint=[{values}], gripper={gripper:+.5f}'
        )

    def _write_yaml(self) -> None:
        document = {
            'joint_names': self.JOINT_NAMES,
            'joint_limits': self.JOINT_LIMITS,
            'gripper_limits': self.GRIPPER_LIMITS,
            'randomization': {
                'variation_ratio': self._variation_ratio,
                'minimum_joint_jitter': 0.01,
                'minimum_gripper_jitter': 0.0002,
                'shuffle_patterns': False,
                'shuffle_steps': False,
            },
            'execution': {
                'repeat_count': 1,
                'default_duration': self._step_duration,
                'default_pause': self._step_pause,
                'gripper_max_effort': 5.0,
            },
            'patterns': [
                {
                    'name': self._pattern_name,
                    'steps': self._steps,
                }
            ],
        }
        self._output_path.parent.mkdir(parents=True, exist_ok=True)
        temporary = self._output_path.with_suffix(
            self._output_path.suffix + '.tmp'
        )
        with temporary.open('w', encoding='utf-8') as stream:
            yaml.safe_dump(
                document,
                stream,
                allow_unicode=True,
                sort_keys=False,
            )
        temporary.replace(self._output_path)

    def _request_quit(self) -> None:
        self._quit_requested = True
        self._restore_terminal()
        if self._steps:
            self.get_logger().info(
                f'{len(self._steps)}개 자세 저장 완료: {self._output_path}'
            )
        else:
            self.get_logger().warning('저장된 자세가 없어 YAML을 만들지 않았습니다.')
        self.get_logger().warning(
            '종료 후에도 토크는 OFF 상태입니다. '
            'controller 목표를 확인하기 전에는 토크를 다시 켜지 마세요.'
        )
        rclpy.shutdown()

    def _restore_terminal(self) -> None:
        if self._stdin_fd is None or self._terminal_settings is None:
            return
        termios.tcsetattr(
            self._stdin_fd,
            termios.TCSADRAIN,
            self._terminal_settings,
        )
        self._terminal_settings = None

    def destroy_node(self) -> bool:
        self._restore_terminal()
        return super().destroy_node()


def main(args: list[str] | None = None) -> None:
    rclpy.init(args=args)
    node = None
    try:
        node = TeachManipulator()
        rclpy.spin(node)
    except (
        ExternalShutdownException,
        FileExistsError,
        KeyboardInterrupt,
        OSError,
        RuntimeError,
        ValueError,
    ) as error:
        if not isinstance(error, (ExternalShutdownException, KeyboardInterrupt)):
            if node is not None:
                node.get_logger().fatal(str(error))
            else:
                print(f'teach_manipulator 오류: {error}')
    finally:
        if node is not None:
            node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()