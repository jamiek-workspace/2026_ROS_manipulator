import time
from pathlib import Path

import cv2
import numpy as np


def draw_point(img, group, color):
    """이미지에 데이터 포인트를 원으로 표시"""
    for p in group:
        pt = tuple(p.astype(int))

        # 화면 영역 안에 있는 점만 표시
        if 0 <= pt[0] < img.shape[1] and 0 <= pt[1] < img.shape[0]:
            cv2.circle(img, pt, 3, color, cv2.FILLED)


def load_knn(model_path="knn_model.xml"):
    """저장된 KNN 모델 로드"""

    model_path = Path(model_path)

    if not model_path.exists():
        raise FileNotFoundError(f"모델 파일을 찾을 수 없습니다: {model_path}")

    knn = cv2.ml.KNearest_load(str(model_path))

    if not knn.isTrained():
        raise RuntimeError("KNN 모델이 학습된 상태가 아닙니다.")

    print("모델 로드 완료:", model_path)

    return knn


def validate_knn(knn, image, nsample=50, K=7):
    """새로운 랜덤 데이터로 KNN 모델 검증"""

    testdata = np.zeros((nsample * 2, 2), np.float32)

    testlabel = np.zeros((nsample * 2, 1), np.float32)

    # 클래스 0
    cv2.randn(testdata[:nsample], 150, 30)

    # 클래스 1
    cv2.randn(testdata[nsample:], 250, 60)

    testlabel[:nsample] = 0
    testlabel[nsample:] = 1

    # 예측
    ret, predicted, neighbors, dist = knn.findNearest(testdata, K)

    # 정확도 계산
    correct = np.sum(predicted == testlabel)

    total = len(testlabel)
    accuracy = correct / total

    print()
    print("===== 검증 결과 =====")
    print("전체 데이터 :", total)
    print("정답 개수   :", correct)
    print("오답 개수   :", total - correct)
    print(f"정확도      : {accuracy * 100:.2f}%")

    # 실제 label / 예측 label을 1차원으로 변환
    true_label = testlabel.ravel()
    pred_label = predicted.ravel()

    correct_mask = true_label == pred_label

    wrong_mask = true_label != pred_label

    # class 0 중 맞게 분류한 데이터
    group0_correct = testdata[(true_label == 0) & correct_mask]

    # class 1 중 맞게 분류한 데이터
    group1_correct = testdata[(true_label == 1) & correct_mask]

    # 잘못 분류한 데이터
    group_wrong = testdata[wrong_mask]

    # 검증 데이터 표시
    # class 0 정답 : 노랑
    draw_point(image, group0_correct, color=(0, 255, 255))

    # class 1 정답 : 하늘색
    draw_point(image, group1_correct, color=(255, 255, 0))

    # 오답 : 흰색
    draw_point(image, group_wrong, color=(255, 255, 255))

    return image


def create_decision_image(knn, width=400, height=400, K=7):
    """KNN 분류 결과를 전체 이미지로 생성"""

    points = [(x, y) for y in range(height) for x in range(width)]

    points = np.array(points, dtype=np.float32)

    # 저장된 KNN 모델로 예측
    ret, resp, neighbors, dist = knn.findNearest(points, K)

    # 분류 결과에 따른 배경색
    colors = [(0, 180, 0) if p == 1 else (0, 0, 180) for p in resp.ravel()]

    image = np.reshape(colors, (height, width, 3)).astype(np.uint8)

    return image


def main():

    # 실행마다 다른 검증 데이터 생성
    seed = int(time.time_ns() % (2**31 - 1))

    cv2.setRNGSeed(seed)

    print("random seed:", seed)

    # -----------------------------
    # 저장 모델 불러오기
    # -----------------------------
    knn = load_knn("knn_model.xml")

    K = 7

    # -----------------------------
    # 분류 영역 생성
    # -----------------------------
    image = create_decision_image(knn, width=400, height=400, K=K)

    # -----------------------------
    # 검증
    # -----------------------------
    image = validate_knn(knn, image, nsample=50, K=K)

    # -----------------------------
    # 결과 출력
    # -----------------------------
    cv2.imshow("Loaded KNN Model", image)

    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()