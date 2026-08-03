#!/usr/bin/env python3

# 카메라 이미지를 DDS에 publish하고 imshow로 화면에 표시
# 원을 임의의 위치 10곳으로 이동
# 원은 베지어 곡선을 따라 이동
# 이동 구간마다 선 색상 변경
# 10곳을 모두 방문하면 도형을 지우고 다시 시작
# 카메라가 없으면 검정 배경 사용

import random

import cv2
import numpy as np
import rclpy
from cv_bridge import CvBridge
from rclpy.node import Node
from sensor_msgs.msg import Image


class RandomCirclePublisher(Node):

    def __init__(self):
        super().__init__("random_circle_publisher")

        # DDS Image Publisher
        self.publisher = self.create_publisher(
            Image,
            "/camera/random_circle",
            10,
        )

        self.bridge = CvBridge()

        # 기본 배경 크기
        self.default_width = 640
        self.default_height = 480

        # 카메라 열기
        self.cap = cv2.VideoCapture(0)

        # 카메라 사용 여부
        self.camera_available = False

        if self.cap.isOpened():
            ret, test_frame = self.cap.read()

            if ret and test_frame is not None:
                self.camera_available = True
                self.height, self.width = test_frame.shape[:2]

                self.get_logger().info(
                    f"카메라를 사용합니다: "
                    f"{self.width} x {self.height}"
                )

            else:
                self.get_logger().warning(
                    "카메라는 열렸지만 프레임을 읽지 못했습니다. "
                    "검정 배경을 사용합니다."
                )

                self.cap.release()
                self.width = self.default_width
                self.height = self.default_height

        else:
            self.get_logger().warning(
                "카메라를 찾지 못했습니다. "
                "검정 배경을 사용합니다."
            )

            self.width = self.default_width
            self.height = self.default_height

        # 원이 화면 밖으로 나가지 않도록 지정하는 여백
        self.margin = 50

        # 한 사이클에서 방문할 위치 개수
        self.number_of_targets = 10

        # 원 이동 속도
        # 값이 작을수록 천천히 이동
        self.t_speed = 0.015

        # 원 크기
        self.circle_radius = 20

        # 선 두께
        self.line_thickness = 4

        # 구간마다 사용할 색상 목록
        # OpenCV는 BGR 순서
        self.line_colors = [
            (0, 0, 255),       # 빨강
            (0, 165, 255),     # 주황
            (0, 255, 255),     # 노랑
            (0, 255, 0),       # 초록
            (255, 255, 0),     # 청록
            (255, 0, 0),       # 파랑
            (255, 0, 255),     # 자홍
            (203, 192, 255),   # 분홍
            (255, 255, 255),   # 흰색
        ]

        # 완성된 도형을 잠시 보여주는 프레임 수
        # 30FPS 기준 30프레임은 약 1초
        self.reset_delay_frames = 30
        self.reset_counter = 0
        self.waiting_for_reset = False

        # 첫 번째 이동 사이클 생성
        self.reset_animation()

        # 약 30FPS로 이미지 처리 및 발행
        self.frame_timer = self.create_timer(
            1.0 / 30.0,
            self.publish_frame,
        )

        self.get_logger().info(
            "Random Bezier Circle Publisher가 시작되었습니다."
        )

    def create_background(self):
        """카메라 영상 또는 검정 배경을 반환한다."""

        if self.camera_available:
            ret, frame = self.cap.read()

            if ret and frame is not None:
                # 카메라 해상도가 실행 중 달라질 경우 크기 통일
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
                "이번 프레임은 검정 배경으로 대체합니다."
            )

        # 카메라가 없거나 프레임 읽기에 실패한 경우
        return np.zeros(
            (self.height, self.width, 3),
            dtype=np.uint8,
        )

    def create_random_points(self):
        """화면 안에서 서로 너무 가깝지 않은 좌표 10개를 생성한다."""

        points = []
        maximum_attempts = 2000
        attempts = 0

        while (
            len(points) < self.number_of_targets
            and attempts < maximum_attempts
        ):
            attempts += 1

            x = random.randint(
                self.margin,
                self.width - self.margin,
            )

            y = random.randint(
                self.margin,
                self.height - self.margin,
            )

            new_point = (x, y)

            # 기존 점과 최소 70픽셀 이상 떨어진 경우 추가
            if all(
                self.distance(new_point, point) >= 70
                for point in points
            ):
                points.append(new_point)

        # 해상도가 작거나 조건을 만족하기 어려울 때 보완
        while len(points) < self.number_of_targets:
            x = random.randint(
                self.margin,
                self.width - self.margin,
            )

            y = random.randint(
                self.margin,
                self.height - self.margin,
            )

            points.append((x, y))

        return points

    @staticmethod
    def distance(point1, point2):
        """두 좌표 사이의 거리를 반환한다."""

        x1, y1 = point1
        x2, y2 = point2

        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def create_control_point(self, start, end):
        """베지어 곡선의 제어점을 생성한다."""

        start_x, start_y = start
        end_x, end_y = end

        # 두 점의 중간 위치
        middle_x = (start_x + end_x) / 2.0
        middle_y = (start_y + end_y) / 2.0

        # 시작점에서 끝점으로 향하는 벡터
        dx = end_x - start_x
        dy = end_y - start_y

        distance = (dx ** 2 + dy ** 2) ** 0.5

        if distance == 0:
            return int(middle_x), int(middle_y)

        # 이동 방향과 수직인 단위 벡터
        perpendicular_x = -dy / distance
        perpendicular_y = dx / distance

        # 곡선이 좌우 중 어느 방향으로 휘어질지 결정
        direction = random.choice([-1, 1])

        # 두 점 사이 거리를 기준으로 곡률 결정
        minimum_strength = 40.0
        maximum_strength = min(160.0, distance * 0.7)

        if maximum_strength < minimum_strength:
            maximum_strength = minimum_strength

        curve_strength = random.uniform(
            minimum_strength,
            maximum_strength,
        )

        control_x = (
            middle_x
            + perpendicular_x * curve_strength * direction
        )

        control_y = (
            middle_y
            + perpendicular_y * curve_strength * direction
        )

        # 제어점이 화면 밖으로 나가지 않도록 제한
        control_x = max(
            self.margin,
            min(self.width - self.margin, control_x),
        )

        control_y = max(
            self.margin,
            min(self.height - self.margin, control_y),
        )

        return (
            int(round(control_x)),
            int(round(control_y)),
        )

    @staticmethod
    def calculate_bezier_point(start, control, end, t):
        """2차 베지어 곡선 위의 현재 좌표를 계산한다."""

        start_x, start_y = start
        control_x, control_y = control
        end_x, end_y = end

        one_minus_t = 1.0 - t

        x = (
            one_minus_t ** 2 * start_x
            + 2.0 * one_minus_t * t * control_x
            + t ** 2 * end_x
        )

        y = (
            one_minus_t ** 2 * start_y
            + 2.0 * one_minus_t * t * control_y
            + t ** 2 * end_y
        )

        return (
            int(round(x)),
            int(round(y)),
        )

    def select_new_line_color(self):
        """현재 구간에 사용할 색상을 선택한다."""

        available_colors = [
            color
            for color in self.line_colors
            if color != self.current_line_color
        ]

        if available_colors:
            return random.choice(available_colors)

        return random.choice(self.line_colors)

    def reset_animation(self):
        """모든 이동 경로를 지우고 새로운 사이클을 시작한다."""

        # 새로운 목표 위치 10개
        self.target_points = self.create_random_points()

        # 첫 번째 점에서 출발하여 두 번째 점으로 이동
        self.current_index = 1

        self.start_point = self.target_points[0]
        self.end_point = self.target_points[1]

        # 현재 베지어 곡선의 제어점
        self.control_point = self.create_control_point(
            self.start_point,
            self.end_point,
        )

        # 베지어 곡선의 진행도
        self.t = 0.0

        # 현재 원 위치
        self.current_point = self.start_point

        # 현재 이동 구간에서 지나온 점
        self.current_segment_points = [
            self.start_point
        ]

        # 완료된 선 구간
        # 각 원소는 {"points": [...], "color": (B, G, R)}
        self.completed_segments = []

        # 첫 번째 이동 구간의 선 색상
        self.current_line_color = random.choice(
            self.line_colors
        )

        self.waiting_for_reset = False
        self.reset_counter = 0

        self.get_logger().info(
            "새로운 목표 위치 10개를 생성했습니다."
        )

    def finish_current_segment(self):
        """현재 곡선 구간을 완료 목록에 저장한다."""

        if len(self.current_segment_points) >= 2:
            self.completed_segments.append(
                {
                    "points": self.current_segment_points.copy(),
                    "color": self.current_line_color,
                }
            )

    def move_circle(self):
        """원을 베지어 곡선을 따라 한 단계 이동시킨다."""

        # 10개 위치 방문 후에는 잠시 정지
        if self.waiting_for_reset:
            self.reset_counter += 1

            if self.reset_counter >= self.reset_delay_frames:
                self.reset_animation()

            return

        # 베지어 곡선 진행
        self.t += self.t_speed

        if self.t >= 1.0:
            self.t = 1.0

        # 현재 베지어 곡선상의 위치
        self.current_point = self.calculate_bezier_point(
            self.start_point,
            self.control_point,
            self.end_point,
            self.t,
        )

        # 같은 점을 반복 저장하지 않도록 검사
        if (
            not self.current_segment_points
            or self.current_segment_points[-1]
            != self.current_point
        ):
            self.current_segment_points.append(
                self.current_point
            )

        # 아직 도착하지 않았다면 다음 프레임에서 계속 이동
        if self.t < 1.0:
            return

        # 현재 목표점에 정확히 도착
        self.current_point = self.end_point

        if self.current_segment_points[-1] != self.end_point:
            self.current_segment_points.append(
                self.end_point
            )

        # 현재 색상의 곡선 구간 저장
        self.finish_current_segment()

        # 다음 목표점 번호
        self.current_index += 1

        # 마지막인 10번째 위치까지 방문한 경우
        if self.current_index >= len(self.target_points):
            self.get_logger().info(
                "10개 위치 방문 완료. "
                "잠시 후 경로를 초기화합니다."
            )

            self.waiting_for_reset = True
            self.reset_counter = 0
            return

        # 다음 구간 설정
        self.start_point = self.end_point
        self.end_point = self.target_points[
            self.current_index
        ]

        self.control_point = self.create_control_point(
            self.start_point,
            self.end_point,
        )

        # 다음 곡선은 처음부터 시작
        self.t = 0.0

        # 새로운 구간의 선 좌표 초기화
        self.current_segment_points = [
            self.start_point
        ]

        # 구간이 바뀔 때마다 다른 색상 선택
        self.current_line_color = (
            self.select_new_line_color()
        )

    @staticmethod
    def draw_polyline(frame, points, line_color, thickness):
        """좌표 목록을 차례대로 연결하여 곡선처럼 표시한다."""

        if len(points) < 2:
            return

        point_array = np.array(
            points,
            dtype=np.int32,
        ).reshape((-1, 1, 2))

        cv2.polylines(
            frame,
            [point_array],
            False,
            line_color,
            thickness,
            cv2.LINE_AA,
        )

    def draw_path(self, frame):
        """완료된 곡선과 현재 이동 중인 곡선을 그린다."""

        # 이미 완료된 구간
        for segment in self.completed_segments:
            self.draw_polyline(
                frame,
                segment["points"],
                segment["color"],
                self.line_thickness,
            )

        # 현재 이동 중인 구간
        if not self.waiting_for_reset:
            self.draw_polyline(
                frame,
                self.current_segment_points,
                self.current_line_color,
                self.line_thickness,
            )

    def draw_targets(self, frame):
        """10개의 목표 위치와 번호를 표시한다."""

        for index, point in enumerate(self.target_points):
            # 아직 방문하지 않은 목표점
            if index >= self.current_index:
                point_color = (180, 180, 180)

            # 방문했거나 현재 이동이 완료된 목표점
            else:
                point_color = (255, 255, 255)

            cv2.circle(
                frame,
                point,
                5,
                point_color,
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

    def draw_information(self, frame):
        """카메라 사용 상태와 이동 정보를 표시한다."""

        background_text = (
            "CAMERA"
            if self.camera_available
            else "BLACK BACKGROUND"
        )

        if self.waiting_for_reset:
            position_text = "Completed: 10/10"
        else:
            position_text = (
                f"Moving to: "
                f"{self.current_index + 1}/"
                f"{self.number_of_targets}"
            )

        cv2.putText(
            frame,
            position_text,
            (20, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2,
            cv2.LINE_AA,
        )

        cv2.putText(
            frame,
            f"Background: {background_text}",
            (20, 65),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (200, 200, 200),
            1,
            cv2.LINE_AA,
        )

        cv2.putText(
            frame,
            "Press Q to quit",
            (20, self.height - 20),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.55,
            (200, 200, 200),
            1,
            cv2.LINE_AA,
        )

    def publish_frame(self):
        """이미지를 생성하고 DDS 발행 및 imshow를 수행한다."""

        # 카메라 영상 또는 검정 배경
        frame = self.create_background()

        # 프레임마다 원을 조금씩 이동
        self.move_circle()

        # 목표점과 경로 그리기
        self.draw_targets(frame)
        self.draw_path(frame)

        # 현재 움직이는 원
        cv2.circle(
            frame,
            self.current_point,
            self.circle_radius,
            (0, 0, 255),
            -1,
            cv2.LINE_AA,
        )

        # 원의 외곽선
        cv2.circle(
            frame,
            self.current_point,
            self.circle_radius + 6,
            (255, 255, 255),
            2,
            cv2.LINE_AA,
        )

        self.draw_information(frame)

        # OpenCV 창에 표시
        cv2.imshow(
            "Random Bezier Circle",
            frame,
        )

        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            rclpy.shutdown()
            return

        # OpenCV 이미지를 ROS2 Image 메시지로 변환
        message = self.bridge.cv2_to_imgmsg(
            frame,
            encoding="bgr8",
        )

        message.header.stamp = (
            self.get_clock().now().to_msg()
        )

        message.header.frame_id = "camera_frame"

        # DDS 토픽으로 발행
        self.publisher.publish(message)

    def destroy_node(self):
        """노드가 종료될 때 자원을 해제한다."""

        if self.cap is not None and self.cap.isOpened():
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