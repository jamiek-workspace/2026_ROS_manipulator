from pathlib import Path

import cv2
import numpy as np


def main():
    file_path = Path(__file__).parent
    file_path = str(file_path / "data/lena.jpg")
    img: np.ndarray = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)  # type: ignore
    # Gaussian 사람이은 함수더라도 대문자를 쓴다.
    gx = cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=3)
    gy = cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize=3)
    dstX = cv2.sqrt(np.abs(gx))
    dstX = cv2.normalize(dstX, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)  # type: ignore

    dstY = cv2.sqrt(np.abs(gy))
    dstY = cv2.normalize(dstY, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)  # type: ignore

    mag = cv2.magnitude(gx, gy)
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(mag)
    print("mag:", minVal, maxVal, minLoc, maxLoc)

    dstM = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)  # type: ignore
    cv2.imshow("img", img)
    cv2.imshow("dstX", dstX)
    cv2.imshow("dstY", dstY)
    cv2.imshow("dstM", dstM)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()