import rclpy
from rclpy.node import Node

def timer_callback():
    print("Hello, ROS 2 World!")


def main(args=None):
    rclpy.init(args=args) # rmw on
    node = Node("message_pub") # node name
    try:
        rclpy.spin(node) # block(loop)
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
    finally:
        node.destroy_node()
        print("Hello, ROS 2 World!")

if __name__ == '__main__':
    main()
