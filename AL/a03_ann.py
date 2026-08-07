import cv2
import numpy as np

np.set_printoptions(precision=2, suppress=True)


def main():
    x_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=np.float32)
    y_train = np.array([[0, 0, 0, 1]], dtype=np.float32).reshape((4, 1))

    model = cv2.ml.ANN_MLP_create()

    model.setLayerSizes(np.array([2, 1]))
    model.setTrainMethod(cv2.ml.ANN_MLP_BACKPROP)
    model.setActivationFunction(cv2.ml.ANN_MLP_SIGMOID_SYM, 2, 1)
    model.setTermCriteria((cv2.TermCriteria_EPS + cv2.TermCriteria_COUNT, 1000, 1e-5))

    # 데이터 학습
    ret = model.train(samples=x_train, layout=cv2.ml.ROW_SAMPLE, responses=y_train)
    # weight
    layerSize = model.getLayerSizes()
    print(layerSize)
    for i in range(layerSize.shape[0] + 2):
        print(i, model.getWeights(i))

    # 추론(순전파)
    ret, y_out = model.predict(x_train)
    print("y_out", y_out)

    y_pred = np.int32(y_out > 0.5)
    print("y_pred", y_pred)

    # 검증
    y_pred = y_pred.flatten()
    y_train = y_train.flatten()
    accuracy = np.sum(y_train == y_pred) / len(y_train)
    print("accuracy", accuracy)


if __name__ == "__main__":
    main()