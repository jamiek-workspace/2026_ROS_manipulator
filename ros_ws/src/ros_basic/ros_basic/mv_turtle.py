import rclpy
import math
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Color, Pose


class Move_turtle(Node):
    def __init__(self):
        super().__init__('message_pub')

        self.create_timer(0.1, self.timer_callback)
        self.pub = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.create_subscription(Pose, 'turtle1/pose', self.pose_callback, 10)  
        self.create_subscription(Color, 'turtle1/color_sensor', self.color_callback, 10)
        self.count = 0.0
        self.pose = Pose()
        self.color = Color()

        self.state = "forward"
        self.step = 0


    def timer_callback(self):
        msg = Twist()

        if self.state == "forward":
            msg.linear.x = 2.0
            msg.angular.z = 0.0

            self.step += 1
            if self.step > 30:
                self.state = "turn"
                self.step = 0

        elif self.state == "turn":
            msg.linear.x = 0.0
            msg.angular.z = 2.5

            self.step += 1
            if self.step > 10:
                self.state = "forward"
                self.step = 0

        self.pub.publish(msg)

    def pose_callback(self, msg: Pose):
        self.pose = msg

    def color_callback(self, msg: Color):
        self.color = msg


def main(args=None):
    rclpy.init(args=args)

    node = Move_turtle()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Node stopped by user.')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()