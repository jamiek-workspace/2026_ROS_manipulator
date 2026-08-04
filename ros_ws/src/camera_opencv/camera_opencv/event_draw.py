# a09_event_draw 기능을 ros2에서 카메라 영상을 배경으로 작동시키기

import cv2
import numpy as np
import rclpy

from cv_bridge import CvBridge
from rclpy.node import Node
from sensor_msgs.msg import Image


class CameraEventDraw(Node):

    def __init__(self):
        super().__init__("camera_event_draw")

        # DDS Publisher
        self.publisher = self.create_publisher(
            Image,
            "/camera/event_draw",
            10,
        )

        self.bridge = CvBridge()

        # OpenCV 창 이름
        self.window_name = "Camera Event Draw"

        # 카메라가 없을 때 사용할 기본 크기
        self.default_width = 640
        self.default_height = 480

        # 웹캠 열기
        # 현재 C920이 /dev/video1이라면 1로 바꾸면 됨
        self.camera_index = 0
        self.cap = cv2.VideoCapture(self.camera_index)

        self.camera_available = False

        if self.cap.isOpened():
            ret, test_frame = self.cap.read()

            if ret and test_frame is not None:
                self.camera_available = True

                self.height, self.width = test_frame.shape[:2]

                self.get_logger().info(
                    f"카메라 사용: /dev/video{self.camera_index}, "
                    f"{self.width} x {self.height}"
                )

            else:
                self.get_logger().warning(
                    "카메라는 열렸지만 영상을 읽지 못했습니다. "
                    "검정 배경을 사용합니다."
                )

                self.cap.release()

                self.width = self.default_width
                self.height = self.default_height

        else:
            self.get_logger().warning(
                f"/dev/video{self.camera_index} 카메라를 열 수 없습니다. "
                "검정 배경을 사용합니다."
            )

            self.width = self.default_width
            self.height = self.default_height

        # 그림만 저장하는 레이어
        self.drawing_layer = np.zeros(
            (self.height, self.width, 3),
            dtype=np.uint8,
        )

        # drawing_layer에서 실제로 그려진 부분을 표시하는 마스크
        self.drawing_mask = np.zeros(
            (self.height, self.width),
            dtype=np.uint8,
        )

        # 이전 마우스 위치
        self.old_x = None
        self.old_y = None

        # 현재 드래그 상태
        self.is_drawing = False

        # 선 두께
        self.line_thickness = 3

        # 사용할 색상 목록: BGR
        self.colors = [
            (0, 0, 255),       # 빨강
            (0, 64, 255),      # 빨강-주황
            (0, 127, 255),     # 주황
            (0, 191, 255),     # 주황-노랑
            (0, 255, 255),     # 노랑
            (0, 255, 128),     # 연두
            (0, 255, 0),       # 초록
            (128, 255, 0),     # 초록-청록
            (255, 255, 0),     # 청록
            (255, 128, 0),     # 하늘색
            (255, 0, 0),       # 파랑
            (255, 0, 128),     # 보라
            (211, 0, 148),     # 자홍
            (203, 96, 200),    # 연보라
            (203, 192, 255),   # 분홍
            (255, 255, 255),   # 흰색
        ]

        self.color_index = 0

        # OpenCV 창 생성
        cv2.namedWindow(
            self.window_name,
            cv2.WINDOW_AUTOSIZE,
        )

        # 마우스 콜백 설정
        cv2.setMouseCallback(
            self.window_name,
            self.on_mouse,
        )

        # 약 30FPS로 실행
        self.timer = self.create_timer(
            1.0 / 30.0,
            self.process_frame,
        )

        self.get_logger().info(
            "Camera Event Draw 노드가 시작되었습니다."
        )

    def create_background(self):
        """카메라 영상 또는 검정 배경을 생성한다."""

        if self.camera_available:
            ret, frame = self.cap.read()

            if ret and frame is not None:
                # 영상 크기를 최초 크기로 통일
                if (
                    frame.shape[1] != self.width
                    or frame.shape[0] != self.height
                ):
                    frame = cv2.resize(
                        frame,
                        (self.width, self.height),
                    )

                return frame

            self.get_logger().warning(
                "카메라 프레임 읽기에 실패했습니다. "
                "검정 배경으로 대체합니다."
            )

        return np.zeros(
            (self.height, self.width, 3),
            dtype=np.uint8,
        )

    def on_mouse(self, event, x, y, flags, param):
        """마우스로 선을 그리는 콜백 함수."""

        # 왼쪽 버튼을 처음 누른 경우
        if event == cv2.EVENT_LBUTTONDOWN:
            self.is_drawing = True

            self.old_x = x
            self.old_y = y

            current_color = self.colors[
                self.color_index
            ]

            cv2.circle(
                self.drawing_layer,
                (x, y),
                self.line_thickness,
                current_color,
                -1,
                cv2.LINE_AA,
            )

            cv2.circle(
                self.drawing_mask,
                (x, y),
                self.line_thickness,
                255,
                -1,
                cv2.LINE_AA,
            )

        # 왼쪽 버튼을 누른 채 마우스를 움직이는 경우
        elif (
            event == cv2.EVENT_MOUSEMOVE
            and self.is_drawing
            and self.old_x is not None
            and self.old_y is not None
        ):
            current_color = self.colors[
                self.color_index
            ]

            cv2.line(
                self.drawing_layer,
                (self.old_x, self.old_y),
                (x, y),
                current_color,
                self.line_thickness,
                cv2.LINE_AA,
            )

            # 마스크에도 동일한 위치에 흰색 선 그리기
            cv2.line(
                self.drawing_mask,
                (self.old_x, self.old_y),
                (x, y),
                255,
                self.line_thickness,
                cv2.LINE_AA,
            )

            self.old_x = x
            self.old_y = y

        # 왼쪽 버튼을 놓은 경우
        elif event == cv2.EVENT_LBUTTONUP:
            self.is_drawing = False

            self.old_x = None
            self.old_y = None

    def combine_images(self, background):
        """카메라 배경과 그림 레이어를 합성한다."""

        result = background.copy()

        # drawing_mask가 0이 아닌 부분에만 그림 복사
        mask = self.drawing_mask > 0

        result[mask] = self.drawing_layer[mask]

        return result

    def clear_drawing(self):
        """그려진 선을 모두 지운다."""

        self.drawing_layer.fill(0)
        self.drawing_mask.fill(0)

        self.get_logger().info(
            "그림을 모두 지웠습니다."
        )

    def change_color(self):
        """다음 선 색상으로 변경한다."""

        self.color_index += 1

        if self.color_index >= len(self.colors):
            self.color_index = 0

        self.get_logger().info(
            f"선 색상 번호: {self.color_index}"
        )

    def draw_information(self, frame):
        """현재 상태를 화면에 표시한다."""

        background_name = (
            "CAMERA"
            if self.camera_available
            else "BLACK BACKGROUND"
        )

        cv2.putText(
            frame,
            f"Background: {background_name}",
            (15, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.65,
            (255, 255, 255),
            2,
            cv2.LINE_AA,
        )

        cv2.putText(
            frame,
            "SPACE: color | C: clear | Q: quit",
            (15, 60),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.55,
            (255, 255, 255),
            1,
            cv2.LINE_AA,
        )

        # 현재 색상 미리보기
        cv2.circle(
            frame,
            (self.width - 30, 30),
            12,
            self.colors[self.color_index],
            -1,
            cv2.LINE_AA,
        )

        cv2.circle(
            frame,
            (self.width - 30, 30),
            14,
            (255, 255, 255),
            1,
            cv2.LINE_AA,
        )

    def process_frame(self):
        """배경 생성, 합성, 화면 표시, DDS 발행을 수행한다."""

        # 웹캠 또는 검정 배경
        background = self.create_background()

        # 카메라 영상과 그림 합성
        result_frame = self.combine_images(
            background
        )

        self.draw_information(result_frame)

        # 화면 출력
        cv2.imshow(
            self.window_name,
            result_frame,
        )

        # OpenCV 키 이벤트 처리
        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            self.get_logger().info(
                "Q 입력으로 노드를 종료합니다."
            )

            rclpy.shutdown()
            return

        if key == ord(" "):
            self.change_color()

        elif key == ord("c"):
            self.clear_drawing()

        # OpenCV 이미지를 ROS2 Image 메시지로 변환
        try:
            message = self.bridge.cv2_to_imgmsg(
                result_frame,
                encoding="bgr8",
            )

            message.header.stamp = (
                self.get_clock().now().to_msg()
            )

            message.header.frame_id = (
                "camera_frame"
            )

            # DDS 발행
            self.publisher.publish(message)

        except Exception as error:
            self.get_logger().error(
                f"이미지 메시지 변환 또는 발행 실패: {error}"
            )

    def destroy_node(self):
        """카메라와 OpenCV 창을 정리한다."""

        if (
            self.cap is not None
            and self.cap.isOpened()
        ):
            self.cap.release()

        cv2.destroyAllWindows()

        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)

    node = CameraEventDraw()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        pass

    finally:
        node.destroy_node()

        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()