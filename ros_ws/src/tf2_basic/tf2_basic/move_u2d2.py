# 팔을 추가해서 엘보우 구현(타입은 revolute로 구현)(다리는 고정이므로 다리 위에 팔을 추가하는 등.)
# 05_add_arm.urdf
# 실행 ros2 launch tf2_basic urdf_display.launch.py model:=urdf/04_physics.urdf gui:=true
# tf를 발행해서 머리를 돌리거나, 막대기를 꺼내거나, 바퀴를 굴려보세요. 재미있게 동작하게
# ros2 run tf2_basic move_u2d2로 움직이기

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState


class MoveU2D2(Node):

    def __init__(self):
        super().__init__('move_u2d2')

        self.joint_state_pub = self.create_publisher(
            JointState,
            '/joint_states',
            10
        )

        self.timer = self.create_timer(0.05, self.timer_callback)

        self.elbow_position = 0.0
        self.direction = 1.0

        self.get_logger().info('move_u2d2 node started')

    def timer_callback(self):
        # 팔꿈치 각도 변경
        self.elbow_position += self.direction * 0.02

        if self.elbow_position >= 2.0:
            self.elbow_position = 2.0
            self.direction = -1.0

        elif self.elbow_position <= 0.0:
            self.elbow_position = 0.0
            self.direction = 1.0

        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()

        # 05_add_arm.urdf의 모든 non-fixed joint
        msg.name = [
            'right_front_wheel_joint',
            'right_back_wheel_joint',
            'left_front_wheel_joint',
            'left_back_wheel_joint',
            'gripper_extension',
            'left_gripper_joint',
            'right_gripper_joint',
            'head_swivel',
            'right_elbow_joint',
        ]

        # 움직이지 않는 조인트는 0.0으로 유지
        msg.position = [
            0.0,                    # right_front_wheel_joint
            0.0,                    # right_back_wheel_joint
            0.0,                    # left_front_wheel_joint
            0.0,                    # left_back_wheel_joint
            0.0,                    # gripper_extension
            0.0,                    # left_gripper_joint
            0.0,                    # right_gripper_joint
            0.0,                    # head_swivel
            self.elbow_position,    # right_elbow_joint
        ]

        self.joint_state_pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    node = MoveU2D2()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
