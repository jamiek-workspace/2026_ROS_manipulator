import math

import cv2
import numpy as np
import rclpy
from cv_bridge import CvBridge
from geometry_msgs.msg import TransformStamped
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import CameraInfo, Image
from tf2_ros import StaticTransformBroadcaster, TransformBroadcaster


def rotation_matrix_to_quaternion(rotation_matrix: np.ndarray):
    """
    3x3 회전 행렬을 quaternion (x, y, z, w)으로 변환한다.
    """
    matrix = np.asarray(
        rotation_matrix,
        dtype=np.float64,
    ).reshape(3, 3)

    trace = float(np.trace(matrix))

    if trace > 0.0:
        s = np.sqrt(trace + 1.0) * 2.0

        qw = 0.25 * s
        qx = (matrix[2, 1] - matrix[1, 2]) / s
        qy = (matrix[0, 2] - matrix[2, 0]) / s
        qz = (matrix[1, 0] - matrix[0, 1]) / s

    elif matrix[0, 0] > matrix[1, 1] and matrix[0, 0] > matrix[2, 2]:
        s = np.sqrt(1.0 + matrix[0, 0] - matrix[1, 1] - matrix[2, 2]) * 2.0

        qw = (matrix[2, 1] - matrix[1, 2]) / s
        qx = 0.25 * s
        qy = (matrix[0, 1] + matrix[1, 0]) / s
        qz = (matrix[0, 2] + matrix[2, 0]) / s

    elif matrix[1, 1] > matrix[2, 2]:
        s = np.sqrt(1.0 + matrix[1, 1] - matrix[0, 0] - matrix[2, 2]) * 2.0

        qw = (matrix[0, 2] - matrix[2, 0]) / s
        qx = (matrix[0, 1] + matrix[1, 0]) / s
        qy = 0.25 * s
        qz = (matrix[1, 2] + matrix[2, 1]) / s

    else:
        s = np.sqrt(1.0 + matrix[2, 2] - matrix[0, 0] - matrix[1, 1]) * 2.0

        qw = (matrix[1, 0] - matrix[0, 1]) / s
        qx = (matrix[0, 2] + matrix[2, 0]) / s
        qy = (matrix[1, 2] + matrix[2, 1]) / s
        qz = 0.25 * s

    quaternion = np.array(
        [qx, qy, qz, qw],
        dtype=np.float64,
    )

    norm = np.linalg.norm(quaternion)

    if norm > 0.0:
        quaternion /= norm

    return quaternion


def quaternion_from_rpy(
    roll: float,
    pitch: float,
    yaw: float,
):
    """
    Roll, pitch, yaw를 quaternion (x, y, z, w)으로 변환한다.
    """
    cr = math.cos(roll * 0.5)
    sr = math.sin(roll * 0.5)
    cp = math.cos(pitch * 0.5)
    sp = math.sin(pitch * 0.5)
    cy = math.cos(yaw * 0.5)
    sy = math.sin(yaw * 0.5)

    qx = sr * cp * cy - cr * sp * sy
    qy = cr * sp * cy + sr * cp * sy
    qz = cr * cp * sy - sr * sp * cy
    qw = cr * cp * cy + sr * sp * sy

    return np.array(
        [qx, qy, qz, qw],
        dtype=np.float64,
    )


