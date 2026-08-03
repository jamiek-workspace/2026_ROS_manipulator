# python3 a03_matplotColor.py

from pathlib import Path
import cv2
import numpy as np
from matplotlib import pyplot as plt

def main():
    file_path = Path(__file__).parent
    img = cv2.imread(str(file_path / "data/robot.png"))
    cv2.imshow("robot", img)
    plt.axis("off")
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)   # 다른 프로그램에서 사용 시 해당 순서 바꿔줘야 함
    plt.imshow(imgRGB)
    cv2.waitKey(30)
    plt.show()


if __name__ == "__main__":
    main()