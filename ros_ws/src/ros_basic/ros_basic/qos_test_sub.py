import rclpy
from rclpy.node import Node
from rclpy.qos import (
    QoSDurabilityPolicy,
    QoSHistoryPolicy,
    QoSProfile,
    QoSReliabilityPolicy,
    qos_profile_default,
)
from std_msgs.msg import String


class M_sub(Node):
    def __init__(self):
        super().__init__("massage_sub")  # 노드 이름
        # subscription callback 등록
        self.qos_profile = QoSProfile(
            history=QoSHistoryPolicy.KEEP_ALL,
            reliability=QoSReliabilityPolicy.RELIABLE,
            durability=QoSDurabilityPolicy.TRANSIENT_LOCAL,
        )
        self.create_subscription(String, "message", self.sub_callback, self.qos_profile)

    def sub_callback(self, msg: String):
        self.get_logger().info(msg.data)


def main(args=None):
    rclpy.init(args=args)  # rmw 활성화
    node = M_sub()
    try:
        rclpy.spin(node)  # 블럭 (무한 루프)
    except KeyboardInterrupt:
        node.get_logger().info("키보드 인터럽트")
    finally:
        node.destroy_node()


if __name__ == "__main__":
    main()