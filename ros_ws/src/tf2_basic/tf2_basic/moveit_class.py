"""MoveItPy로 OpenManipulator-X의 arm과 gripper를 제어한다."""

import os
import sys

import rclpy
from moveit.planning import MoveItPy
from rclpy.node import Node


class OpenManipulatorMoveItNode(Node):
    def __init__(self):
        super().__init__("open_manipulator_controller")
        self.moveit = MoveItPy(node_name="open_manipulator_moveit_py")
        self.arm = self.moveit.get_planning_component("arm")
        self.gripper = self.moveit.get_planning_component("gripper")
        self.move_manipulator()

    def move_manipulator(self):
        for goal_name in ("home", "init", "home", "init"):
            self.get_logger().info("joint move!!!")
            self.plan_and_execute(
                self.moveit,
                self.arm,
                configuration_name=goal_name,
                controller_name="arm_controller",
            )
        for goal_name in ("open", "close", "open", "close"):
            self.get_logger().info("gripper move!!!")
            self.plan_and_execute(
                self.moveit,
                self.gripper,
                configuration_name=goal_name,
                controller_name="gripper_controller",
            )

    def plan_and_execute(
        self,
        moveit: MoveItPy,
        component,
        configuration_name: str,
        controller_name: str,
    ) -> bool:
        """Named state까지 경로를 계획하고 실행한다."""
        component.set_start_state_to_current_state()
        component.set_goal_state(configuration_name=configuration_name)

        plan_result = component.plan()

        moveit.execute(
            plan_result.trajectory,
            controllers=[controller_name],
        )
        return True


def main() -> None:
    rclpy.init()

    node = OpenManipulatorMoveItNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()
        rclpy.try_shutdown()
        sys.stdout.flush()
        sys.stderr.flush()
        os._exit(0)


if __name__ == "__main__":
    main()