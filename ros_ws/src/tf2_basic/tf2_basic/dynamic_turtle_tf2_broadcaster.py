# 노드 명령어
# ros2 run tf2_basic dynamic_turtle_tf2_broadcaster
# ros2 run tf2_basic static_turtle_tf2_broadcaster
# ros2 run turtlesim turtlesim_node
# ros2 run turtlesim turtle_teleop_key
# rviz2

import numpy as np
import rclpy
from geometry_msgs.msg import TransformStamped
from rclpy.node import Node
from tf2_ros.transform_broadcaster import TransformBroadcaster
from turtlesim.msg import Pose


def euler_to_quaternion_pure(roll, pitch, yaw):
    cr = np.cos(roll * 0.5)
    sr = np.sin(roll * 0.5)
    cp = np.cos(pitch * 0.5)
    sp = np.sin(pitch * 0.5)
    cy = np.cos(yaw * 0.5)
    sy = np.sin(yaw * 0.5)
    qw = cr * cp * cy + sr * sp * sy
    qx = sr * cp * cy - cr * sp * sy
    qy = cr * sp * cy + sr * cp * sy
    qz = cr * cp * sy - sr * sp * cy

    return qx, qy, qz, qw


class M_pub(Node):
    def __init__(self):
        super().__init__("dynamic_tf")  # 노드 이름
        # timer 등록
        self.transformation = [1.0, 1.0, 0.0, 0.0, 0.0, np.pi / 6]
        self.transformation2 = [1.0, 1.0, 1.0, 0.0, 0.0, -np.pi / 6]
        self.tf_broadcaster = TransformBroadcaster(self)
        self.create_subscription(Pose, "turtle1/pose", self.pose_callback, 10)

    def pose_callback(self, msg: Pose):
        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = "world"  # 중요!!(상위 tf2 명시)
        t.child_frame_id = "turtle1"
        x, y, z, w = euler_to_quaternion_pure(0.0, 0.0, msg.theta)
        t.transform.translation.x = msg.x
        t.transform.translation.y = msg.y
        t.transform.translation.z = 0.0
        t.transform.rotation.x = x
        t.transform.rotation.y = y
        t.transform.rotation.z = z
        t.transform.rotation.w = w
        self.tf_broadcaster.sendTransform(t)


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