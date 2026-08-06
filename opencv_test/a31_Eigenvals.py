from pathlib import Path

import cv2
import numpy as np


def findLocalMaxima(eigen_result, threshold, kernel_size):
    if eigen_result.ndim != 3 or eigen_result.shape[2] != 6:
        raise ValueError(
            "eigen_result는 cornerEigenValsAndVecs()의 (height, width, 6) 결과여야 합니다."
        )
    # 두 번째 고유값, 즉 작은 고유값을 코너 응답값으로 사용
    response = eigen_result[:, :, 1]
    kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT,
        (kernel_size, kernel_size),
    )
    # 주변 영역의 최댓값
    dilated = cv2.dilate(response, kernel)
    # 임계값보다 크면서 주변 영역의 최댓값인 위치
    local_max = (response == dilated) & (response > threshold)
    # 완전히 평탄한 영역이 선택되지 않도록 검사
    eroded = cv2.erode(response, kernel)
    local_max &= response > eroded
    # np.argwhere()는 (y, x) 순서로 반환
    points = np.argwhere(local_max)
    if points.size == 0:
        return np.empty((0, 2), dtype=np.int32)
    # OpenCV에서 사용하는 (x, y) 순서로 변경
    points = points[:, [1, 0]]
    return points.astype(np.int32)


def main():
    file_path = Path(__file__).parent
    file_path1 = str(file_path / "data/CornerTest.jpg")
    img1: np.ndarray = cv2.imread(file_path1, cv2.IMREAD_GRAYSCALE)  # type: ignore
    file_path2 = str(file_path / "data/chessBoard.jpg")
    img2: np.ndarray = cv2.imread(file_path2, cv2.IMREAD_GRAYSCALE)  # type: ignore
    file_path3 = str(file_path / "data/chessboard2.jpg")
    img3: np.ndarray = cv2.imread(file_path3, cv2.IMREAD_GRAYSCALE)  # type: ignore
    res = cv2.cornerEigenValsAndVecs(img1, 5, 3)
    ret, res2 = cv2.threshold(np.abs(res), 0.1, 0, cv2.THRESH_TOZERO)
    corners = findLocalMaxima(res2, threshold=0.2, kernel_size=11)
    for x, y in corners:
        cv2.circle(img1, (x, y), 5, 255, 2)
    cv2.imshow("img1", img1)

    res = cv2.cornerEigenValsAndVecs(img2, 5, 3)
    ret, res2 = cv2.threshold(np.abs(res), 0.1, 0, cv2.THRESH_TOZERO)
    corners = findLocalMaxima(res2, threshold=0.2, kernel_size=11)
    for x, y in corners:
        cv2.circle(img2, (x, y), 5, 255, 2)
    cv2.imshow("img2", img2)

    res = cv2.cornerEigenValsAndVecs(img3, 5, 3)
    ret, res2 = cv2.threshold(np.abs(res), 0.1, 0, cv2.THRESH_TOZERO)
    corners = findLocalMaxima(res2, threshold=0.2, kernel_size=11)
    for x, y in corners:
        cv2.circle(img3, (x, y), 5, 255, 2)
    cv2.imshow("img3", img3)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()