class ArucoTfPublisher(Node):
    def __init__(self):
        super().__init__("aruco_tf_publisher")

        self.bridge = CvBridge()

        # 움직이는 ArUco 마커 TF
        self.tf_broadcaster = TransformBroadcaster(self)

        # camera_link -> camera_link_optical 고정 TF
        self.static_tf_broadcaster = StaticTransformBroadcaster(self)

        self.frame_count = 0
        self.camera_info_received = False

        self.camera_matrix = None
        self.dist_coeffs = None

        self.camera_link_frame = "/camera_link"

        # OpenCV 좌표계가 사용하는 optical frame
        self.camera_optical_frame = "/camera_optical"

        self.marker_length = 0.04
        self.axis_length = 0.03

        self.image_topic = "/gripper_camera/image_raw"

        self.camera_info_topic = "/gripper_camera/camera_info"

        self.dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)

        if hasattr(
            cv2.aruco,
            "DetectorParameters_create",
        ):
            self.detector_parameters = cv2.aruco.DetectorParameters_create()  # type: ignore
        else:
            self.detector_parameters = cv2.aruco.DetectorParameters()

        self.camera_info_subscription = self.create_subscription(
            CameraInfo,
            self.camera_info_topic,
            self.camera_info_callback,
            qos_profile_sensor_data,
        )

        self.image_subscription = self.create_subscription(
            Image,
            self.image_topic,
            self.image_callback,
            qos_profile_sensor_data,
        )

        # camera_link -> camera_optical_frame 고정 변환 발행
        self.publish_camera_optical_tf()

        self.get_logger().info("ArUco TF publisher 시작")
        self.get_logger().info(f"Image topic: {self.image_topic}")
        self.get_logger().info(f"CameraInfo topic: {self.camera_info_topic}")
        self.get_logger().info(f"Camera link frame: {self.camera_link_frame}")
        self.get_logger().info(f"Camera optical frame: {self.camera_optical_frame}")
        self.get_logger().info(f"Marker length: {self.marker_length:.3f} m")
        self.get_logger().info(f"OpenCV version: {cv2.__version__}")

    def publish_camera_optical_tf(self):
        """
        ROS camera_link 좌표계를 OpenCV optical 좌표계로 변환한다.

        camera_link:
            X: 전방
            Y: 왼쪽
            Z: 위쪽

        camera optical:
            X: 오른쪽
            Y: 아래쪽
            Z: 전방

        표준 optical 변환:
            roll  = -90도
            pitch = 0도
            yaw   = -90도
        """
        transform = TransformStamped()

        transform.header.stamp = self.get_clock().now().to_msg()
        transform.header.frame_id = self.camera_link_frame
        transform.child_frame_id = self.camera_optical_frame

        # optical frame 원점이 camera_link 원점과 같다고 가정
        transform.transform.translation.x = 0.0
        transform.transform.translation.y = 0.0
        transform.transform.translation.z = 0.0

        quaternion = quaternion_from_rpy(
            roll=-math.pi / 2.0,
            pitch=0.0,
            yaw=-math.pi / 2.0,
        )

        transform.transform.rotation.x = float(quaternion[0])
        transform.transform.rotation.y = float(quaternion[1])
        transform.transform.rotation.z = float(quaternion[2])
        transform.transform.rotation.w = float(quaternion[3])

        self.static_tf_broadcaster.sendTransform(transform)

        self.get_logger().info(
            "카메라 optical 고정 TF 발행 완료: "
            f"{self.camera_link_frame} -> "
            f"{self.camera_optical_frame}"
        )

    def camera_info_callback(
        self,
        msg: CameraInfo,
    ):
        camera_matrix = np.asarray(
            msg.k,
            dtype=np.float64,
        ).reshape(3, 3)

        if camera_matrix[0, 0] <= 0.0 or camera_matrix[1, 1] <= 0.0:
            self.get_logger().error("CameraInfo의 카메라 행렬이 유효하지 않습니다.")
            return

        self.camera_matrix = np.ascontiguousarray(
            camera_matrix,
            dtype=np.float64,
        )

        if len(msg.d) > 0:
            distortion = np.asarray(
                msg.d,
                dtype=np.float64,
            ).reshape(-1, 1)
        else:
            distortion = np.zeros(
                (5, 1),
                dtype=np.float64,
            )

        self.dist_coeffs = np.ascontiguousarray(
            distortion,
            dtype=np.float64,
        )

        if not self.camera_info_received:
            self.camera_info_received = True

            self.get_logger().info("CameraInfo 수신 완료")
            self.get_logger().info(f"CameraInfo frame_id: {msg.header.frame_id}")
            self.get_logger().info(f"TF optical frame: {self.camera_optical_frame}")
            self.get_logger().info(f"Image size: {msg.width}x{msg.height}")
            self.get_logger().info(f"Distortion model: {msg.distortion_model}")
            self.get_logger().info(f"Camera matrix:\n{self.camera_matrix}")
            self.get_logger().info(f"Distortion coefficients:\n{self.dist_coeffs.flatten()}")

    def publish_marker_tf(
        self,
        marker_id: int,
        rvec: np.ndarray,
        tvec: np.ndarray,
        stamp,
    ):
        """
        OpenCV가 계산한 ArUco pose를 optical frame 기준으로 발행한다.

        OpenCV와 ROS optical frame의 축 방향은 동일하다.

        OpenCV / ROS optical:
            X: 영상 오른쪽
            Y: 영상 아래쪽
            Z: 카메라 전방
        """
        rvec = np.ascontiguousarray(
            rvec,
            dtype=np.float64,
        ).reshape(3, 1)

        tvec = np.ascontiguousarray(
            tvec,
            dtype=np.float64,
        ).reshape(3)

        rotation_matrix, _ = cv2.Rodrigues(rvec)
        quaternion = rotation_matrix_to_quaternion(rotation_matrix)
        transform = TransformStamped()
        transform.header.stamp = stamp

        # 중요:
        # OpenCV 결과는 일반 camera_link가 아니라
        # optical frame을 부모로 사용해야 한다.
        transform.header.frame_id = self.camera_optical_frame
        transform.child_frame_id = f"aruco_marker_{marker_id}"

        # optical frame 기준:
        # tvec[0] = 오른쪽
        # tvec[1] = 아래쪽
        # tvec[2] = 전방
        transform.transform.translation.x = float(tvec[0])
        transform.transform.translation.y = float(tvec[1])
        transform.transform.translation.z = float(tvec[2])

        transform.transform.rotation.x = float(quaternion[0])
        transform.transform.rotation.y = float(quaternion[1])
        transform.transform.rotation.z = float(quaternion[2])
        transform.transform.rotation.w = float(quaternion[3])

        self.tf_broadcaster.sendTransform(transform)

    def image_callback(
        self,
        msg: Image,
    ):
        self.frame_count += 1
        if self.frame_count % 30 == 1:
            self.get_logger().info(
                f"이미지 콜백 진입: {msg.width}x{msg.height}, encoding={msg.encoding}"
            )
        try:
            frame = self.bridge.imgmsg_to_cv2(
                msg,
                desired_encoding="bgr8",
            )

        except Exception as error:
            self.get_logger().error(f"이미지 변환 실패: {error}")
            return

        frame = np.ascontiguousarray(
            frame,
            dtype=np.uint8,
        )

        if not self.camera_info_received:
            cv2.putText(
                frame,
                "Waiting for CameraInfo",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 255),
                2,
                cv2.LINE_AA,
            )

            cv2.imshow(
                "ArUco Detection",
                frame,
            )
            cv2.waitKey(1)
            return

        gray = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY,
        )

        gray = np.ascontiguousarray(
            gray,
            dtype=np.uint8,
        )

        corners, ids, rejected = cv2.aruco.detectMarkers(
            gray,
            self.dictionary,
            parameters=self.detector_parameters,
        )

        if ids is not None and len(ids) > 0:
            cv2.aruco.drawDetectedMarkers(
                frame,
                corners,
                ids,
            )

            rvecs, tvecs, _ = cv2.aruco.estimatePoseSingleMarkers(
                corners,
                float(self.marker_length),
                self.camera_matrix,
                self.dist_coeffs,
            )

            for index, marker_id_value in enumerate(ids.flatten()):
                marker_id = int(marker_id_value)

                rvec = np.ascontiguousarray(
                    rvecs[index],
                    dtype=np.float64,
                ).reshape(3, 1)

                tvec = np.ascontiguousarray(
                    tvecs[index],
                    dtype=np.float64,
                ).reshape(3, 1)

                # 영상 위 좌표축:
                # X 빨강, Y 초록, Z 파랑
                cv2.drawFrameAxes(
                    frame,
                    self.camera_matrix,
                    self.dist_coeffs,
                    rvec,
                    tvec,
                    float(self.axis_length),
                    2,
                )

                self.publish_marker_tf(
                    marker_id=marker_id,
                    rvec=rvec,
                    tvec=tvec,
                    stamp=msg.header.stamp,
                )

                marker_corners = np.asarray(
                    corners[index],
                    dtype=np.float32,
                ).reshape(4, 2)

                center_x = int(np.mean(marker_corners[:, 0]))
                center_y = int(np.mean(marker_corners[:, 1]))

                position = tvec.reshape(3)

                cv2.circle(
                    frame,
                    (center_x, center_y),
                    4,
                    (0, 255, 255),
                    -1,
                )

                cv2.putText(
                    frame,
                    f"ID: {marker_id}",
                    (
                        center_x - 40,
                        center_y - 30,
                    ),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 255),
                    2,
                    cv2.LINE_AA,
                )

                cv2.putText(
                    frame,
                    (f"optical x:{position[0]:.3f} y:{position[1]:.3f} z:{position[2]:.3f}"),
                    (
                        center_x - 140,
                        center_y + 30,
                    ),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.45,
                    (255, 255, 0),
                    1,
                    cv2.LINE_AA,
                )

                if self.frame_count % 30 == 1:
                    self.get_logger().info(
                        f"ArUco ID={marker_id}, "
                        f"optical tvec=("
                        f"{position[0]:.3f}, "
                        f"{position[1]:.3f}, "
                        f"{position[2]:.3f})"
                    )

        else:
            cv2.putText(
                frame,
                "No ArUco marker",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 255),
                2,
                cv2.LINE_AA,
            )

        cv2.imshow(
            "ArUco Detection",
            frame,
        )

        cv2.waitKey(1)

    def destroy_node(self):
        cv2.destroyAllWindows()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = ArucoTfPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        cv2.destroyAllWindows()
        node.destroy_node()
        if rclpy.ok():
            rclpy.try_shutdown()


if __name__ == "__main__":
    main()