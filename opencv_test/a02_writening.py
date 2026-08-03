# python3 a02_writening.py
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
    img = cv2.imread(str(file_path / "data/robot.png"), cv2.IMREAD_GRAYSCALE)    # 절대 경로
    print(type(img), img.shape, img.dtype)
    img = cv2.resize(img, (2000, 500))  # 500, height, y, 2000, width, x
    x = img.shape[1]
    y = img.shape[0]
    print(x, y)
    cv2.imshow("robot", img)

    cv2.imwrite(str(file_path / "data" / "robot_gray.jpg"), img)
    imwrite_op = [cv2.IMWRITE_JPEG_QUALITY, 10]  # 0~100, 100이 최고 품질
    cv2.imwrite(str(file_path / "data" / "robot_gray.jpg"), img, imwrite_op)
    cv2.imwrite(str(file_path / "data" / "robot_gray.bmp"), img)
    cv2.waitKey()   # 블럭 함수


if __name__ == "__main__":
    main()


