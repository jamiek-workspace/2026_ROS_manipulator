# mask 선행, inrange -> contour -> morphology
# threshold, adaptivethreshold -> ..morphology. -> contour

from pathlib import Path

import cv2
import numpy as np


def main():
    file_path = Path(__file__).parent
    file_path = str(file_path / "data/morphology.jpg")
    img: np.ndarray = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)  # type: ignore

    kernel = cv2.getStructuringElement(shape=cv2.MORPH_RECT, ksize=(3, 3))
    erode = cv2.erode(img, kernel, iterations=5)
    dilate = cv2.dilate(img, kernel, iterations=5)
    open = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=5)
    close = cv2.morphologyEx(open, cv2.MORPH_CLOSE, kernel, iterations=5)
    gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
    tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel, iterations=5)
    blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel, iterations=5)
    cv2.imshow("img", img)
    cv2.imshow("erode", erode)
    cv2.imshow("dilate", dilate)
    cv2.imshow("open", open)
    cv2.imshow("close", close)
    cv2.imshow("gradient", gradient)
    cv2.imshow("tophat", tophat)
    cv2.imshow("blackhat", blackhat)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()