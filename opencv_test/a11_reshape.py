from pathlib import Path

import cv2
import numpy as np


def main():
    file_path = Path(__file__).parent
    img = cv2.imread(str(file_path/ "data/lena.jpg"))

    cv2.namedWindow("img", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("img", img.shape[1], img.shape[0])

    print("img.shape= ", img.shape)
    img = img.flatten()
    print("img.shape= ", img.shape)
    img = img.reshape((512, 512, 3))
    print("img.shape= ", img.shape)
    cv2.imshow("img", img)
    cv2.waitKey()  # 블럭 함수
    cv2.destroyAllWindows


if __name__ == "__main__":
    main()