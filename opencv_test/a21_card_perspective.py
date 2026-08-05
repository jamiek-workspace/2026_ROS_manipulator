from pathlib import Path

import cv2
import numpy as np

# 마우스로 선택한 점을 저장한다.
clicked_points = []


def order_points(points):
    """
    4개의 점을 다음 순서로 정렬한다.

    0: 왼쪽 위
    1: 오른쪽 위
    2: 오른쪽 아래
    3: 왼쪽 아래
    """
    points = np.array(points, dtype=np.float32)

    ordered = np.zeros((4, 2), dtype=np.float32)

    # x + y 값
    point_sum = points.sum(axis=1)

    # x - y 값
    point_diff = np.diff(points, axis=1).reshape(-1)

    # 합이 가장 작은 점: 왼쪽 위
    ordered[0] = points[np.argmin(point_sum)]

    # 차이가 가장 작은 점: 오른쪽 위
    ordered[1] = points[np.argmin(point_diff)]

    # 합이 가장 큰 점: 오른쪽 아래
    ordered[2] = points[np.argmax(point_sum)]

    # 차이가 가장 큰 점: 왼쪽 아래
    ordered[3] = points[np.argmax(point_diff)]

    return ordered


def mouse_callback(event, x, y, flags, param):
    display_img = param

    if event == cv2.EVENT_LBUTTONDOWN:
        # 점은 최대 4개까지만 선택한다.
        if len(clicked_points) >= 4:
            return

        clicked_points.append((x, y))

        point_number = len(clicked_points)

        # 클릭한 위치에 점 표시
        cv2.circle(display_img, (x, y), 6, (0, 0, 255), -1)

        # 클릭 순서 표시
        cv2.putText(
            display_img,
            str(point_number),
            (x + 8, y - 8),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2,
        )

        # 이전 점과 현재 점 연결
        if point_number >= 2:
            cv2.line(
                display_img,
                clicked_points[-2],
                clicked_points[-1],
                (255, 0, 0),
                2,
            )

        # 네 번째 점을 찍으면 첫 번째 점과 연결
        if point_number == 4:
            cv2.line(
                display_img,
                clicked_points[3],
                clicked_points[0],
                (255, 0, 0),
                2,
            )

        cv2.imshow("Select 4 Points", display_img)


def main():
    global clicked_points

    file_path = Path("/home/jamiek/2026_ROS_manipulator/opencv_test/data/card.bmp")

    img = cv2.imread(str(file_path))

    if img is None:
        print(f"이미지를 불러올 수 없습니다: {file_path}")
        return

    # 원본 이미지를 직접 수정하지 않도록 복사한다.
    display_img = img.copy()

    cv2.namedWindow("Select 4 Points")
    cv2.setMouseCallback("Select 4 Points", mouse_callback, display_img)

    print("카드의 꼭짓점 4개를 마우스 왼쪽 버튼으로 클릭하세요.")
    print("클릭 순서는 상관없습니다.")
    print("r: 선택 초기화")
    print("q 또는 ESC: 종료")

    while True:
        cv2.imshow("Select 4 Points", display_img)

        key = cv2.waitKey(10) & 0xFF

        # 4개의 점이 모두 선택되면 원근 변환 실행
        if len(clicked_points) == 4:
            src_pts = order_points(clicked_points)

            # 결과 영상 크기
            output_width = 300
            output_height = 200

            dst_pts = np.array(
                [
                    [0, 0],
                    [output_width - 1, 0],
                    [output_width - 1, output_height - 1],
                    [0, output_height - 1],
                ],
                dtype=np.float32,
            )

            perspective_matrix = cv2.getPerspectiveTransform(src_pts, dst_pts)

            result = cv2.warpPerspective(
                img,
                perspective_matrix,
                (output_width, output_height),
            )

            cv2.imshow("Perspective Result", result)

            # 같은 네 점으로 계속 변환하지 않도록 대기
            while True:
                result_key = cv2.waitKey(0) & 0xFF

                if result_key == ord("r"):
                    clicked_points.clear()
                    display_img[:] = img
                    cv2.destroyWindow("Perspective Result")
                    break

                if result_key == ord("q") or result_key == 27:
                    cv2.destroyAllWindows()
                    return

        # r 키를 누르면 선택 초기화
        if key == ord("r"):
            clicked_points.clear()
            display_img[:] = img

            try:
                cv2.destroyWindow("Perspective Result")
            except cv2.error:
                pass

        # q 또는 ESC 키로 종료
        if key == ord("q") or key == 27:
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()