import rclpy
from rclpy.node import Node

class M_pub(Node):
    def __init__(self):
        super().__init__("message_pub")
        self.create_timer(1.0, self.timer_callback)
        self.counter = 0

    def timer_callback(self):
        self.counter += 1
        print(f"Hello, ROS 2 World! ({self.counter})")


def main(args=None):
    rclpy.init(args=args) # rmw on
    node = M_pub() # node name
    try:
        rclpy.spin(node) # block(loop)
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
    finally:
        node.destroy_node()
        print("Hello, ROS 2 World!")

if __name__ == '__main__':
    main()
