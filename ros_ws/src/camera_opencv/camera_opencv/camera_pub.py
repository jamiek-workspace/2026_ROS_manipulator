# camera를 ros에서 발행

import cv2
import rclpy
from cv_bridge import CvBridge
from rclpy.node import Node
from sensor_msgs.msg import CameraInfo, Image


class Camera_pub(Node):
    def __init__(self):
        super().__init__("camera_pub")
        self.create_timer(1 / 30, self.img_gen_callback)
        cv2.namedWindow("camera")
        self.pub = self.create_publisher(Image, "camera/image_raw", 10)
        self.pub_info = self.create_publisher(CameraInfo, "camera/camera_info", 10)
        self.brige = CvBridge()
        self.width = 640
        self.height = 480
        pipeline = (
            "v4l2src device=/dev/video0 ! "
            f"image/jpeg,width={self.width},height={self.height},framerate=30/1 ! "
            "jpegdec ! "
            "videoconvert ! "
            "video/x-raw,format=BGR ! "
            "appsink drop=true sync=false"
        )
        self.cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)
        self.camera_info = self.create_camera_info()

    def create_camera_info(self):
        msg = CameraInfo()

        msg.width = self.width
        msg.height = self.height
        msg.distortion_model = "plumb_bob"

        msg.d = [0.0, 0.0, 0.0, 0.0, 0.0]
        fx = 600.0
        fy = 600.0
        cx = self.width / 2.0
        cy = self.height / 2.0
        # K matrix
        msg.k = [fx, 0.0, cx, 0.0, fy, cy, 0.0, 0.0, 1.0]
        # Rectification matrix
        msg.r = [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]
        # Projection matrix
        msg.p = [fx, 0.0, cx, 0.0, 0.0, fy, cy, 0.0, 0.0, 0.0, 1.0, 0.0]
        return msg

    def img_gen_callback(self):
        ret, frame = self.cap.read()
        if not ret:
            return
        # 도형 그리기
        # cv2.rectangle(frame, (10, 10), (self.width - 10, self.height - 10), (230, 126, 173), 3)
        color = (230, 126, 173)
        t = 3
        l = 35

        # 좌상
        cv2.line(frame, (10,10), (10+l,10), color, t)
        cv2.line(frame, (10,10), (10,10+l), color, t)

        # 우상
        cv2.line(frame, (self.width-10,10), (self.width-10-l,10), color, t)
        cv2.line(frame, (self.width-10,10), (self.width-10,10+l), color, t)

        # 좌하
        cv2.line(frame, (10,self.height-10), (10+l,self.height-10), color, t)
        cv2.line(frame, (10,self.height-10), (10,self.height-10-l), color, t)

        # 우하
        cv2.line(frame,
                (self.width-10,self.height-10),
                (self.width-10-l,self.height-10),
                color, t)
        cv2.line(frame,
                (self.width-10,self.height-10),
                (self.width-10,self.height-10-l),
                color, t)


        
        cv2.imshow("Camera", frame)
        key = cv2.waitKey(3)  # 처리 기간이 필요 milliseconse
        img = self.brige.cv2_to_imgmsg(frame, encoding="bgr8")
        now = self.get_clock().now().to_msg()
        img.header.stamp = now
        img.header.frame_id = "camera_link"
        self.camera_info.header.stamp = now
        self.camera_info.header.frame_id = "camera_link"

        self.pub.publish(img)
        self.pub_info.publish(self.camera_info)

        if key == ord("q"):
            raise KeyboardInterrupt


def main(args=None):
    rclpy.init(args=args)  # rmw 활성화
    node = Camera_pub()
    try:
        rclpy.spin(node)  # 블럭 (무한 루프)
    except KeyboardInterrupt:
        print("키보드 인터럽트")
    finally:
        node.cap.release()
        cv2.destroyAllWindows()
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == "__main__":
    main()