import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Header


class MessageTimeSubscriber(Node):

    def __init__(self):
        super().__init__('mtsub')

        self.message_subscription = self.create_subscription(
            String,
            'message3',
            self.message_callback,
            10
        )

        self.time_subscription = self.create_subscription(
            Header,
            'time',
            self.time_callback,
            10
        )

    def message_callback(self, msg):
        self.get_logger().info(
            f'Received message3: {msg.data}'
        )

    def time_callback(self, msg):
        self.get_logger().info(
            f'Received time: '
            f'{msg.stamp.sec}.{msg.stamp.nanosec:09d}'
        )


def main(args=None):
    rclpy.init(args=args)

    node = MessageTimeSubscriber()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()