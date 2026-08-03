# ros2 topic bw /image_raw/compressed

import cv2
import rclpy
from cv_bridge import CvBridge
from rclpy.node import Node
from sensor_msgs.msg import CompressedImage


class Compressed_image_sub(Node):
    def __init__(self):
        super().__init__("compressed_image_sub")
        cv2.namedWindow("camera")
        self.create_subscription(CompressedImage, "image_raw/compressed", self.image_callback, 10)
        self.brige = CvBridge()

    def image_callback(self, msg: CompressedImage):
        img = self.brige.compressed_imgmsg_to_cv2(msg)
        cv2.imshow("camera", img)
        key = cv2.waitKey(3)
        if key == ord("q"):
            raise KeyboardInterrupt


def main(args=None):
    rclpy.init(args=args)  # rmw 활성화
    node = Compressed_image_sub()
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