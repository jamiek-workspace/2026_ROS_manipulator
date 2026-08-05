#!/usr/bin/env python3
"""ROS 2 ArUco detection, pose visualization, and dynamic TF broadcaster."""

from __future__ import annotations

import math
from typing import Optional

import cv2
import numpy as np
import rclpy
from cv_bridge import CvBridge
from geometry_msgs.msg import TransformStamped
from rclpy.node import Node
from sensor_msgs.msg import CameraInfo, Image
from tf2_ros import TransformBroadcaster


class ArucoTfNode(Node):
    """Detect ArUco markers from a camera image and publish marker TF frames."""

    DICTIONARIES = {
        "DICT_4X4_50": cv2.aruco.DICT_4X4_50,
        "DICT_4X4_100": cv2.aruco.DICT_4X4_100,
        "DICT_5X5_50": cv2.aruco.DICT_5X5_50,
        "DICT_6X6_50": cv2.aruco.DICT_6X6_50,
        "DICT_7X7_50": cv2.aruco.DICT_7X7_50,
        "DICT_ARUCO_ORIGINAL": cv2.aruco.DICT_ARUCO_ORIGINAL,
    }

    def __init__(self) -> None:
        super().__init__("aruco_tf_node")

        # ---------------------------------------------------------
        # ROS parameters
        # ---------------------------------------------------------
        self.declare_parameter("image_topic", "/vehicle_1/camera/image_raw")
        self.declare_parameter("camera_info_topic", "/vehicle_1/camera/camera_info")
        self.declare_parameter("marker_size", 0.10)  # metres
        self.declare_parameter("dictionary", "DICT_4X4_50")
        self.declare_parameter("marker_frame_prefix", "aruco_marker_")
        self.declare_parameter("camera_frame_override", "")
        self.declare_parameter("show_image", True)

        image_topic = str(self.get_parameter("image_topic").value)
        camera_info_topic = str(self.get_parameter("camera_info_topic").value)
        dictionary_name = str(self.get_parameter("dictionary").value)

        if dictionary_name not in self.DICTIONARIES:
            valid = ", ".join(self.DICTIONARIES)
            raise ValueError(
                f"지원하지 않는 dictionary입니다: {dictionary_name}. 사용 가능: {valid}"
            )

        self.marker_size = float(self.get_parameter("marker_size").value)
        self.marker_frame_prefix = str(
            self.get_parameter("marker_frame_prefix").value
        )
        self.camera_frame_override = str(
            self.get_parameter("camera_frame_override").value
        )
        self.show_image = bool(self.get_parameter("show_image").value)

        if self.marker_size <= 0.0:
            raise ValueError("marker_size는 0보다 커야 합니다.")

        # OpenCV 4.6-compatible ArUco API
        dictionary_id = self.DICTIONARIES[dictionary_name]
        self.aruco_dictionary = cv2.aruco.getPredefinedDictionary(dictionary_id)
        self.detector_parameters = cv2.aruco.DetectorParameters_create()

        self.bridge = CvBridge()
        self.tf_broadcaster = TransformBroadcaster(self)

        self.camera_matrix: Optional[np.ndarray] = None
        self.dist_coeffs: Optional[np.ndarray] = None
        self.camera_info_received = False

        self.camera_info_subscription = self.create_subscription(
            CameraInfo,
            camera_info_topic,
            self.camera_info_callback,
            10,
        )
        self.image_subscription = self.create_subscription(
            Image,
            image_topic,
            self.image_callback,
            10,
        )

        if self.show_image:
            cv2.namedWindow("aruco_detection", cv2.WINDOW_NORMAL)
            cv2.resizeWindow("aruco_detection", 960, 540)

        self.get_logger().info(
            f"ArUco 노드 시작: image={image_topic}, "
            f"camera_info={camera_info_topic}, marker_size={self.marker_size:.3f} m, "
            f"dictionary={dictionary_name}"
        )

    def camera_info_callback(self, msg: CameraInfo) -> None:
        """Save camera intrinsic parameters from sensor_msgs/CameraInfo."""
        self.camera_matrix = np.asarray(msg.k, dtype=np.float64).reshape(3, 3)
        self.dist_coeffs = np.asarray(msg.d, dtype=np.float64)

        if not self.camera_info_received:
            self.camera_info_received = True
            self.get_logger().info(
                f"CameraInfo 수신 완료: frame_id='{msg.header.frame_id}'"
            )

    def image_callback(self, msg: Image) -> None:
        """Detect markers, estimate poses, draw axes, and publish TF."""
        try:
            image = self.bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
        except Exception as error:  # CvBridgeError differs by ROS distro
            self.get_logger().error(f"영상 변환 실패: {error}")
            return

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        corners, ids, rejected = cv2.aruco.detectMarkers(
            gray,
            self.aruco_dictionary,
            parameters=self.detector_parameters,
        )

        if ids is not None and len(ids) > 0:
            cv2.aruco.drawDetectedMarkers(image, corners, ids)

            if self.camera_matrix is None or self.dist_coeffs is None:
                cv2.putText(
                    image,
                    "Waiting for CameraInfo...",
                    (20, 35),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 0, 255),
                    2,
                )
                self.get_logger().warn(
                    "마커는 검출했지만 CameraInfo가 없어 자세를 계산할 수 없습니다.",
                    throttle_duration_sec=2.0,
                )
            else:
                rvecs, tvecs, _ = cv2.aruco.estimatePoseSingleMarkers(
                    corners,
                    self.marker_size,
                    self.camera_matrix,
                    self.dist_coeffs,
                )

                for marker_id, corner, rvec, tvec in zip(
                    ids.flatten(), corners, rvecs, tvecs
                ):
                    rvec = np.asarray(rvec, dtype=np.float64).reshape(3)
                    tvec = np.asarray(tvec, dtype=np.float64).reshape(3)

                    # Draw marker XYZ axes at the marker location.
                    cv2.drawFrameAxes(
                        image,
                        self.camera_matrix,
                        self.dist_coeffs,
                        rvec,
                        tvec,
                        self.marker_size * 0.6,
                        2,
                    )

                    center = np.mean(corner.reshape(4, 2), axis=0).astype(int)
                    quaternion = self.rvec_to_quaternion(rvec)

                    self.draw_pose_text(
                        image=image,
                        marker_id=int(marker_id),
                        center=(int(center[0]), int(center[1])),
                        tvec=tvec,
                        quaternion=quaternion,
                    )
                    self.publish_marker_tf(
                        stamp=msg.header.stamp,
                        parent_frame=(
                            self.camera_frame_override
                            if self.camera_frame_override
                            else msg.header.frame_id
                        ),
                        marker_id=int(marker_id),
                        tvec=tvec,
                        quaternion=quaternion,
                    )

        detected_count = 0 if ids is None else len(ids)
        cv2.putText(
            image,
            f"detected markers: {detected_count}",
            (20, image.shape[0] - 20),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 0),
            2,
        )

        if self.show_image:
            cv2.imshow("aruco_detection", image)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                self.get_logger().info("q 키 입력: 노드를 종료합니다.")
                rclpy.shutdown()

    def publish_marker_tf(
        self,
        stamp,
        parent_frame: str,
        marker_id: int,
        tvec: np.ndarray,
        quaternion: tuple[float, float, float, float],
    ) -> None:
        """Publish camera -> marker as a dynamic TF transform."""
        if not parent_frame:
            self.get_logger().warn(
                "Image header.frame_id가 비어 있어 TF를 발행하지 않습니다. "
                "camera_frame_override 파라미터를 지정하세요.",
                throttle_duration_sec=2.0,
            )
            return

        transform = TransformStamped()
        transform.header.stamp = stamp
        transform.header.frame_id = parent_frame
        transform.child_frame_id = f"{self.marker_frame_prefix}{marker_id}"

        # OpenCV tvec: marker origin expressed in the camera optical frame.
        transform.transform.translation.x = float(tvec[0])
        transform.transform.translation.y = float(tvec[1])
        transform.transform.translation.z = float(tvec[2])

        transform.transform.rotation.x = quaternion[0]
        transform.transform.rotation.y = quaternion[1]
        transform.transform.rotation.z = quaternion[2]
        transform.transform.rotation.w = quaternion[3]

        self.tf_broadcaster.sendTransform(transform)

    @staticmethod
    def rvec_to_quaternion(
        rvec: np.ndarray,
    ) -> tuple[float, float, float, float]:
        """Convert an OpenCV Rodrigues rotation vector to quaternion xyzw."""
        rotation_matrix, _ = cv2.Rodrigues(rvec)
        m = rotation_matrix
        trace = float(np.trace(m))

        if trace > 0.0:
            s = math.sqrt(trace + 1.0) * 2.0
            qw = 0.25 * s
            qx = (m[2, 1] - m[1, 2]) / s
            qy = (m[0, 2] - m[2, 0]) / s
            qz = (m[1, 0] - m[0, 1]) / s
        elif m[0, 0] > m[1, 1] and m[0, 0] > m[2, 2]:
            s = math.sqrt(1.0 + m[0, 0] - m[1, 1] - m[2, 2]) * 2.0
            qw = (m[2, 1] - m[1, 2]) / s
            qx = 0.25 * s
            qy = (m[0, 1] + m[1, 0]) / s
            qz = (m[0, 2] + m[2, 0]) / s
        elif m[1, 1] > m[2, 2]:
            s = math.sqrt(1.0 + m[1, 1] - m[0, 0] - m[2, 2]) * 2.0
            qw = (m[0, 2] - m[2, 0]) / s
            qx = (m[0, 1] + m[1, 0]) / s
            qy = 0.25 * s
            qz = (m[1, 2] + m[2, 1]) / s
        else:
            s = math.sqrt(1.0 + m[2, 2] - m[0, 0] - m[1, 1]) * 2.0
            qw = (m[1, 0] - m[0, 1]) / s
            qx = (m[0, 2] + m[2, 0]) / s
            qy = (m[1, 2] + m[2, 1]) / s
            qz = 0.25 * s

        quaternion = np.asarray([qx, qy, qz, qw], dtype=np.float64)
        norm = float(np.linalg.norm(quaternion))
        if norm == 0.0:
            return 0.0, 0.0, 0.0, 1.0

        quaternion /= norm
        return tuple(float(value) for value in quaternion)

    @staticmethod
    def draw_pose_text(
        image: np.ndarray,
        marker_id: int,
        center: tuple[int, int],
        tvec: np.ndarray,
        quaternion: tuple[float, float, float, float],
    ) -> None:
        """Draw marker ID, translation, and quaternion near the marker."""
        x, y = center
        lines = [
            f"ID={marker_id}",
            f"t=({tvec[0]:.3f}, {tvec[1]:.3f}, {tvec[2]:.3f}) m",
            (
                f"q=({quaternion[0]:.2f}, {quaternion[1]:.2f}, "
                f"{quaternion[2]:.2f}, {quaternion[3]:.2f})"
            ),
        ]

        start_x = max(5, x + 10)
        start_y = max(25, y - 35)
        for index, text in enumerate(lines):
            cv2.putText(
                image,
                text,
                (start_x, start_y + index * 22),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.52,
                (0, 255, 0),
                2,
            )

    def destroy_node(self) -> bool:
        if self.show_image:
            cv2.destroyAllWindows()
        return super().destroy_node()


def main(args=None) -> None:
    rclpy.init(args=args)
    node = ArucoTfNode()

    try:
        # imshow/waitKey runs in the image callback on this main thread.
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()
