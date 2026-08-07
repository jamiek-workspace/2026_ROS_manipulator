# install 의 ros2 실행 파일을 수정한다.
# /home/aa/gong_manipulator_20206/gong_ws/install/camera_opencv/lib/camera_opencv/camera_yolo
# 1번라인의 셔뱅에 실행 파일 python3.12 를 가상 환경의 실행 파일로 교체 한다.
# #!/home/aa/gong_manipulator_20206/perception_envs/depth_yolo/.venv/bin/python3.12

import cv2
import rclpy
import torch
from cv_bridge import CvBridge
from rclpy.node import Node
from sensor_msgs.msg import CameraInfo, Image
from ultralytics import YOLO


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
        self.cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.cap.set(cv2.CAP_PROP_FPS, 30)
        self.cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
        self.camera_info = self.create_camera_info()
        self.get_logger().info(f"{torch.cuda.is_available()}")
        self.model = YOLO("yolo26n.pt")

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
        results = self.model.predict(frame, stream=False, verbose=False)
        frame = results[0].plot()  # type: ignore
        cv2.imshow("Camera", frame)
        key = cv2.waitKey(3)  # 처리 기간이 필요 milliseconse
        img = self.brige.cv2_to_imgmsg(frame)
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