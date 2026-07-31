import os
import sys

import rclpy
from moveit.core.kinematic_constraints import construct_joint_constraint
from moveit.core.robot_state import RobotState
from moveit.planning import MoveItPy
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup
from rclpy.executors import MultiThreadedExecutor
from rclpy.node import Node
from std_srvs.srv import Empty


class OpenManipulatorMoveItNode(Node):
    def __init__(self):
        super().__init__("open_manipulator_controller")

        self.moveit = MoveItPy(node_name="open_manipulator_moveit_py")
        self.arm = self.moveit.get_planning_component("arm")
        self.gripper = self.moveit.get_planning_component("gripper")

        self.arm_robot_state1 = {
            "joint1": -1.724194,
            "joint2": -0.289922,
            "joint3": 0.136524,
            "joint4": 0.633534,
        }

        # 서비스 요청은 한 번에 하나씩 실행
        self.service_group = MutuallyExclusiveCallbackGroup()

        # 서비스 실행 중에도 timer가 실행되도록 별도 callback group 사용
        self.timer_group = MutuallyExclusiveCallbackGroup()

        self.service = self.create_service(
            Empty,
            "move_manipulator",
            self.move_service_callback,
            callback_group=self.service_group,
        )

        self.timer = self.create_timer(
            0.5,
            self.timer_callback,
            callback_group=self.timer_group,
        )

    def timer_callback(self):
        self.get_logger().info("update!!")

    def move_service_callback(self, request, response):
        self.get_logger().info("Move service started")

        try:
            self.move_manipulator()
            self.get_logger().info("Move service completed")
        except Exception as error:
            self.get_logger().error(f"Move service failed: {error}")

        return response

    def move_manipulator(self):
        for goal_name in (
            "home",
            "init",
            self.arm_robot_state1,
            "my_pose",
            "home",
            "init",
        ):
            self.get_logger().info(f"Arm move: {goal_name}")

            self.plan_and_execute(
                component=self.arm,
                configuration=goal_name,
                controller_name="arm_controller",
            )

        for goal_name in ("open", "close", "open", "close"):
            self.get_logger().info(f"Gripper move: {goal_name}")

            self.plan_and_execute(
                component=self.gripper,
                configuration=goal_name,
                controller_name="gripper_controller",
            )

    def plan_and_execute(
        self,
        component,
        configuration: str | dict[str, float],
        controller_name: str,
    ) -> bool:
        component.set_start_state_to_current_state()

        if isinstance(configuration, str):
            component.set_goal_state(configuration_name=configuration)
        else:
            robot_model = self.moveit.get_robot_model()
            robot_state = RobotState(robot_model)
            robot_state.joint_positions = configuration

            joint_model_group = robot_model.get_joint_model_group("arm")

            joint_constraint = construct_joint_constraint(
                robot_state=robot_state,
                joint_model_group=joint_model_group,
            )

            component.set_goal_state(motion_plan_constraints=[joint_constraint])

        plan_result = component.plan()

        if not plan_result:
            self.get_logger().error(f"Planning failed: {configuration}")
            return False

        self.moveit.execute(
            plan_result.trajectory,
            controllers=[controller_name],
        )

        return True


def main():
    rclpy.init()

    node = OpenManipulatorMoveItNode()

    # 서비스 동작과 timer 동작을 동시에 처리
    executor = MultiThreadedExecutor(num_threads=2)
    executor.add_node(node)

    try:
        executor.spin()
    except KeyboardInterrupt:
        pass
    finally:
        executor.shutdown()
        node.destroy_node()
        rclpy.try_shutdown()

        sys.stdout.flush()
        sys.stderr.flush()
        os._exit(0)


if __name__ == "__main__":
    main()