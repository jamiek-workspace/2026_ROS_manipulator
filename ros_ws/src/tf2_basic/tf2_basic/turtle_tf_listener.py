# ros2 run turtlesim turtlesim_node
# rviz2
# ros2 run tf2_basic dynamic_turtle_tf2_broadcaster
# ros2 run tf2_basic tf_listener
# ros2 run turtlesim turtle_teleop_key
# sudo apt install ros-jazzy-rqt-tf-tree
# ros2 run rqt_tf_tree rqt_tf_tree --force-discover
# 예외 처리 TransformException

# 과제: turtlesim을 따라가는 두번째 turtle2를 생성
# turtle spawn은 service 코드 쓰기
# timer는 1.0 간격으로 회전과 정지, 직진을 tf look-up 정보로 구현
# turtle1 turtle2 tf 모두 발행

# 실행 순서
# ros2 run turtlesim turtlesim_node
# ros2 run tf2_basic dynamic_turtle_tf2_broadcaster
# ros2 run tf2_basic turtle_tf_listener
# ros2 run turtlesim turtle_teleop_key

import math

import rclpy
from geometry_msgs.msg import TransformStamped, Twist
from rclpy.node import Node
from rclpy.time import Time
from tf2_ros import Buffer, TransformBroadcaster, TransformException
from tf2_ros import TransformListener
from turtlesim.msg import Pose
from turtlesim.srv import Spawn


def yaw_to_quaternion(yaw):
    """
    turtlesim은 평면 운동만 하므로 yaw(theta)만 Quaternion으로 변환한다.
    """
    return (
        0.0,
        0.0,
        math.sin(yaw / 2.0),
        math.cos(yaw / 2.0),
    )


class TurtleTfListener(Node):

    def __init__(self):
        super().__init__("turtle_tf_listener")

        # turtle2 생성 여부
        self.turtle2_spawned = False

        # timer 동작 상태
        # rotate -> stop -> forward -> rotate ...
        self.motion_state = "rotate"

        # 최근 TF 정보 저장
        self.distance = 0.0
        self.angle_error = 0.0

        # turtle2 속도 발행
        self.cmd_pub = self.create_publisher(
            Twist,
            "/turtle2/cmd_vel",
            10,
        )

        # turtle2의 위치를 TF로 발행하기 위한 broadcaster
        self.tf_broadcaster = TransformBroadcaster(self)

        # turtle2 pose 구독
        self.create_subscription(
            Pose,
            "/turtle2/pose",
            self.turtle2_pose_callback,
            10,
        )

        # TF listener
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(
            self.tf_buffer,
            self,
        )

        # turtlesim의 spawn 서비스 클라이언트
        self.spawn_client = self.create_client(
            Spawn,
            "/spawn",
        )

        # turtle2 생성 요청
        self.spawn_turtle2()

        # 1초마다 회전, 정지, 직진 동작
        self.timer = self.create_timer(
            1.0,
            self.timer_callback,
        )

    def spawn_turtle2(self):
        """
        turtlesim의 /spawn 서비스를 이용해 turtle2를 생성한다.
        """
        while not self.spawn_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("/spawn 서비스를 기다리는 중입니다.")

        request = Spawn.Request()

        request.x = 2.0
        request.y = 2.0
        request.theta = 0.0
        request.name = "turtle2"

        future = self.spawn_client.call_async(request)
        future.add_done_callback(self.spawn_callback)

    def spawn_callback(self, future):
        """
        turtle2 생성 서비스 응답 처리
        """
        try:
            response = future.result()

            self.turtle2_spawned = True

            self.get_logger().info(
                f"{response.name} 생성 완료"
            )

        except Exception as error:
            self.get_logger().error(
                f"turtle2 생성 실패: {error}"
            )

    def turtle2_pose_callback(self, msg: Pose):
        """
        turtle2의 현재 위치를 world -> turtle2 TF로 발행한다.
        """
        if not self.turtle2_spawned:
            return

        transform = TransformStamped()

        transform.header.stamp = self.get_clock().now().to_msg()
        transform.header.frame_id = "world"
        transform.child_frame_id = "turtle2"

        transform.transform.translation.x = msg.x
        transform.transform.translation.y = msg.y
        transform.transform.translation.z = 0.0

        qx, qy, qz, qw = yaw_to_quaternion(msg.theta)

        transform.transform.rotation.x = qx
        transform.transform.rotation.y = qy
        transform.transform.rotation.z = qz
        transform.transform.rotation.w = qw

        self.tf_broadcaster.sendTransform(transform)

    def lookup_turtle_transform(self):
        """
        turtle2 좌표계에서 turtle1의 상대 위치를 조회한다.

        반환되는 translation:
        x: turtle2의 앞쪽 기준 turtle1의 거리
        y: turtle2의 왼쪽 기준 turtle1의 거리
        """
        try:
            transform = self.tf_buffer.lookup_transform(
                "turtle2",   # target frame
                "turtle1",   # source frame
                Time(),
            )

            relative_x = transform.transform.translation.x
            relative_y = transform.transform.translation.y

            self.distance = math.sqrt(
                relative_x ** 2 + relative_y ** 2
            )

            self.angle_error = math.atan2(
                relative_y,
                relative_x,
            )

            return True

        except TransformException as error:
            self.get_logger().warning(
                f"TF 조회 실패: {error}"
            )
            return False

    def timer_callback(self):
        if not self.turtle2_spawned:
            return

        if not self.lookup_turtle_transform():
            return

        # turtle1에 충분히 가까우면 정지
        if self.distance <= 1.0:
            cmd = Twist()
            self.cmd_pub.publish(cmd)

            self.motion_state = "rotate"

            self.get_logger().info(
                f"[도착·정지] 거리={self.distance:.2f}"
            )
            return

        cmd = Twist()

        if self.motion_state == "rotate":
            cmd.linear.x = 0.0

            # 너무 작은 각도 오차에는 반응하지 않음
            if abs(self.angle_error) > 0.1:
                cmd.angular.z = max(
                    min(0.8 * self.angle_error, 0.8),
                    -0.8,
                )
            else:
                cmd.angular.z = 0.0

            self.get_logger().info(
                f"[회전] 각도 오차="
                f"{math.degrees(self.angle_error):.2f}도"
            )

            self.motion_state = "stop"

        elif self.motion_state == "stop":
            cmd.linear.x = 0.0
            cmd.angular.z = 0.0

            self.get_logger().info("[정지]")

            self.motion_state = "forward"

        elif self.motion_state == "forward":
            # 가까워질수록 속도를 낮춤
            cmd.linear.x = min(
                0.5 * (self.distance - 1.0),
                0.8,
            )
            cmd.angular.z = 0.0

            self.get_logger().info(
                f"[직진] 거리={self.distance:.2f}, "
                f"속도={cmd.linear.x:.2f}"
            )

            self.motion_state = "rotate"

        self.cmd_pub.publish(cmd)


def main(args=None):
    rclpy.init(args=args)

    node = TurtleTfListener()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        node.get_logger().info("키보드 인터럽트")

    finally:
        # 종료 전에 turtle2 정지
        stop_msg = Twist()
        node.cmd_pub.publish(stop_msg)

        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()