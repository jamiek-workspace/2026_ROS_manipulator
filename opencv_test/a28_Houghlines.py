from pathlib import Path

import cv2
import numpy as np


def main():
    file_path = Path(__file__).parent
    file_path = str(file_path / "data/apartment.jpg")
    img: np.ndarray = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)  # type: ignore
    edges = cv2.Canny(img, 50, 200)
    lines: np.ndarray = cv2.HoughLines(edges, rho=1, theta=np.pi / 180.0, threshold=100)  # type: ignore
    print("lines.shape=", lines.shape)
    cnt = 0
    for line in lines:
        rho, theta = line[0]
        c = np.cos(theta)
        s = np.sin(theta)
        x0 = c * rho
        y0 = s * rho
        x1 = int(x0 + 1000 * (-s))
        y1 = int(y0 + 1000 * (c))
        x2 = int(x0 - 1000 * (-s))
        y2 = int(y0 - 1000 * (c))
        cv2.line(img, (x1, y1), (x2, y2), (255), 1)
        if cnt > 100:
            break
        cnt += 1
    cv2.imshow("canny", edges)
    cv2.imshow("img", img)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()