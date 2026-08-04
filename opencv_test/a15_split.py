from pathlib import Path
import numpy as np
import cv2


def main():
    file_path = Path(__file__).parent
    img = cv2.imread(str(file_path / "data/lena.jpg"))

    cv2.namedWindow("img", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("img", img.shape[1], img.shape[0])

    b, g, r = cv2.split(img)
    empty = np.zeros_like(b)
    b = cv2.merge([b, empty, empty])    # type: ignore
    g = cv2.merge([empty, g, empty])
    r = cv2.merge([empty, empty, r])

    cv2.imshow("img", img)
    cv2.imshow("b_plane", b)
    cv2.imshow("g_plane", g)
    cv2.imshow("r_plane", r)

    
    cv2.waitKey()  # 블럭 함수
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()