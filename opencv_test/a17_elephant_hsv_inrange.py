from pathlib import Path

import cv2
import numpy as np


def onChange(value):
    pass


def main():
    file_path = Path(__file__).parent
    img = cv2.imread(str(file_path / "data/elephant.jpg"))

    cv2.namedWindow("img", cv2.WINDOW_NORMAL)

    h_lower = 0
    h_up = 179
    s_lower = 0
    s_up = 255
    v_lower = 0
    v_up = 255

    cv2.createTrackbar("h_value_upper", "img", h_up, 179, onChange)
    cv2.createTrackbar("h_value_lower", "img", h_lower, 179, onChange)
    cv2.createTrackbar("s_value_upper", "img", s_up, 255, onChange)
    cv2.createTrackbar("s_value_lower", "img", s_lower, 255, onChange)
    cv2.createTrackbar("v_value_upper", "img", v_up, 255, onChange)
    cv2.createTrackbar("v_value_lower", "img", v_lower, 255, onChange)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    while True:
        h_up = cv2.getTrackbarPos("h_value_upper", "img")
        h_lower = cv2.getTrackbarPos("h_value_lower", "img")
        s_up = cv2.getTrackbarPos("s_value_upper", "img")
        s_lower = cv2.getTrackbarPos("s_value_lower", "img")
        v_up = cv2.getTrackbarPos("v_value_upper", "img")
        v_lower = cv2.getTrackbarPos("v_value_lower", "img")
        lower = np.array([h_lower, s_lower, v_lower], dtype=np.uint8)
        upper = np.array([h_up, s_up, v_up], dtype=np.uint8)
        mask = cv2.inRange(hsv, lower, upper)  # type: ignore
        cv2.imshow("img", mask)
        if cv2.waitKey(30) == ord("q"):
            break
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()