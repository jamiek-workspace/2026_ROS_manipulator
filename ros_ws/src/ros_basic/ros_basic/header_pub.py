import rclpy
from rclpy.node import Node
from std_msgs.msg import Header


class M_pub(Node):
    def __init__(self):
        super().__init__('header_pub')

        self.create_timer(10, self.timer_callback)
        self.pub = self.create_publisher(Header, "message", 10)

    def timer_callback(self):
        msg = Header()
        msg.frame_id = "time test"
        msg.stamp = self.get_clock().now().to_msg()
        self.pub.publish(msg)



def main(args=None):
    rclpy.init(args=args)

    node = M_pub()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Node stopped by user.')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()