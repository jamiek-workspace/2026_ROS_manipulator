from pathlib import Path

import cv2
import numpy as np


def findLocalMaxima(src):
    kernel = cv2.getStructuringElement(shape=cv2.MORPH_RECT, ksize=(11, 11))
    dilate = cv2.dilate(src, kernel)
    localMax = src == dilate

    erode = cv2.erode(src, kernel)
    localMax2 = src > erode
    localMax &= localMax2
    points = np.argwhere(localMax == True)
    points[:, [0, 1]] = points[:, [1, 0]]
    return points


def main():
    file_path = Path(__file__).parent
    file_path1 = str(file_path / "data/CornerTest.jpg")
    img1: np.ndarray = cv2.imread(file_path1, cv2.IMREAD_GRAYSCALE)  # type: ignore
    file_path2 = str(file_path / "data/chessBoard.jpg")
    img2: np.ndarray = cv2.imread(file_path2, cv2.IMREAD_GRAYSCALE)  # type: ignore
    file_path3 = str(file_path / "data/chessboard2.jpg")
    img3: np.ndarray = cv2.imread(file_path3, cv2.IMREAD_GRAYSCALE)  # type: ignore
    res = cv2.cornerHarris(img1, 5, 3, 0.01)
    T = 0.05 * res.max()
    ret, res2 = cv2.threshold(np.abs(res), T, 0, cv2.THRESH_TOZERO)
    res = cv2.normalize(res2, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

    corners = findLocalMaxima(res2)
    for x, y in corners:
        cv2.circle(img1, (x, y), 5, 255, 2)
    cv2.imshow("img1", img1)

    res = cv2.cornerHarris(img2, 5, 3, 0.01)
    cv2.imshow("res", res)
    T = 0.1 * res.max()
    ret, res2 = cv2.threshold(np.abs(res), T, 0, cv2.THRESH_TOZERO)
    res = cv2.normalize(res2, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    corners = findLocalMaxima(res2)
    for x, y in corners:
        cv2.circle(img2, (x, y), 5, 255, 2)
    cv2.imshow("img2", img2)

    res = cv2.cornerHarris(img3, 5, 3, 0.01)
    T = 0.01 * res.max()
    ret, res2 = cv2.threshold(np.abs(res), T, 0, cv2.THRESH_TOZERO)
    res = cv2.normalize(res2, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    corners = findLocalMaxima(res2)
    for x, y in corners:
        cv2.circle(img3, (x, y), 5, 255, 2)
    cv2.imshow("img3", img3)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()