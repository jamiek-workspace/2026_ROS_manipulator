from pathlib import Path
import cv2
import numpy as np


def main():
    file_path = Path(__file__).parent
    img = cv2.imread(str(file_path / "data/lena.jpg"))
    dst1 = cv2.resize(img, (50, 50))
    dst2 = cv2.resize(img, np.array(img.shape[0:2]), fx = 0.8, fy = 0.7)
    dst3 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    dst4 = cv2.flip(img, 0)
    dst5 = cv2.flip(img, -1)
    dst6 = cv2.flip(img, 1)

    cv2.imshow("img", img)
    cv2.imshow("resize", dst1)
    cv2.imshow("scale", dst2)
    cv2.imshow("rotate", dst3)
    cv2.imshow("flip vertical", dst4)
    cv2.imshow("flip horizon", dst5)
    cv2.imshow("flip both", dst6)
    cv2.waitKey()  # 블럭 함수
    cv2.destroyAllWindows


if __name__ == "__main__":
    main()