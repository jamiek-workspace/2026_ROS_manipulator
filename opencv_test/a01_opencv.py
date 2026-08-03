# python3 a01_opencv.py
# sudo apt install python3-venv python3-pip
# python3 -m venv --system-site-packages .venv
# touch .venv/COLCON_IGNORE
# source .venv/bin/activate (가상환경. 오른쪽 하단으로 선택 가능)
# python -m pip install --no-deps opencv-stubs

import cv2
import numpy as np
from pathlib import Path


def main():
    file_path = Path(__file__).parent
    print("안녕하세요")
    print("OpenCV version:", cv2.__version__)
    # black_img = np.array((300, 300, 1), dtype=np.uint8)
    # cv2.imshow("black", black_img)
    # img = cv2.imread("data/robot.png")  # 상대 경로

    img = cv2.imread(str(file_path / "data/robot.png"))    # 절대 경로
    cv2.imshow("robot", img)
    cv2.waitKey()   # 블럭 함수


if __name__ == "__main__":
    main()


