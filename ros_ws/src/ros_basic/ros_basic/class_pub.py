import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class M_pub(Node):
    def __init__(self):
        super().__init__('message_pub')

        self.pub = self.create_publisher(
            String,
            'message',
            10
        )

        self.count = 0

        self.timer = self.create_timer(
            1.0,
            self.timer_callback
        )

    def timer_callback(self):
        msg = String()
        msg.data = f'Hello, ROS 2 World! {self.count}'

        self.get_logger().info(msg.data)
        self.pub.publish(msg)

        self.count += 1


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