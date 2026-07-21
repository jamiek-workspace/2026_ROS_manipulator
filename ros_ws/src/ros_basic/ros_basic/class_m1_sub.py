import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Message1Subscriber(Node):

    def __init__(self):
        super().__init__('m1sub')

        self.subscription = self.create_subscription(
            String,
            'message1',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        self.get_logger().info(
            f'Received message1: {msg.data}'
        )


def main(args=None):
    rclpy.init(args=args)

    node = Message1Subscriber()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()