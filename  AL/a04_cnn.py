# frozen_inference_graph.pb
# faster_rcnn_resnet50_coco_2018_01_28.pbtxt
from pathlib import Path

import color
import cv2


def main():
    data_file_path = Path(__file__).parent / "data"

    with open(data_file_path / "coco90-2017.names", "r") as f:
        class_names = [line.strip() for line in f.readlines()]
    print(class_names)

    image_name = ["dog.jpg", "person.jpg", "horses.jpg", "eagle.jpg"]
    src_list = []
    for name in image_name:
        src_list.append(cv2.imread(str(data_file_path / name)))  # type: ignore

    # model load
    net = cv2.dnn.readNet(
        str(data_file_path / "frozen_inference_graph.pb"),
        str(data_file_path / "faster_rcnn_resnet50_coco_2018_01_28.pbtxt"),
    )
    # 추론
    for i, src in enumerate(src_list):
        height, width, _ = src.shape
        blob = cv2.dnn.blobFromImage(src, size=(300, 300), swapRB=True, crop=False)
        net.setInput(blob)
        outs = net.forward()
        print("outs.shape = ", outs.shape)

        # detection
        for detection in outs[0, 0, :, :]:
            label = int(detection[1])
            score = float(detection[2])

            color_t = color.COLORSL[label % len(color.COLORSL)]
            text = f"{class_names[label]} : {score}"

            if score > 0.5:
                left = int(detection[3] * width)
                top = int(detection[4] * height)
                right = int(detection[5] * width)
                bottom = int(detection[6] * height)
                cv2.rectangle(src, (left, top), (right, bottom), color_t, 2)
                cv2.putText(src, text, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color_t, 2)

        cv2.imshow("img" + str(i), src)
    cv2.waitKey()


if __name__ == "__main__":
    main()