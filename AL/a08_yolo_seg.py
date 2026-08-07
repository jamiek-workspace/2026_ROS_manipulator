import time

import cv2
import numpy as np
import torch
from ultralytics import YOLO


def main():
    print(torch.__version__)
    print(torch.cuda.is_available())

    # 모델 로드
    model = YOLO("yolo26n-seg.pt")  # yolo11n-seg.py

    cap = cv2.VideoCapture(0, cv2.CAP_V4L2)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FPS, 30)
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))

    start = time.time()
    frames = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model.predict(frame, stream=False, verbose=False)

        res = results[0]
        # print(f"res.boxes: {res.boxes}")
        # print(f"res.names: {res.names}")
        # print(f"res.keypoints: {res.keypoints}")
        # print(f"res.masks: {res.masks}")
        # print(f"res.probes: {res.probs}")

        class_info = []
        index_info = []
        for i, cls in enumerate(res.boxes.cls):
            label = res.names.get(int(cls), "unknown")
            class_info.append(label)
            index_info.append(i)

        # annotated = results[0].plot()
        frames += 1
        fps = frames / (time.time() - start)
        cv2.putText(
            frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2
        )

        # person 의 좌표 얻기
        for label, idx in zip(class_info, index_info):
            if label == "person":
                mask = res.masks.data[idx].cpu().numpy()
                # frame 에 mask 적용하기 해서 블러 처리 하기
                # blurred = cv2.GaussianBlur(frame, (51, 51), 0)
                # frame = np.where(mask[:, :, None], blurred, frame)
                # frame 에 mask 부분만 노락색 색상을 칠하기
                # yellow = np.full_like(frame, (0, 255, 255))
                # frame = np.where(mask[:, :, None], yellow, frame)
                # frame 에 mask 부분만 반투명하게 노락색 색상을 칠하기
                kernel = np.ones((15, 15), np.uint8)
                # morphology 처리로 마스크 영상 넓히기
                # mask = cv2.dilate(mask.astype(np.uint8), kernel, iterations=5).astype(bool)
                # morphology 처리로 마스크 영상 졻히기
                # mask = cv2.erode(mask.astype(np.uint8), kernel, iterations=2).astype(bool)
                # morphology 처리로 마스크 영상 열기 (침식 후 팽창)
                # mask = cv2.morphologyEx(mask.astype(np.uint8), cv2.MORPH_OPEN, kernel, iterations=3).astype(bool)
                # morphology 처리로 마스크 영상 닫기 (팽창 후 침식)
                mask = cv2.morphologyEx(
                    mask.astype(np.uint8), cv2.MORPH_RECT, kernel, iterations=1
                ).astype(bool)

                yellow = np.full_like(frame, (0, 255, 255))
                frame = np.where(
                    mask[:, :, None],
                    np.clip(frame * 0.4 + yellow * 0.8, 0, 255).astype(np.uint8),
                    frame,
                )

        if cv2.waitKey(1) & 0xFF == 27:
            break
        cv2.imshow("YOLOv8 Inference", frame)

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()