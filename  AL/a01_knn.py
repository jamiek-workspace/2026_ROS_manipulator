# from pathlib import Path

import time

import cv2
import numpy as np


def draw_point(img, group, color):
    for p in group:
        pt = tuple(p.astype(int))
        cv2.circle(img, pt, 3, color, cv2.FILLED)


def validate_knn(knn, image, nsample=50, K=7):
    """학습된 KNN 모델을 새로운 랜덤 데이터로 검증하고 화면에 표시"""

    # 검증 데이터 생성
    testdata = np.zeros((nsample * 2, 2), np.float32)
    testlabel = np.zeros((nsample * 2, 1), np.float32)

    # 학습 데이터와 동일한 분포에서 새로운 데이터 생성
    cv2.randn(testdata[:nsample], 150, 30)
    cv2.randn(testdata[nsample:], 250, 60)

    testlabel[:nsample] = 0
    testlabel[nsample:] = 1

    # 예측
    ret, predicted, neighbors, dist = knn.findNearest(testdata, K)

    # 정확도 계산
    correct = np.sum(predicted == testlabel)
    total = len(testlabel)
    accuracy = correct / total

    print("\n===== 검증 결과 =====")
    print("전체 데이터 :", total)
    print("정답 개수   :", correct)
    print("오답 개수   :", total - correct)
    print(f"정확도      : {accuracy * 100:.2f}%")

    # -----------------------------
    # 검증 데이터 시각화
    # -----------------------------
    # 1차원으로 변환
    true_label = testlabel.ravel()
    pred_label = predicted.ravel()

    # 정오답 마스크
    correct_mask = true_label == pred_label
    wrong_mask = true_label != pred_label

    # 클래스별 + 정오답별 분리
    group0_correct = testdata[(true_label == 0) & correct_mask]
    group1_correct = testdata[(true_label == 1) & correct_mask]
    group_wrong = testdata[wrong_mask]

    # 검증 데이터 표시
    # 클래스 0 정답: 노랑
    draw_point(image, group0_correct, color=(0, 255, 255))

    # 클래스 1 정답: 하늘색
    draw_point(image, group1_correct, color=(255, 255, 0))

    # 오답: 흰색
    draw_point(image, group_wrong, color=(255, 255, 255))

    return image


def main():
    nsample = 50
    traindata = np.zeros((nsample * 2, 2), np.float32)
    label = np.zeros((nsample * 2, 1), np.float32)

    seed = int(time.time_ns() % (2**31 - 1))
    cv2.setRNGSeed(seed)

    cv2.randn(traindata[:nsample], 150, 30)
    cv2.randn(traindata[nsample:], 250, 60)
    label[:nsample], label[nsample:] = 0, 1

    K = 7
    knn = cv2.ml.KNearest_create()
    knn.train(traindata, cv2.ml.ROW_SAMPLE, label)  # 학습
    knn.save("knn_model.xml")

    points = [(x, y) for y in range(400) for x in range(400)]
    res = knn.findNearest(np.array(points, np.float32), K)  # 예측, 추론
    ret, resp, neig, dist = res
    print(ret)
    print(resp)
    print(neig)
    print(dist)
    colors = [(0, 180, 0) if p == 1 else (0, 0, 180) for p in resp]
    image = np.reshape(colors, (400, 400, 3)).astype("uint8")
    draw_point(image, traindata[:nsample], color=(0, 0, 255))
    draw_point(image, traindata[nsample:], color=(0, 255, 0))

    validate_knn(knn, image)
    cv2.imshow("img", image)

    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()