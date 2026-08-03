# ros2 topic bw /image_raw/compressed

import cv2
import numpy as np
import rclpy
from cv_bridge import CvBridge
from rclpy.node import Node
from sensor_msgs.msg import CompressedImage


class M_pub(Node):
    def __init__(self):
        super().__init__("compressed_image_pub")
        self.create_timer(1/30, self.img_gen_callback)
        cv2.namedWindow("camera")
        self.img = np.zeros((300, 300), dtype=np.uint8)
        self.brightness = 0
        self.pub = self.create_publisher(CompressedImage, "image_raw/compressed", 10)  # 토픽 생성
        self.bridge = CvBridge()


    def img_gen_callback(self):
        self.brightness += 1
        self.img.fill(self.brightness)
        cv2.imshow("camera", self.img)
        if self.brightness > 255:
            self.brightness = 0
        key = cv2.waitKey(3)  # 처리 기간이 필요 milliseconse
        success, encoded_img = cv2.imencode(".jpg", self.img, (cv2.IMWRITE_JPEG_QUALITY, 25))  # jpg로 저장
        if success:
            compressed_msg = CompressedImage()
            compressed_msg.header.stamp = self.get_clock().now().to_msg()
            compressed_msg.header.frame_id = "test img"
            compressed_msg.format = "jpeg"
            compressed_msg.data = encoded_img.tobytes()
            self.pub.publish(compressed_msg)
        else:
            self.get_logger().info("압축실패")
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
        cv2.destroyAllWindows()
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == "__main__":
    main()