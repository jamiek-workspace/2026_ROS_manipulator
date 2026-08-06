from pathlib import Path

import cv2
import numpy as np


def main():
    file_path = Path(__file__).parent
    file_path = str(file_path / "data/apartment.jpg")
    img: np.ndarray = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)  # type: ignore
    edges = cv2.Canny(img, 50, 200)
    lines: np.ndarray = cv2.HoughLinesP(edges, rho=1, theta=np.pi / 180.0, threshold=100)  # type: ignore
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img, (x1, y1), (x2, y2), (255), 1)
    cv2.imshow("canny", edges)
    cv2.imshow("img", img)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()