from pathlib import Path

import cv2
import numpy as np


def main():
    file_path = Path(__file__).parent
    img = cv2.imread(str(file_path / "data/lena.jpg"))
    h, w = img.shape[:2]
    src_pts = np.array([[0, 0], [w - 1, 0], [w - 1, h - 1], [0, h - 1]], dtype=np.float32)    # point는 [x, y]순임에 유의
    dst_pts = np.array([[30, 64], [w - 60, 20], [w - 74, h - 52], [0, h - 93]], dtype=np.float32)
    M1 = cv2.getPerspectiveTransform(src_pts, dst_pts)  # type: ignore
    dst = cv2.warpPerspective(img, M1, (h, w))
    cv2.imshow("img", img)
    cv2.imshow("dst", dst)


    cv2.waitKey()
    cv2.destroyAllWindows


if __name__ == "__main__":
    main()