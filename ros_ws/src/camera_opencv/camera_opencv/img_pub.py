import rclpy
from rclpy.node import Node
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge


class M_pub(Node):
    def __init__(self):
        super().__init__("massage_pub")  # 노드 이름
        # timer 등록
        self.create_timer(1/30, self.img_gen_callback)  # 1초에 30번 호출
        cv2.namedWindow("camera")  # 윈도우 생성
        self.img = np.zeros((300, 300), dtype=np.uint8)
        self.brightness = 0
        self.pub = self.create_publisher(Image, "image_raw", 10)  # 토픽 생성
        self.bridge = CvBridge()


    def img_gen_callback(self):
        self.brightness += 1
        self.img.fill(self.brightness) # 채우기 함수
        cv2.imshow("camera", self.img)  # 이미지 출력
        if self.brightness > 255:
            self.brightness = 0
        key = cv2.waitKey(3)  # 처리 기간이 필요 milliseconse
        img = Image()
        img = self.bridge.cv2_to_imgmsg(self.img, encoding="mono8")  # cv2 -> ros msg
        img.header.stamp = self.get_clock().now().to_msg()  # 헤더 시간
        img.header.frame_id = "camera"  # 헤더 프레임
        self.pub.publish(img)  # 토픽 발행
        if key == ord("q"):
            raise KeyboardInterrupt 


def main(args=None):
    rclpy.init(args=args)  # rmw 활성화
    node = M_pub()
    try:
        rclpy.spin(node)  # 블럭 (무한 루프)
    except KeyboardInterrupt:
        print("키보드 인터럽트")
    finally:
        node.destroy_node()


if __name__ == "__main__":
    main()