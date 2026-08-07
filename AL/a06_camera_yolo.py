# depth + yolo 가상 환경에서 실행
import cv2
from ultralytics import YOLO


def main():

    cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
    # MJPG 설정
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc("M", "J", "P", "G"))
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FPS, 30)

    if not cap.isOpened():
        print("cap is not open")
        return

    model = YOLO("yolo26n.pt")  # load a pretrained YOLO26n model
    while True:
        ret, frame = cap.read()
        results = model(frame)
        annotated = results[0].plot()  # type: ignore

        if not ret:
            break
        cv2.imshow("Camera", annotated)
        if cv2.waitKey(1) == ord("q"):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()