from pathlib import Path

import cv2
import numpy as np


def main():
    file_path = Path(__file__).parent
    white_img = np.full((600, 600, 3), 255, dtype=np.uint8)
    pt1 = 100, 100
    diff = 0
    while True:
        white_img = np.full((600, 600, 3), 255, dtype=np.uint8)
        diff += 1
        cv2.rectangle(white_img, pt1, (400 - diff, 400 - diff), (0, 255, 0), 2)
        cv2.line(white_img, (0, 0), (500, diff), (255, 0, 0), 5)
        cv2.line(white_img, (0, 0), (diff, 500), (0, 0, 255), 5)
        cv2.imshow("white", white_img)
        if cv2.waitKey(30) == ord("q"):  # 블럭 함수
            break
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()