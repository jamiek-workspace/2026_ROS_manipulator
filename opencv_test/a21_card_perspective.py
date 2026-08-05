from pathlib import Path

import cv2
import numpy as np

clicked_points = []


def mouse_callback(event, x, y, flags, param):
    """마우스 클릭 좌표만 저장한다."""
    if event != cv2.EVENT_LBUTTONDOWN:
        return

    if len(clicked_points) >= 4:
        return

    clicked_points.append((x, y))
    print(f"{len(clicked_points)}번 좌표: ({x}, {y})")


def draw_points_and_lines(img, points):
    """
    원본 영상의 복사본에 선택된 점과 선을 그린다.

    점 입력 순서:
    1: top-left
    2: top-right
    3: bottom-right
    4: bottom-left
    """
    display = img.copy()

    point_names = ["TL", "TR", "BR", "BL"]

    # 안내 문구
    cv2.putText(
        display,
        "Click: 1-TL, 2-TR, 3-BR, 4-BL",
        (10, 25),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 255, 255),
        2,
    )

    cv2.putText(
        display,
        "r: reset, q/ESC: quit",
        (10, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 255, 255),
        2,
    )

    # 선택된 점과 번호를 표시한다.
    for i, point in enumerate(points):
        x, y = point

        cv2.circle(
            display,
            (x, y),
            6,
            (0, 0, 255),
            -1,
        )

        cv2.putText(
            display,
            f"{i + 1}:{point_names[i]}",
            (x + 8, y - 8),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2,
        )

    # 클릭한 순서대로 선을 연결한다.
    for i in range(1, len(points)):
        cv2.line(
            display,
            points[i - 1],
            points[i],
            (255, 0, 0),
            2,
        )

    # 네 점이 모두 선택되면 마지막 점과 첫 점을 연결한다.
    if len(points) == 4:
        cv2.line(
            display,
            points[3],
            points[0],
            (255, 0, 0),
            2,
        )

    return display


def main():
    image_path = Path(__file__).parent / "data" / "card.bmp"

    img = cv2.imread(str(image_path))

    if img is None:
        print(f"이미지를 불러올 수 없습니다: {image_path}")
        return

    # 원근 변환 결과 크기: 가로 150, 세로 250
    output_width = 150
    output_height = 250

    window_name = "Select 4 Points"

    cv2.namedWindow(window_name)
    cv2.setMouseCallback(window_name, mouse_callback)

    print("다음 순서대로 클릭하세요.")
    print("1: 왼쪽 위     top-left")
    print("2: 오른쪽 위   top-right")
    print("3: 오른쪽 아래 bottom-right")
    print("4: 왼쪽 아래   bottom-left")
    print("r: 초기화")
    print("q 또는 ESC: 종료")

    transformed = False

    while True:
        # 매 프레임 원본 이미지에서 다시 그리므로 점과 선이 사라지지 않는다.
        display_img = draw_points_and_lines(img, clicked_points)
        cv2.imshow(window_name, display_img)

        if len(clicked_points) == 4 and not transformed:
            # 클릭한 순서를 그대로 사용한다.
            src_pts = np.array(
                clicked_points,
                dtype=np.float32,
            )

            dst_pts = np.array(
                [
                    [0, 0],  # TL
                    [output_width - 1, 0],  # TR
                    [output_width - 1, output_height - 1],  # BR
                    [0, output_height - 1],  # BL
                ],
                dtype=np.float32,
            )

            # Perspective 변환 행렬 M 계산
            M = cv2.getPerspectiveTransform(
                src_pts,
                dst_pts,
            )

            result = cv2.warpPerspective(
                img,
                M,
                (output_width, output_height),
            )

            print("\n입력된 좌표")
            print(f"TL: {src_pts[0]}")
            print(f"TR: {src_pts[1]}")
            print(f"BR: {src_pts[2]}")
            print(f"BL: {src_pts[3]}")

            print("\nPerspective Transform Matrix M")
            print(M)

            cv2.imshow("Perspective Result", result)

            transformed = True

        key = cv2.waitKey(10) & 0xFF

        if key == ord("r"):
            clicked_points.clear()
            transformed = False

            try:
                cv2.destroyWindow("Perspective Result")
            except cv2.error:
                pass

            print("\n좌표를 초기화했습니다.")
            print("TL -> TR -> BR -> BL 순서로 다시 클릭하세요.")

        elif key == ord("q") or key == 27:
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()