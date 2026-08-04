from pathlib import Path

import cv2


def main():
    file_path = Path(__file__).parent
    img = cv2.imread(str(file_path / "data/lena.jpg"))

    cv2.namedWindow("img", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("img", img.shape[1], img.shape[0])

    # 얕은 복사
    roi = img[100:200, 300:400]  # roi 가 새로운 메모리 영역을 가지지 않는다.
    # 깊은 복사
    roi2 = img[100:200, 300:400].copy()
    roi2[:, :] = (0, 255, 0)

    cv2.imshow("img", img)
    cv2.imshow("roi", roi2)
    cv2.waitKey()  # 블럭 함수
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()