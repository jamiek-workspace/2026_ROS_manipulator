import rclpy
from action_msgs.msg import GoalStatus
from control_msgs.action import (
    FollowJointTrajectory,
    FollowJointTrajectory_GetResult_Response,
    GripperCommand,
    GripperCommand_GetResult_Response,
)
from rclpy.action import ActionClient
from rclpy.node import Node
from rclpy.task import Future
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectoryPoint


class Manipulator_pub(Node):
    def __init__(self):
        super().__init__("manipulator_pub")  # 노드 이름
        # timer 등록
        self.create_timer(1.5, self.timer_callback)
        self.joint_client = ActionClient(
            self, FollowJointTrajectory, "/arm_controller/follow_joint_trajectory"
        )
        self.gripper_client = ActionClient(self, GripperCommand, "/gripper_controller/gripper_cmd")
        self.joint_state_subscription = self.create_subscription(
            JointState, "joint_states", self.joint_callback, 10
        )
        self.current_joint_position = [0.0, 0.0, 0.0, 0.0]
        self.current_gripper_position = 0.0
        self.joint_state_received = False
        self.count = True
        self.duration_sec = 1

    def timer_callback(self):
        point = JointTrajectoryPoint()
        seconds = int(self.duration_sec)
        nanoseconds = int((self.duration_sec - seconds) * 1_000_000_000)
        point.time_from_start.sec = seconds
        point.time_from_start.nanosec = nanoseconds
        if self.count:
            point.positions = [
                0.8995922516973869,
                -0.5832234352774157,
                -0.26300971181849175,
                -0.6258641614575486,
            ]
            self.move_gripper(0.019)
            self.count = False
        else:
            point.positions = [
                0.4795922516973865,
                -0.883223435277416,
                0.3969902881815083,
                0.8941358385424522,
            ]
            self.move_gripper(-0.01)
            self.count = True
        self.move_joint(point)

    def joint_callback(self, msg: JointState):
        self.current_joint_position = msg.position

    def move_gripper(self, position: float, max_effort=10.0, timeout_sec=5.0):
        if not self.gripper_client.wait_for_server(timeout_sec=timeout_sec):
            self.get_logger().info("gripper_controller Action 서버를 찾지 못햇습니다.")
        goal = GripperCommand.Goal()
        goal.command.position = float(position)
        goal.command.max_effort = float(max_effort)
        send_goal_future = self.gripper_client.send_goal_async(goal)
        send_goal_future.add_done_callback(self.goal_callback)

    def goal_callback(self, future: Future):
        self.goal_handle = future.result()  # type: ignore
        self.get_result_future = self.goal_handle.get_result_async()  # type: ignore
        self.get_result_future.add_done_callback(self.get_result_callback)

    def feedback_callback(
        self,
        msg: GripperCommand.Impl.FeedbackMessage,
    ):
        feedback: GripperCommand.Feedback = msg.feedback
        self.get_logger().info(f"{feedback.position}")

    def get_result_callback(self, future: Future):
        result: GripperCommand_GetResult_Response = (
            future.result()  # type: ignore
        )
        if result.status == GoalStatus.STATUS_SUCCEEDED:
            self.get_logger().info(f"succeeded result: {result.result.position}")
        elif result.status == GoalStatus.STATUS_ABORTED:
            self.get_logger().info("aborted!!")
        elif result.status == GoalStatus.STATUS_CANCELED:
            self.get_logger().info("canceled!!")

    def move_joint(self, point: JointTrajectoryPoint):
        if not self.joint_client.wait_for_server(timeout_sec=1.0):
            self.get_logger().info("joint_controller Action 서버를 찾지 못햇습니다.")
        goal = FollowJointTrajectory.Goal()
        # todo :
        goal.trajectory.header.stamp = self.get_clock().now().to_msg()
        goal.trajectory.header.frame_id = "move_manipulator"
        goal.trajectory.joint_names = ["joint1", "joint2", "joint3", "joint4"]
        goal.trajectory.points.append(point)  # type: ignore

        send_goal_future = self.joint_client.send_goal_async(goal)
        send_goal_future.add_done_callback(self.goal_joint_callback)

    def goal_joint_callback(self, future: Future):
        self.goal_handle = future.result()  # type: ignore
        self.get_result_future = self.goal_handle.get_result_async()  # type: ignore
        self.get_result_future.add_done_callback(self.get_joint_result_callback)

    def feedback_joint_callback(
        self,
        msg: FollowJointTrajectory.Impl.FeedbackMessage,
    ):
        feedback: FollowJointTrajectory.Feedback = msg.feedback
        self.get_logger().info(f"{feedback.actual.positions}")

    def get_joint_result_callback(self, future: Future):
        result: FollowJointTrajectory_GetResult_Response = (
            future.result()  # type: ignore
        )
        if result.status == GoalStatus.STATUS_SUCCEEDED:
            self.get_logger().info(f"succeeded result: {result.result.error_string}")
        elif result.status == GoalStatus.STATUS_ABORTED:
            self.get_logger().info("aborted!!")
        elif result.status == GoalStatus.STATUS_CANCELED:
            self.get_logger().info("canceled!!")


def main(args=None):
    rclpy.init(args=args)  # rmw 활성화
    node = Manipulator_pub()
    try:
        rclpy.spin(node)  # 블럭 (무한 루프)
    except KeyboardInterrupt:
        print("키보드 인터럽트")
    finally:
        node.destroy_node()


if __name__ == "__main__":
    main()