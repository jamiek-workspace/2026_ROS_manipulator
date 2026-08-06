# orb keypoints와 descriptor를 사용해서 임의의 물체를 검출한다.
# 1 keypoints -> 사진 찍어서 orb로 얻기
# 2 keypoints -> 카메라 영상을 사용
# a34번 예제 응용, camera_pub을 사용해서 AI를 활용한 코드 작성

#!/usr/bin/env python3

from pathlib import Path

import cv2
import numpy as np
import rclpy
from cv_bridge import CvBridge
from rclpy.node import Node
from sensor_msgs.msg import Image


class MatchORB(Node):
    def __init__(self) -> None:
        super().__init__("match_orb")

        # camera_pub에서 발행하는 카메라 토픽을 구독한다.
        self.subscription = self.create_subscription(
            Image,
            "/camera/image_raw",
            self.image_callback,
            10,
        )

        self.bridge = CvBridge()

        # ORB 특징점 검출기
        self.orb = cv2.ORB_create(
            nfeatures=1500,
            scaleFactor=1.2,
            nlevels=8,
        )

        # ORB descriptor는 이진 descriptor이므로 NORM_HAMMING 사용
        self.matcher = cv2.BFMatcher(cv2.NORM_HAMMING)

        # 기준 이미지 관련 변수
        self.reference_image: np.ndarray | None = None
        self.reference_gray: np.ndarray | None = None
        self.reference_keypoints = None
        self.reference_descriptors: np.ndarray | None = None

        # 최근 카메라 프레임
        self.current_frame: np.ndarray | None = None

        # 매칭 관련 설정값
        self.ratio_threshold = 0.75
        self.minimum_matches = 10

        # 기준 이미지 저장 경로
        self.reference_path = (
            Path(__file__).resolve().parent / "data" / "orb_reference.jpg"
        )
        self.reference_path.parent.mkdir(parents=True, exist_ok=True)

        self.get_logger().info("ORB object matching node started.")
        self.get_logger().info("Press 'c' to capture a reference object.")
        self.get_logger().info("Press 'r' to reset the reference image.")
        self.get_logger().info("Press 'q' to quit.")

    def image_callback(self, msg: Image) -> None:
        try:
            frame = self.bridge.imgmsg_to_cv2(
                msg,
                desired_encoding="bgr8",
            )
        except Exception as error:
            self.get_logger().error(f"Image conversion failed: {error}")
            return

        self.current_frame = frame.copy()
        result_frame = frame.copy()

        if self.reference_descriptors is None:
            cv2.putText(
                result_frame,
                "Press C to capture reference object",
                (20, 35),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 255),
                2,
            )
        else:
            result_frame = self.detect_object(frame)

        cv2.imshow("ORB Object Detection", result_frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord("c"):
            self.capture_reference()

        elif key == ord("r"):
            self.reset_reference()

        elif key == ord("q"):
            self.get_logger().info("Closing match_orb node.")
            rclpy.shutdown()

    def capture_reference(self) -> None:
        """현재 카메라 화면을 기준 이미지로 지정한다."""

        if self.current_frame is None:
            self.get_logger().warning("No camera frame received yet.")
            return

        # 현재는 카메라 전체 화면을 기준 이미지로 사용한다.
        # 물체만 잘 보이도록 화면 가까이에 놓고 c 키를 누른다.
        self.reference_image = self.current_frame.copy()

        self.reference_gray = cv2.cvtColor(
            self.reference_image,
            cv2.COLOR_BGR2GRAY,
        )

        (
            self.reference_keypoints,
            self.reference_descriptors,
        ) = self.orb.detectAndCompute(
            self.reference_gray,
            None,
        )

        if (
            self.reference_descriptors is None
            or self.reference_keypoints is None
            or len(self.reference_keypoints) < self.minimum_matches
        ):
            self.get_logger().warning(
                "Not enough keypoints were detected. "
                "Try capturing an object with more texture."
            )

            self.reference_image = None
            self.reference_gray = None
            self.reference_keypoints = None
            self.reference_descriptors = None
            return

        cv2.imwrite(
            str(self.reference_path),
            self.reference_image,
        )

        self.get_logger().info(
            f"Reference captured: "
            f"{len(self.reference_keypoints)} keypoints"
        )
        self.get_logger().info(
            f"Reference image saved to: {self.reference_path}"
        )

        reference_view = cv2.drawKeypoints(
            self.reference_image,
            self.reference_keypoints,
            None,
            flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,
        )

        cv2.imshow("Reference ORB Keypoints", reference_view)

    def detect_object(self, frame: np.ndarray) -> np.ndarray:
        """기준 이미지와 현재 카메라 영상을 ORB로 비교한다."""

        if (
            self.reference_image is None
            or self.reference_keypoints is None
            or self.reference_descriptors is None
        ):
            return frame

        frame_gray = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY,
        )

        frame_keypoints, frame_descriptors = self.orb.detectAndCompute(
            frame_gray,
            None,
        )

        if (
            frame_descriptors is None
            or frame_keypoints is None
            or len(frame_keypoints) < 2
        ):
            result = frame.copy()

            self.draw_status(
                result,
                "No keypoints detected",
                (0, 0, 255),
            )

            return result

        knn_matches = self.matcher.knnMatch(
            self.reference_descriptors,
            frame_descriptors,
            k=2,
        )

        good_matches = []

        for matches in knn_matches:
            if len(matches) < 2:
                continue

            best_match, second_match = matches

            if best_match.distance < (
                self.ratio_threshold * second_match.distance
            ):
                good_matches.append(best_match)

        good_matches = sorted(
            good_matches,
            key=lambda match: match.distance,
        )

        display_matches = good_matches[:100]

        camera_result = frame.copy()

        if len(good_matches) >= self.minimum_matches:
            camera_result = self.draw_detected_object(
                camera_result,
                frame_keypoints,
                good_matches,
            )

        match_result = cv2.drawMatches(
            self.reference_image,
            self.reference_keypoints,
            camera_result,
            frame_keypoints,
            display_matches,
            None,
            matchColor=(0, 255, 0),
            singlePointColor=None,
            flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS,
        )

        if len(good_matches) >= self.minimum_matches:
            text = f"Object detected: {len(good_matches)} matches"
            color = (0, 255, 0)
        else:
            text = f"Not detected: {len(good_matches)} matches"
            color = (0, 0, 255)

        cv2.rectangle(
            match_result,
            (10, 10),
            (520, 55),
            (0, 0, 0),
            -1,
        )

        cv2.putText(
            match_result,
            text,
            (20, 42),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.75,
            color,
            2,
        )

        return match_result

    def draw_detected_object(
        self,
        frame: np.ndarray,
        frame_keypoints,
        good_matches,
    ) -> np.ndarray:
        """Homography를 이용해 검출된 물체의 경계를 표시한다."""

        if (
            self.reference_image is None
            or self.reference_keypoints is None
        ):
            return frame

        reference_points = np.float32(
            [
                self.reference_keypoints[match.queryIdx].pt
                for match in good_matches
            ]
        ).reshape(-1, 1, 2)

        frame_points = np.float32(
            [
                frame_keypoints[match.trainIdx].pt
                for match in good_matches
            ]
        ).reshape(-1, 1, 2)

        homography, mask = cv2.findHomography(
            reference_points,
            frame_points,
            cv2.RANSAC,
            5.0,
        )

        if homography is None:
            return frame

        height, width = self.reference_image.shape[:2]

        reference_corners = np.float32(
            [
                [0, 0],
                [width - 1, 0],
                [width - 1, height - 1],
                [0, height - 1],
            ]
        ).reshape(-1, 1, 2)

        detected_corners = cv2.perspectiveTransform(
            reference_corners,
            homography,
        )

        detected_corners = np.int32(detected_corners)

        cv2.polylines(
            frame,
            [detected_corners],
            True,
            (0, 255, 0),
            3,
            cv2.LINE_AA,
        )

        return frame

    @staticmethod
    def draw_status(
        image: np.ndarray,
        text: str,
        color: tuple[int, int, int],
    ) -> None:
        cv2.rectangle(
            image,
            (10, 10),
            (500, 55),
            (0, 0, 0),
            -1,
        )

        cv2.putText(
            image,
            text,
            (20, 42),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.75,
            color,
            2,
        )

    def reset_reference(self) -> None:
        """현재 등록된 기준 이미지를 초기화한다."""

        self.reference_image = None
        self.reference_gray = None
        self.reference_keypoints = None
        self.reference_descriptors = None

        cv2.destroyWindow("Reference ORB Keypoints")

        self.get_logger().info("Reference image reset.")

    def destroy_node(self) -> None:
        cv2.destroyAllWindows()
        super().destroy_node()


def main(args=None) -> None:
    rclpy.init(args=args)

    node = MatchORB()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        if rclpy.ok():
            rclpy.shutdown()

        node.destroy_node()


if __name__ == "__main__":
    main()