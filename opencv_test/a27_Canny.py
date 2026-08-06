from pathlib import Path

import cv2
import numpy as np


def main():
    file_path = Path(__file__).parent
    file_path = str(file_path / "data/lena.jpg")
    img: np.ndarray = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)  # type: ignore

    edges1 = cv2.Canny(img, 50, 100)
    edges2 = cv2.Canny(img, 50, 200)
    cv2.imshow("img", img)
    cv2.imshow("canny100", edges1)
    cv2.imshow("canny200", edges2)

    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()