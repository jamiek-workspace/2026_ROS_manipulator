from pathlib import Path

import cv2
import numpy as np


def find_harris(img):
    fast = cv2.FastFeatureDetector_create(
        threshold=20, nonmaxSuppression=True, type=cv2.FastFeatureDetector_TYPE_9_16
    )
    keypoints: list[cv2.KeyPoint] = fast.detect(img, None)
    print(keypoints, len(keypoints))

    result = cv2.drawKeypoints(
        img, keypoints, None, color=(0, 0, 255), flags=cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS
    )
    return result


def find_orb(img):
    orb = cv2.ORB_create(
        nfeatures=30, scaleFactor=1.2, nlevels=8, edgeThreshold=31, fastThreshold=20
    )
    keypoints, _ = orb.detectAndCompute(img, None)
    print(keypoints, len(keypoints))

    result = cv2.drawKeypoints(
        img, keypoints, None, color=(0, 0, 255), flags=cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS
    )
    return result


def find_gftt(img):
    corners = cv2.goodFeaturesToTrack(
        img, maxCorners=30, qualityLevel=0.01, minDistance=10, blockSize=5, useHarrisDetector=False
    )
    points = np.int32(corners.reshape(-1, 2))
    for x, y in points:
        cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), 4)
    return img


def find_harris(img):
    fast = cv2.FastFeatureDetector_create(
        threshold=20, nonmaxSuppression=True, type=cv2.FastFeatureDetector_TYPE_9_16
    )
    keypoints: list[cv2.KeyPoint] = fast.detect(img, None)
    print(keypoints, len(keypoints))

    result = cv2.drawKeypoints(
        img, keypoints, None, color=(0, 0, 255), flags=cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS
    )
    return result


def main():
    file_path = Path(__file__).parent
    file_path1 = str(file_path / "data/CornerTest.jpg")
    img1: np.ndarray = cv2.imread(file_path1, cv2.IMREAD_GRAYSCALE)  # type: ignore
    file_path2 = str(file_path / "data/chessBoard.jpg")
    img2: np.ndarray = cv2.imread(file_path2, cv2.IMREAD_GRAYSCALE)  # type: ignore
    file_path3 = str(file_path / "data/chessboard2.jpg")
    img3: np.ndarray = cv2.imread(file_path3, cv2.IMREAD_GRAYSCALE)  # type: ignore

    cv2.imshow("img1", find_harris(img1))
    cv2.imshow("img2", find_harris(img2))
    cv2.imshow("img3", find_harris(img3))
    cv2.imshow("img4", find_gftt(img1))
    cv2.imshow("img5", find_gftt(img2))
    cv2.imshow("img6", find_gftt(img3))
    cv2.imshow("img7", find_orb(img1))
    cv2.imshow("img8", find_orb(img2))
    cv2.imshow("img9", find_orb(img3))

    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()