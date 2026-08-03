# sudo usermod -aG video $USER
# sudo chmod 666 /dev/video0
# sudo chmod 666 /dev/video1
# v4l2-ctl --list-devices
# v4l2-ctl -d /dev/video0 --list-formats-ext
# gst-launch-1.0 --version
# gst-launch-1.0 v4l2src device=/dev/video0 ! image/jpeg,width=640,height=480,framerate=30/1 ! jpegdec ! videoconvert ! autovideosink
from pathlib import Path

import cv2


def main():
    file_path = Path(__file__).parent
    cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
    # MJPG 설정
    fourcc = cv2.VideoWriter_fourcc(*"MJPG")
    cap.set(cv2.CAP_PROP_FOURCC, fourcc)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FPS, 30)

    if not cap.isOpened():
        return
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("black", frame)
        if cv2.waitKey(1) == ord("q"):
            break
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()