from pathlib import Path

import cv2
import numpy as np


def main():
    file_path = Path(__file__).parent
    file_path = str(file_path / "data/lena.jpg")
    img: np.ndarray = cv2.imread(str(file_path))    # type: ignore

    # Gaussian(인명은 함수더라도 대문자를 쓴다.)
    dst1 = cv2.GaussianBlur(img, (11, 11), 3)
    dst2 = cv2.GaussianBlur(img, (11, 11), 10)
    dst3 = cv2.bilateralFilter(img, -1, 10, 30)    # bilateral 노이즈 없애면서 경계강화

    cv2.imshow("img", img)
    cv2.imshow("Gaussian", dst1)
    cv2.imshow("Gaussian10", dst2)
    cv2.imshow("bilaterial", dst3)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()