# python3 -c "import cv2; print(cv2.__version__); print(cv2.getBuildInformation())" | rg aruco
# sudo apt install -y python3-venv python3-full
# source .venv/bin/activate
# python -m pip install --upgrade pip
# python -m pip install "numpy==1.26.4"
# python -m pip install "opencv-contrib-python==4.6.0.66"
# python -m pip uninstall "opencv-contrib-python==4.6.0.66"
from pathlib import Path

import cv2
import numpy as np


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

    # dictionary
    dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
    parameters = cv2.aruco.DetectorParameters_create()

    previous_ids = set()

    marker_length = 0.04

    camera_matrix = np.array(
        [[600.0, 0.0, 320.0], [0.0, 600.0, 240.0], [0.0, 0.0, 1.0]], dtype=np.float64
    )
    dist_coeffs = np.zeros((5, 1), dtype=np.float64)

    if not cap.isOpened():
        print("cap close")
        return
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        corners, ids, rejected = cv2.aruco.detectMarkers(gray, dictionary, parameters=parameters)
        if ids is not None:
            cv2.aruco.drawDetectedMarkers(frame, corners, ids)
            rvecs, tvecs, object_points = cv2.aruco.estimatePoseSingleMarkers(
                corners, marker_length, camera_matrix, dist_coeffs
            )
            print(rvecs, tvecs)
        if not ret:
            continue
        # detection 하는 코드

        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) == ord("q"):
            break
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()