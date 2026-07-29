"""MoveItPy로 OpenManipulator-X의 arm과 gripper를 제어한다."""

import os
import sys

import rclpy
from moveit.core.kinematic_constraints import construct_joint_constraint
from moveit.core.robot_state import RobotState
from moveit.planning import MoveItPy
from rclpy.node import Node


class OpenManipulatorMoveItNode(Node):
    def __init__(self):
        super().__init__("open_manipulator_controller")
        self.moveit = MoveItPy(node_name="open_manipulator_moveit_py")
        self.arm = self.moveit.get_planning_component("arm")
        self.gripper = self.moveit.get_planning_component("gripper")
        self.arm_robot_state1 = {
            "joint1": -0.021476,
            "joint2": -0.762388,
            "joint3": 0.598253,
            "joint4": 1.061515,
        }
        self.move_manipulator()

    def move_manipulator(self):
        for goal_name in ("home", "init", self.arm_robot_state1, "my_pose", "home", "init"):
            self.get_logger().info("joint move!!!")
            self.plan_and_execute(
                self.moveit,
                self.arm,
                configuration=goal_name,
                controller_name="arm_controller",
            )
        for goal_name in ("open", "close", "open", "close"):
            self.get_logger().info("gripper move!!!")
            self.plan_and_execute(
                self.moveit,
                self.gripper,
                configuration=goal_name,
                controller_name="gripper_controller",
            )

    def plan_and_execute(
        self,
        moveit: MoveItPy,
        component,
        configuration: str | dict[str, float],
        controller_name: str,
    ) -> bool:
        """Named state까지 경로를 계획하고 실행한다."""
        component.set_start_state_to_current_state()
        if issubclass(type(configuration), str):
            component.set_goal_state(configuration_name=configuration)
        else:
            robot_model = self.moveit.get_robot_model()
            robot_state = RobotState(robot_model)
            robot_state.joint_positions = configuration
            joint_model_group = robot_model.get_joint_model_group("arm")
            joint_constraint = construct_joint_constraint(
                robot_state=robot_state, joint_model_group=joint_model_group
            )
            component.set_goal_state(motion_plan_constraints=[joint_constraint])

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
        # todo : moveitpy shutdown 작동 되는지 확인하고 수정하기
        sys.stdout.flush()
        sys.stderr.flush()
        os._exit(0)


if __name__ == "__main__":
    main()