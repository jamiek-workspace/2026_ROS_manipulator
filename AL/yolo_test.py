import cv2
from ultralytics import YOLO


def main():
    model = YOLO("yolo26n.pt")  # load a pretrained YOLO26n model
    results = model("/home/jamiek/2026_ROS_manipulator/AL/data/dog.jpg")  # run inference

    annotated =results[0].plot()
    cv2.imshow("result", annotated)
    cv2.waitKey()


if __name__ == "__main__":
    main()