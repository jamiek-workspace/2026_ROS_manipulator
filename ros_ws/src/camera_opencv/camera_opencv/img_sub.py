import rclpy
from rclpy.node import Node
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge


class M_sub(Node):
    def __init__(self):
        super().__init__("massage_sub")  # 노드 이름
        cv2.namedWindow("camera")  # 윈도우 생성
        self.bridge = CvBridge()
        self.create_subscription(Image, "image_raw", self.img_callback, 10)  # 토픽 구독


    def img_callback(self, img: Image):
        img_sub = self.bridge.imgmsg_to_cv2(img)  # ros msg -> cv2
        cv2.imshow("camera", img_sub)  # 이미지 출력
        key = cv2.waitKey(3)  # 처리 기간이 필요 milliseconse
        if key == ord("q"):
            raise KeyboardInterrupt 


def main(args=None):
    rclpy.init(args=args)  # rmw 활성화
    node = M_sub()
    try:
        rclpy.spin(node)  # 블럭 (무한 루프)
    except KeyboardInterrupt:
        print("키보드 인터럽트")
    finally:
        node.destroy_node()


if __name__ == "__main__":
    main()