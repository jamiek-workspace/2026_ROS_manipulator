# from pathlib import Path

import cv2
import numpy as np


def main():
    # file_path = Path(__file__).parent
    img = np.zeros((500, 500, 1), dtype=np.uint8)
    cv2.imshow("img", img)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()