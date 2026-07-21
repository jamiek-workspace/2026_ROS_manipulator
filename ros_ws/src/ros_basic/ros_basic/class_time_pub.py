import rclpy
from rclpy.node import Node
from std_msgs.msg import Header


class TimePublisher(Node):

    def __init__(self):
        super().__init__('time_pub')

        self.publisher = self.create_publisher(
            Header,
            'time',
            10
        )

        self.timer = self.create_timer(
            1.0,
            self.timer_callback
        )

    def timer_callback(self):
        msg = Header()
        msg.stamp = self.get_clock().now().to_msg()
        msg.frame_id = 'time_pub'

        self.publisher.publish(msg)

        self.get_logger().info(
            f'Published time: '
            f'{msg.stamp.sec}.{msg.stamp.nanosec:09d}'
        )


def main(args=None):
    rclpy.init(args=args)

    node = TimePublisher()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()