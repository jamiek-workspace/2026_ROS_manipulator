from pathlib import Path
import cv2
import numpy as np


def main():
    file_path = Path(__file__).parent
    img = cv2.imread(str(file_path / "data/lena.jpg"))
    M1 = cv2.getRotationMatrix2D(np.array(img.shape[:2]) / 2, 45, 0.6)
    M2 = cv2.getRotationMatrix2D(np.array(img.shape[:2]) / 2, -45, 0.8)
    pts1 = np.array([[0,0],[1,0],[1,1]], dtype=np.float32)
    pts2 = np.array([[0,0],[1.3, 0],[0.7, 0.8]], dtype=np.float32)
    M3 = cv2.getAffineTransform(pts1, pts2) # type: ignore

    print(M1, type(M1))
    dst1 = cv2.warpAffine(img, M1, img.shape[:2])   # type: ignore
    dst2 = cv2.warpAffine(img, M2, img.shape[:2])   # type: ignore
    dst3 = cv2.warpAffine(img, M3, img.shape[:2])   # type: ignore
    cv2.imshow("img", img)
    cv2.imshow("dst1", dst1)
    cv2.imshow("dst2", dst2)
    cv2.imshow("dst3", dst3)
    cv2.waitKey()  # 블럭 함수
    cv2.destroyAllWindows


if __name__ == "__main__":
    main()