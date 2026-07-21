import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class M_sub(Node):
    def __init__(self):
        super().__init__('message_sub')

        self.subscription = self.create_subscription(
            String,
            'message',
            self.sub_callback,
            10
        )

    def sub_callback(self, msg: String):
        self.get_logger().info(f'Received message: {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    node = M_sub()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Node stopped by user.')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()