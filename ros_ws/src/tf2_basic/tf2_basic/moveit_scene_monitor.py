"""MoveItPy로 OpenManipulator-X의 arm과 gripper를 제어한다."""

import os
import sys

import rclpy
from geometry_msgs.msg import Pose
from moveit.core.kinematic_constraints import construct_joint_constraint
from moveit.core.robot_state import RobotState
from moveit.planning import MoveItPy
from moveit_msgs.msg import CollisionObject
from rclpy.node import Node
from shape_msgs.msg import SolidPrimitive


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
        self.planning_scene_monitor = self.moveit.get_planning_scene_monitor()
        self.add_table()
        self.add_wall()
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

    def add_table(self):
        collision_object = CollisionObject()
        collision_object.header.frame_id = "world"
        collision_object.id = "table"

        table = SolidPrimitive()
        table.type = SolidPrimitive.BOX
        table.dimensions = [0.8, 0.8, 0.05]  # x, y, z , --m 단위

        table_pose = Pose()
        table_pose.position.x = 0.25
        table_pose.position.y = 0.0
        table_pose.position.z = -0.025

        table_pose.orientation.x = 0.0
        table_pose.orientation.y = 0.0
        table_pose.orientation.z = 0.0
        table_pose.orientation.w = 1.0

        collision_object.primitives.append(table)  # type: ignore
        collision_object.primitive_poses.append(table_pose)  # type: ignore
        collision_object.operation = CollisionObject.ADD

        success = self.planning_scene_monitor.process_collision_object(collision_object)

        if success:
            self.get_logger().info("table을 추가 했습니다")

        with self.planning_scene_monitor.read_only() as scene:
            scene_msg = scene.planning_scene_message

            self.get_logger().info(f"planning frame: {scene.planning_frame}")

            for obj in scene_msg.world.collision_objects:
                self.get_logger().info(
                    f"collision object: id={obj.id}, frame={obj.header.frame_id}"
                )

    def add_wall(self):
        collision_object = CollisionObject()
        collision_object.header.frame_id = "world"
        collision_object.id = "wall"

        wall = SolidPrimitive()
        wall.type = SolidPrimitive.BOX
        wall.dimensions = [0.4, 0.02, 0.3]  # x, y, z , --m 단위

        wall_pose = Pose()
        wall_pose.position.x = 0.3
        wall_pose.position.y = 0.0
        wall_pose.position.z = 0.0

        wall_pose.orientation.x = 0.0
        wall_pose.orientation.y = 0.0
        wall_pose.orientation.z = 0.0
        wall_pose.orientation.w = 1.0

        collision_object.primitives.append(wall)  # type: ignore
        collision_object.primitive_poses.append(wall_pose)  # type: ignore
        collision_object.operation = CollisionObject.ADD

        success = self.planning_scene_monitor.process_collision_object(collision_object)

        if success:
            self.get_logger().info("wall을 추가 했습니다")

        with self.planning_scene_monitor.read_only() as scene:
            scene_msg = scene.planning_scene_message

            self.get_logger().info(f"planning frame: {scene.planning_frame}")

            for obj in scene_msg.world.collision_objects:
                self.get_logger().info(
                    f"collision object: id={obj.id}, frame={obj.header.frame_id}"
                )


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