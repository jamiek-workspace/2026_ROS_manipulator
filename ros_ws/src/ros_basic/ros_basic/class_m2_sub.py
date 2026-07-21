import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Message2Subscriber(Node):

    def __init__(self):
        super().__init__('m2sub')

        self.subscription = self.create_subscription(
            String,
            'message2',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        self.get_logger().info(
            f'Received message2: {msg.data}'
        )


def main(args=None):
    rclpy.init(args=args)

    node = Message2Subscriber()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()