# from pathlib import Path

import color
import cv2
import numpy as np


def onMouse(event, x, y, flags, param):
    img, option = param
    # old_x, old_y = 0, 0
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 1, color.RED, 2)
        print("왼쪽 버튼 클릭", x, y)
        onMouse.old_x = x   # 함수 속성 변수(c의 static처럼 활용 가능)
        onMouse.old_y = y
    if flags == cv2.EVENT_FLAG_LBUTTON and event == cv2.EVENT_MOUSEMOVE:
        print("드래그")
        cv2.line(img,(onMouse.old_x, onMouse.old_y), (x,y), list(color.COLORS.values())[option[0]], 2)
        onMouse.old_x = x
        onMouse.old_y = y
    elif event == cv2.EVENT_MOUSEMOVE:
        print("마우스 이동", x, y)
    cv2.imshow("canvas", img)




def main():
    # file_path = Path(__file__).parent
    cv2.namedWindow("canvas")
    img = np.zeros((300, 700, 3), dtype=np.uint8)
    option = [0]
    cv2.setMouseCallback("canvas", onMouse, (img, option))

    cv2.imshow("canvas", img)
    while True:
        key = cv2.waitKey(30)
        if key == ord("q"):
            break
        if key == ord(" "):
            option[0] += 1
        if option[0] > 12:
            option[0] = 0


if __name__ == "__main__":
    main()