from pathlib import Path
import numpy as np
import cv2


def main():
    file_path = Path(__file__).parent
    img = cv2.imread(str(file_path / "data/lena.jpg"))

    cv2.namedWindow("img", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("img", img.shape[1], img.shape[0])

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    # 알고리즘
    # 역변화... cvtColor

    cv2.imshow("img", img)
    cv2.imshow("hsv", hsv)
    cv2.imshow("ycrcb", ycrcb)
    cv2.imshow("gray", gray)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()