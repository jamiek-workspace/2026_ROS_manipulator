# gst-launch-1.0 --version
# sudo apt install gstreamer1.0-plugins-good
# gst-launch-1.0 device=/dev/video0 ! image/jpeg,width=640,height=480,framerate=30/1 ! jpegdec ! videoconvert ! autovideosink
from pathlib import Path

import cv2


def main():
    file_path = Path(__file__).parent
    pipeline = (
        "v4l2src device=/dev/video0 ! "
        "image/jpeg,width=640,height=480,framerate=30/1 ! "
        "jpegdec ! "
        "videoconvert ! "
        "video/x-raw,format=BGR ! "
        "appsink drop=true sync=false"
    )
    cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)
    # MJPG 설정

    if not cap.isOpened():
        return
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) == ord("q"):
            break
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()