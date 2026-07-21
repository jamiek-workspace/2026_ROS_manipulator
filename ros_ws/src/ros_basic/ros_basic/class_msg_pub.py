import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class MessagePublisher(Node):

    def __init__(self):
        super().__init__('message_pub')

        self.message1_pub = self.create_publisher(
            String,
            'message1',
            10
        )

        self.message2_pub = self.create_publisher(
            String,
            'message2',
            10
        )

        self.message3_pub = self.create_publisher(
            String,
            'message3',
            10
        )

        self.timer = self.create_timer(1.0, self.timer_callback)
        self.count = 0

    def timer_callback(self):
        msg1 = String()
        msg2 = String()
        msg3 = String()

        msg1.data = f'Message 1: {self.count}'
        msg2.data = f'Message 2: {self.count}'
        msg3.data = f'Message 3: {self.count}'

        self.message1_pub.publish(msg1)
        self.message2_pub.publish(msg2)
        self.message3_pub.publish(msg3)

        self.get_logger().info(
            f'Published: {msg1.data}, {msg2.data}, {msg3.data}'
        )

        self.count += 1


def main(args=None):
    rclpy.init(args=args)

    node = MessagePublisher()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()