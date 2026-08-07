# from pathlib import Path

import cv2
import numpy as np


def main():
    nsample = 50
    traindata = np.zeros((nsample * 2, 2), np.float32)
    label = np.zeros((nsample * 2, 1), np.float32)

    cv2.randn(traindata[:nsample], 150, 30)
    cv2.randn(traindata[nsample:], 250, 60)
    label[:nsample], label[nsample:] = 0, 1

    K = 7
    knn = cv2.ml.KNearest_create()
    knn.train(traindata, cv2.ml.ROW_SAMPLE, label)  # 학습

    points = [(x, y) for y in range(400) for x in range(400)]
    res = knn.findNearest(np.array(points, np.float32), K)  # 예측, 추론
    ret, resp, neig, dist = res
    print(ret)
    print(resp)
    print(neig)
    print(dist)

    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()