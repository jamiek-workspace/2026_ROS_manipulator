#!/usr/bin/env python3
"""Read an ArUco marker TF and prepare a MoveIt pick sequence."""

from __future__ import annotations

from collections import deque
from enum import Enum, auto
import math
import threading
from typing import Optional

import rclpy
from geometry_msgs.msg import PoseStamped, TransformStamped
from rclpy.duration import Duration
from rclpy.executors import MultiThreadedExecutor
from rclpy.node import Node
from rclpy.time import Time
from std_srvs.srv import Trigger
from tf2_ros import Buffer, TransformException, TransformListener


class PickState(Enum):
    """State of the ArUco pick sequence."""

    WAITING_FOR_MARKER = auto()
    READY = auto()
    MOVING_TO_PRE_GRASP = auto()
    OPENING_GRIPPER = auto()
    MOVING_TO_GRASP = auto()
    CLOSING_GRIPPER = auto()
    ATTACHING_OBJECT = auto()
    LIFTING_OBJECT = auto()
    DONE = auto()
    ERROR = auto()


class ArucoPickNode(Node):
    """Prepare a MoveIt pick sequence from an ArUco marker TF."""

    def __init__(self) -> None:
        super().__init__("aruco_pick_node")

        # ---------------------------------------------------------
        # ROS parameters
        # ---------------------------------------------------------
        self.declare_parameter("planning_frame", "world")
        self.declare_parameter("marker_frame", "aruco_marker_0")

        # 마커 위에서 대기할 높이
        self.declare_parameter("pre_grasp_offset_z", 0.10)

        # 마커 기준 실제 grasp 목표 높이
        self.declare_parameter("grasp_offset_z", 0.03)

        # 물체를 잡은 뒤 들어 올릴 거리
        self.declare_parameter("lift_distance", 0.10)

        # 마커 위치 안정성 판단
        self.declare_parameter("stable_sample_count", 10)
        self.declare_parameter("stable_position_tolerance", 0.01)

        # 처음에는 자동 실행을 끄는 것을 권장
        self.declare_parameter("auto_start", False)

        self.planning_frame = str(
            self.get_parameter("planning_frame").value
        )
        self.marker_frame = str(
            self.get_parameter("marker_frame").value
        )

        self.pre_grasp_offset_z = float(
            self.get_parameter("pre_grasp_offset_z").value
        )
        self.grasp_offset_z = float(
            self.get_parameter("grasp_offset_z").value
        )
        self.lift_distance = float(
            self.get_parameter("lift_distance").value
        )

        self.stable_sample_count = int(
            self.get_parameter("stable_sample_count").value
        )
        self.stable_position_tolerance = float(
            self.get_parameter("stable_position_tolerance").value
        )
        self.auto_start = bool(
            self.get_parameter("auto_start").value
        )

        if self.stable_sample_count < 2:
            raise ValueError("stable_sample_count는 2 이상이어야 합니다.")

        # ---------------------------------------------------------
        # TF2
        # ---------------------------------------------------------
        self.tf_buffer = Buffer(
            cache_time=Duration(seconds=10.0)
        )
        self.tf_listener = TransformListener(
            self.tf_buffer,
            self,
        )

        # ---------------------------------------------------------
        # Marker tracking
        # ---------------------------------------------------------
        self.marker_samples: deque[tuple[float, float, float]] = deque(
            maxlen=self.stable_sample_count
        )

        self.latest_marker_transform: Optional[TransformStamped] = None
        self.stable_marker_transform: Optional[TransformStamped] = None

        self.marker_detected = False
        self.marker_stable = False

        # ---------------------------------------------------------
        # Pick state
        # ---------------------------------------------------------
        self.state = PickState.WAITING_FOR_MARKER
        self.pick_started = False
        self.pick_lock = threading.Lock()

        # ---------------------------------------------------------
        # Service
        # ---------------------------------------------------------
        self.start_pick_service = self.create_service(
            Trigger,
            "/start_aruco_pick",
            self.start_pick_callback,
        )

        # TF를 10 Hz로 확인
        self.tf_timer = self.create_timer(
            0.1,
            self.update_marker_transform,
        )

        self.get_logger().info(
            "Aruco pick node 시작: "
            f"planning_frame={self.planning_frame}, "
            f"marker_frame={self.marker_frame}, "
            f"auto_start={self.auto_start}"
        )

        self.get_logger().info(
            "마커가 안정적으로 검출된 뒤 다음 서비스로 시작하세요: "
            "ros2 service call /start_aruco_pick std_srvs/srv/Trigger"
        )

    # ---------------------------------------------------------
    # TF acquisition
    # ---------------------------------------------------------
    def update_marker_transform(self) -> None:
        """Read planning_frame -> marker_frame and test position stability."""

        try:
            transform = self.tf_buffer.lookup_transform(
                self.planning_frame,
                self.marker_frame,
                Time(),
                timeout=Duration(seconds=0.05),
            )

        except TransformException as error:
            if self.marker_detected:
                self.get_logger().warn(
                    f"마커 TF를 잃었습니다: {error}",
                    throttle_duration_sec=2.0,
                )

            self.marker_detected = False
            self.marker_stable = False
            self.marker_samples.clear()

            if not self.pick_started:
                self.state = PickState.WAITING_FOR_MARKER

            return

        self.marker_detected = True
        self.latest_marker_transform = transform

        translation = transform.transform.translation

        sample = (
            float(translation.x),
            float(translation.y),
            float(translation.z),
        )
        self.marker_samples.append(sample)

        if len(self.marker_samples) < self.stable_sample_count:
            self.get_logger().info(
                f"마커 안정화 중: "
                f"{len(self.marker_samples)}/{self.stable_sample_count}",
                throttle_duration_sec=1.0,
            )
            return

        self.marker_stable = self.is_marker_position_stable()

        if not self.marker_stable:
            self.state = PickState.WAITING_FOR_MARKER
            self.get_logger().warn(
                "마커 위치가 아직 흔들리고 있습니다.",
                throttle_duration_sec=1.0,
            )
            return

        self.stable_marker_transform = transform

        if not self.pick_started:
            self.state = PickState.READY

        self.log_marker_pose(transform)

        if self.auto_start and not self.pick_started:
            self.start_pick_sequence_async()

    def is_marker_position_stable(self) -> bool:
        """Return True when recent marker positions are sufficiently stable."""

        if len(self.marker_samples) < self.stable_sample_count:
            return False

        xs = [sample[0] for sample in self.marker_samples]
        ys = [sample[1] for sample in self.marker_samples]
        zs = [sample[2] for sample in self.marker_samples]

        spread_x = max(xs) - min(xs)
        spread_y = max(ys) - min(ys)
        spread_z = max(zs) - min(zs)

        maximum_spread = max(
            spread_x,
            spread_y,
            spread_z,
        )

        return maximum_spread <= self.stable_position_tolerance

    def log_marker_pose(self, transform: TransformStamped) -> None:
        """Print the current stable marker position."""

        position = transform.transform.translation

        self.get_logger().info(
            "안정된 ArUco 위치: "
            f"x={position.x:.3f}, "
            f"y={position.y:.3f}, "
            f"z={position.z:.3f} "
            f"[{self.planning_frame}]",
            throttle_duration_sec=1.0,
        )

    # ---------------------------------------------------------
    # Start trigger
    # ---------------------------------------------------------
    def start_pick_callback(
        self,
        request: Trigger.Request,
        response: Trigger.Response,
    ) -> Trigger.Response:
        """Start the pick sequence after marker validation."""

        del request

        if self.pick_started:
            response.success = False
            response.message = "Pick 동작이 이미 실행 중이거나 완료되었습니다."
            return response

        if not self.marker_detected:
            response.success = False
            response.message = (
                f"{self.marker_frame} TF가 아직 검출되지 않았습니다."
            )
            return response

        if not self.marker_stable:
            response.success = False
            response.message = "마커 위치가 아직 안정적이지 않습니다."
            return response

        self.start_pick_sequence_async()

        response.success = True
        response.message = "ArUco pick sequence를 시작합니다."
        return response

    def start_pick_sequence_async(self) -> None:
        """Run the blocking pick procedure outside ROS callbacks."""

        with self.pick_lock:
            if self.pick_started:
                return

            self.pick_started = True

        worker = threading.Thread(
            target=self.execute_pick_sequence,
            daemon=True,
        )
        worker.start()

    # ---------------------------------------------------------
    # Pick sequence
    # ---------------------------------------------------------
    def execute_pick_sequence(self) -> None:
        """Execute pre-grasp, grasp, close, attach, and lift stages."""

        try:
            marker_transform = self.stable_marker_transform

            if marker_transform is None:
                raise RuntimeError("안정된 마커 Transform이 없습니다.")

            pre_grasp_pose = self.create_target_pose(
                marker_transform=marker_transform,
                offset_z=self.pre_grasp_offset_z,
            )

            grasp_pose = self.create_target_pose(
                marker_transform=marker_transform,
                offset_z=self.grasp_offset_z,
            )

            lift_pose = self.create_target_pose(
                marker_transform=marker_transform,
                offset_z=(
                    self.grasp_offset_z
                    + self.lift_distance
                ),
            )

            self.get_logger().info(
                "Pick 목표 자세 계산 완료:"
                f"\n  pre-grasp={self.pose_to_text(pre_grasp_pose)}"
                f"\n  grasp={self.pose_to_text(grasp_pose)}"
                f"\n  lift={self.pose_to_text(lift_pose)}"
            )

            # -------------------------------------------------
            # STEP 1: pre-grasp
            # -------------------------------------------------
            self.state = PickState.MOVING_TO_PRE_GRASP
            self.get_logger().info("[1/6] Pre-grasp 위치로 이동 예정")

            # 다음 단계에서 구현:
            # self.move_to_pose(pre_grasp_pose)

            # -------------------------------------------------
            # STEP 2: open gripper
            # -------------------------------------------------
            self.state = PickState.OPENING_GRIPPER
            self.get_logger().info("[2/6] 그리퍼 열기 예정")

            # 다음 단계에서 구현:
            # self.command_gripper(self.open_position)

            # -------------------------------------------------
            # STEP 3: grasp
            # -------------------------------------------------
            self.state = PickState.MOVING_TO_GRASP
            self.get_logger().info("[3/6] Grasp 위치로 이동 예정")

            # 다음 단계에서 구현:
            # self.move_to_pose(grasp_pose)

            # -------------------------------------------------
            # STEP 4: close gripper
            # -------------------------------------------------
            self.state = PickState.CLOSING_GRIPPER
            self.get_logger().info("[4/6] 그리퍼 닫기 예정")

            # 다음 단계에서 구현:
            # self.command_gripper(self.close_position)

            # -------------------------------------------------
            # STEP 5: attach collision object
            # -------------------------------------------------
            self.state = PickState.ATTACHING_OBJECT
            self.get_logger().info("[5/6] ArUco cube attach 예정")

            # 다음 단계에서 구현:
            # self.attach_aruco_cube()

            # -------------------------------------------------
            # STEP 6: lift
            # -------------------------------------------------
            self.state = PickState.LIFTING_OBJECT
            self.get_logger().info("[6/6] Cube 들어 올리기 예정")

            # 다음 단계에서 구현:
            # self.move_to_pose(lift_pose)

            self.state = PickState.DONE
            self.get_logger().info(
                "현재 버전은 목표 자세 계산까지 완료했습니다. "
                "다음 단계에서 MoveIt 실행 함수를 연결하세요."
            )

        except Exception as error:
            self.state = PickState.ERROR
            self.get_logger().error(
                f"Pick sequence 실패: {error!r}"
            )

    # ---------------------------------------------------------
    # Pose generation
    # ---------------------------------------------------------
    def create_target_pose(
        self,
        marker_transform: TransformStamped,
        offset_z: float,
    ) -> PoseStamped:
        """Create a target pose above the marker in the planning frame."""

        marker_translation = marker_transform.transform.translation

        target = PoseStamped()
        target.header.frame_id = self.planning_frame
        target.header.stamp = self.get_clock().now().to_msg()

        target.pose.position.x = float(marker_translation.x)
        target.pose.position.y = float(marker_translation.y)
        target.pose.position.z = (
            float(marker_translation.z)
            + float(offset_z)
        )

        # 초기 테스트용 고정 자세.
        # OpenManipulator end-effector 축에 맞게 이후 조절해야 함.
        target.pose.orientation.x = 0.0
        target.pose.orientation.y = 1.0
        target.pose.orientation.z = 0.0
        target.pose.orientation.w = 0.0

        return target

    @staticmethod
    def pose_to_text(pose: PoseStamped) -> str:
        """Return a compact pose string for logging."""

        position = pose.pose.position
        orientation = pose.pose.orientation

        return (
            f"p=({position.x:.3f}, "
            f"{position.y:.3f}, "
            f"{position.z:.3f}), "
            f"q=({orientation.x:.3f}, "
            f"{orientation.y:.3f}, "
            f"{orientation.z:.3f}, "
            f"{orientation.w:.3f})"
        )


def main(args=None) -> None:
    rclpy.init(args=args)

    node = ArucoPickNode()
    executor = MultiThreadedExecutor(num_threads=3)
    executor.add_node(node)

    try:
        executor.spin()

    except KeyboardInterrupt:
        pass

    finally:
        executor.shutdown()
        node.destroy_node()

        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()