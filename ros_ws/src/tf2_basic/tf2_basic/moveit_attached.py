
"""MoveItPy로 OpenManipulator-X의 arm과 gripper를 제어한다."""

import os
import sys

import rclpy
from geometry_msgs.msg import Pose
from moveit.core.kinematic_constraints import construct_joint_constraint
from moveit.core.robot_state import RobotState
from moveit.planning import MoveItPy
from moveit_msgs.msg import AttachedCollisionObject, CollisionObject
from rclpy.node import Node
from shape_msgs.msg import SolidPrimitive


class OpenManipulatorMoveItNode(Node):
    def __init__(self):
        super().__init__("open_manipulator_controller")
        self.moveit = MoveItPy(node_name="open_manipulator_moveit_py")
        self.arm = self.moveit.get_planning_component("arm")
        self.gripper = self.moveit.get_planning_component("gripper")
        self.planning_scene_monitor = self.moveit.get_planning_scene_monitor()
        self.object_id = "grasped_box"
        self.attach_link = "end_effector_link"
        self.touch_links = [
            "link5",
            "end_effector_link",
            "gripper_left_link",
            "gripper_right_link",
        ]

        self.move_manipulator()

    def move_manipulator(self):
        self.add_pick_object()
        # 초기 자세
        self.plan_and_execute(
            self.moveit,
            self.arm,
            configuration="init",
            controller_name="arm_controller",
        )
        # 물체 집기 직전 자세 1
        #  1.0691846091560846
        # - 0.24850488763726686
        # - 0.6212622190934778
        # - -0.8682331259434797
        self.plan_and_execute(
            self.moveit,
            self.arm,
            configuration={
                "joint1": 1.0691846091560846,
                "joint2": 0.24850488763726686,
                "joint3": 0.6212622190934778,
                "joint4": -0.8682331259434797,
            },
            controller_name="arm_controller",
        )
        # 그리퍼 열기
        self.add_table()
        self.add_wall()
        self.plan_and_execute(
            self.moveit,
            self.gripper,
            configuration="open",
            controller_name="gripper_controller",
        )
        # 물체 집기 직전 자세 2
        self.plan_and_execute(
            self.moveit,
            self.arm,
            configuration={
                "joint1": 1.0691846091560846,
                "joint2": 0.24850488763726686,
                "joint3": 0.6212622190934778,
                "joint4": -0.8682331259434797,
            },
            controller_name="arm_controller",
        )
        # 그리퍼 닫기
        self.plan_and_execute(
            self.moveit,
            self.gripper,
            configuration="close",
            controller_name="gripper_controller",
        )
        # 물체를 로봇 부착
        self.attach_object()
        # 물체를 든 상태로 이동 ( 회피 plane)
        # -0.9725438195197036
        # - 0.44485442848662915
        # - 0.3666214083044612
        # - -0.8406214717615383
        self.plan_and_execute(
            self.moveit,
            self.arm,
            configuration={
                "joint1": -0.9725438195197036,
                "joint2": 0.44485442848662915,
                "joint3": 0.3666214083044612,
                "joint4": -0.8406214717615383,
            },
            controller_name="arm_controller",
        )
        # 그리퍼 열기
        self.plan_and_execute(
            self.moveit,
            self.gripper,
            configuration="open",
            controller_name="gripper_controller",
        )
        # attached object 제거
        self.detach_object()
        # world에 box 다시 추가
        self.add_pick_object()
        self.add_placed_object(0.2, -0.2, 0.065)
        # 초기 위치 이동
        self.plan_and_execute(
            self.moveit,
            self.arm,
            configuration="init",
            controller_name="arm_controller",
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
        table_pose.position.z = -0.05

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
        wall.dimensions = [0.4, 0.02, 0.2]  # x, y, z , --m 단위

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

    def add_pick_object(self):
        collision_object = CollisionObject()
        collision_object.header.frame_id = "world"
        collision_object.header.stamp = self.get_clock().now().to_msg()
        collision_object.id = self.object_id

        box = SolidPrimitive()
        box.type = SolidPrimitive.BOX
        box.dimensions = [0.04, 0.04, 0.08]

        box_pose = Pose()
        box_pose.position.x = 0.20
        box_pose.position.y = 0.20
        box_pose.position.z = 0.065
        box_pose.orientation.w = 1.0

        collision_object.primitives.append(box)  # type: ignore
        collision_object.primitive_poses.append(box_pose)  # type: ignore
        collision_object.operation = CollisionObject.ADD

        success = self.planning_scene_monitor.process_collision_object(collision_object)
        if success:
            self.get_logger().info("world 에 box 추가")
        return success

    def attach_object(self):
        if not self.remove_world_object(self.object_id):
            return False
        attached_object = AttachedCollisionObject()

        attached_object.link_name = self.attach_link
        attached_object.object.id = self.object_id
        attached_object.object.header.frame_id = self.attach_link
        attached_object.object.header.stamp = self.get_clock().now().to_msg()

        box = SolidPrimitive()
        box.type = SolidPrimitive.BOX
        box.dimensions = [0.04, 0.04, 0.08]

        box_pose = Pose()
        box_pose.position.x = 0.02
        box_pose.position.y = 0.0
        box_pose.position.z = 0.0
        box_pose.orientation.w = 1.0

        attached_object.object.primitives.append(box)  # type: ignore
        attached_object.object.primitive_poses.append(box_pose)  # type: ignore
        attached_object.object.operation = CollisionObject.ADD

        attached_object.touch_links = self.touch_links

        with self.planning_scene_monitor.read_write() as scene:
            success = scene.process_attached_collision_object(attached_object)
            scene.current_state.update()

        if success:
            self.get_logger().info("부착 성공!!")
        return success

    def remove_world_object(self, object_id: str):
        remove_object = CollisionObject()
        remove_object.header.frame_id = "world"
        remove_object.header.stamp = self.get_clock().now().to_msg()
        remove_object.id = self.object_id
        remove_object.operation = CollisionObject.REMOVE

        success = self.planning_scene_monitor.process_collision_object(remove_object)
        if success:
            self.get_logger().info("world 에서 box 제거")
        return success

    def detach_object(self):
        attached_object = AttachedCollisionObject()

        attached_object.link_name = self.attach_link
        attached_object.object.id = self.object_id
        attached_object.object.header.frame_id = self.attach_link
        attached_object.object.header.stamp = self.get_clock().now().to_msg()
        attached_object.object.operation = CollisionObject.REMOVE

        with self.planning_scene_monitor.read_write() as scene:
            success = scene.process_attached_collision_object(attached_object)
            scene.current_state.update()

        if success:
            self.get_logger().info("분리 성공!!")
        return success

    def add_placed_object(self, x, y, z):
        collision_object = CollisionObject()
        collision_object.header.frame_id = "world"
        collision_object.header.stamp = self.get_clock().now().to_msg()
        collision_object.id = self.object_id

        box = SolidPrimitive()
        box.type = SolidPrimitive.BOX
        box.dimensions = [0.04, 0.04, 0.08]

        box_pose = Pose()
        box_pose.position.x = x
        box_pose.position.y = y
        box_pose.position.z = z
        box_pose.orientation.w = 1.0

        collision_object.primitives.append(box)  # type: ignore
        collision_object.primitive_poses.append(box_pose)  # type: ignore
        collision_object.operation = CollisionObject.ADD

        success = self.planning_scene_monitor.process_collision_object(collision_object)
        if success:
            self.get_logger().info("world 에 내려 놓은 box 추가")
        return success


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
