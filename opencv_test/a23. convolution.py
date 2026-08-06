from pathlib import Path

import cv2
import numpy as np


def main():
    file_path = Path(__file__).parent
    file_path = str(file_path / "data/lena.jpg")
    img: np.ndarray = cv2.imread(str(file_path))

    # boxfilter
    dst1 = cv2.boxFilter(img, ddepth=-1, ksize=(7, 7)) # ksize는 홀수여야 함

    # blur
    dst2 = cv2.blur(img, (11, 11))

    # filter 20
    kernel = np.ones((11, 11)) / 121
    dst3 = cv2.filter2D(img, ddepth=-1, kernel=kernel)

    cv2.imshow("img", img)
    cv2.imshow("box11", dst1)
    cv2.imshow("blur", dst2)
    cv2.imshow("filter 20", dst3)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()