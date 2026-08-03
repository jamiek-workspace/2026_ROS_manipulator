# 카메라 이미지를 DDS에 publish하고 imshow로 화면에 표시
# 원을 특정 위치 10곳에 랜덤으로 이동시키는 코드를 작성하세요.
# 원이 이동하면 라인이 그려지는 효과도 추가하세요.
# 10곳을 모두 돌면 그려진 도형은 다 지우고 다시 처음부터 실행하게 하세요.

#!/usr/bin/env python3

import random

import cv2
import rclpy
from cv_bridge import CvBridge
from rclpy.node import Node
from sensor_msgs.msg import Image


class RandomCirclePublisher(Node):

    def __init__(self):
        super().__init__("random_circle_publisher")

        # DDS를 통해 Image 메시지를 발행할 Publisher
        self.publisher = self.create_publisher(
            Image,
            "/camera/random_circle",
            10,
        )

        self.bridge = CvBridge()

        # 카메라 열기
        self.cap = cv2.VideoCapture(0)

        if not self.cap.isOpened():
            self.get_logger().error("카메라를 열 수 없습니다.")
            raise RuntimeError("Failed to open camera")

        self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # 원이 화면 밖으로 나가지 않도록 여백 지정
        self.margin = 50

        # 원이 이동할 10개의 위치
        self.target_points = self.create_random_points()

        # 현재 몇 번째 위치인지 나타내는 인덱스
        self.current_index = 0

        # 현재까지 지나온 좌표
        self.visited_points = []

        # 원의 현재 위치
        self.current_point = self.target_points[0]

        # 카메라 이미지 발행 주기: 약 30 FPS
        self.frame_timer = self.create_timer(
            1.0 / 30.0,
            self.publish_frame,
        )

        # 원 이동 주기: 0.7초마다 다음 위치로 이동
        self.move_timer = self.create_timer(
            0.7,
            self.move_circle,
        )

        self.get_logger().info(
            "Random circle publisher node started."
        )

    def create_random_points(self):
        """화면 안에 원이 이동할 임의의 좌표 10개를 생성한다."""

        points = []

        while len(points) < 10:
            x = random.randint(
                self.margin,
                self.width - self.margin,
            )
            y = random.randint(
                self.margin,
                self.height - self.margin,
            )

            new_point = (x, y)

            # 너무 가까운 좌표가 연속해서 생성되지 않도록 검사
            if all(
                self.distance(new_point, point) > 70
                for point in points
            ):
                points.append(new_point)

        return points

    @staticmethod
    def distance(point1, point2):
        """두 좌표 사이의 거리를 계산한다."""

        x1, y1 = point1
        x2, y2 = point2

        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def move_circle(self):
        """원을 다음 목표 위치로 이동시킨다."""

        # 현재 위치를 지나온 좌표에 저장
        self.visited_points.append(self.current_point)

        self.current_index += 1

        # 10개의 위치를 모두 방문한 경우
        if self.current_index >= len(self.target_points):
            self.get_logger().info(
                "10개 위치 방문 완료. 경로를 초기화합니다."
            )

            # 새로운 임의 좌표 10개 생성
            self.target_points = self.create_random_points()

            # 이동 기록 초기화
            self.visited_points.clear()
            self.current_index = 0

        self.current_point = self.target_points[
            self.current_index
        ]

    def draw_path(self, frame):
        """지나온 위치를 선으로 연결한다."""

        draw_points = self.visited_points + [
            self.current_point
        ]

        for index in range(1, len(draw_points)):
            cv2.line(
                frame,
                draw_points[index - 1],
                draw_points[index],
                (255, 0, 255),  # 자홍색, BGR
                3,
                cv2.LINE_AA,
            )

    def draw_targets(self, frame):
        """10개의 목표 위치를 작은 점으로 표시한다."""

        for index, point in enumerate(self.target_points):
            cv2.circle(
                frame,
                point,
                5,
                (255, 255, 255),  # 흰색, BGR
                -1,
                cv2.LINE_AA,
            )

            cv2.putText(
                frame,
                str(index + 1),
                (point[0] + 8, point[1] - 8),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 255),
                1,
                cv2.LINE_AA,
            )

    def publish_frame(self):
        """카메라 프레임에 도형을 그리고 DDS에 발행한다."""

        ret, frame = self.cap.read()

        if not ret:
            self.get_logger().warning(
                "카메라 프레임을 읽지 못했습니다."
            )
            return

        # 목표 위치 표시
        self.draw_targets(frame)

        # 지나온 경로 표시
        self.draw_path(frame)

        # 현재 원 표시
        cv2.circle(
            frame,
            self.current_point,
            22,
            (0, 0, 255),  # 빨간색, BGR
            -1,
            cv2.LINE_AA,
        )

        cv2.circle(
            frame,
            self.current_point,
            28,
            (255, 255, 255),
            2,
            cv2.LINE_AA,
        )

        # 현재 진행 상태 표시
        cv2.putText(
            frame,
            f"Position: {self.current_index + 1}/10",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (255, 255, 255),
            2,
            cv2.LINE_AA,
        )

        # OpenCV 창에 출력
        cv2.imshow("Random Circle Camera", frame)

        # q를 누르면 ROS2 종료
        if cv2.waitKey(1) & 0xFF == ord("q"):
            rclpy.shutdown()
            return

        # OpenCV 이미지를 ROS2 Image 메시지로 변환
        msg = self.bridge.cv2_to_imgmsg(
            frame,
            encoding="bgr8",
        )

        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "camera_frame"

        # DDS 토픽에 발행
        self.publisher.publish(msg)

    def destroy_node(self):
        """노드 종료 시 카메라와 OpenCV 창을 정리한다."""

        if self.cap.isOpened():
            self.cap.release()

        cv2.destroyAllWindows()

        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)

    node = RandomCirclePublisher()

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