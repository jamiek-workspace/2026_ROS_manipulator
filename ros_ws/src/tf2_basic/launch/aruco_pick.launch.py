#!/usr/bin/env python3
"""Launch the ArUco pick node with OpenManipulator-X MoveIt parameters."""

from pathlib import Path

from launch import LaunchDescription
from launch_ros.actions import Node
from moveit_configs_utils import MoveItConfigsBuilder


def generate_launch_description():
    moveit_config = (
        MoveItConfigsBuilder(
            robot_name="open_manipulator_x",
            package_name="open_manipulator_moveit_config",
        )
        .robot_description_semantic(
            str(
                Path("config")
                / "open_manipulator_x"
                / "open_manipulator_x.srdf"
            )
        )
        .joint_limits(
            str(
                Path("config")
                / "open_manipulator_x"
                / "joint_limits.yaml"
            )
        )
        .trajectory_execution(
            str(
                Path("config")
                / "open_manipulator_x"
                / "moveit_controllers.yaml"
            )
        )
        .robot_description_kinematics(
            str(
                Path("config")
                / "open_manipulator_x"
                / "kinematics.yaml"
            )
        )
        .to_moveit_configs()
    )

    aruco_pick_node = Node(
        package="tf2_basic",
        executable="aruco_pick_node",
        name="aruco_pick_node",
        output="screen",
        parameters=[
            moveit_config.to_dict(),
            {
                "use_sim_time": True,
                "planning_frame": "world",
                "marker_frame": "aruco_marker_0",
                "pre_grasp_offset_z": 0.08,
                "grasp_offset_z": 0.00,
                "lift_distance": 0.10,
                "arm_group": "arm",
                "end_effector_link": "end_effector_link",
                "arm_controller": "arm_controller",
                "auto_start": False,
            },
        ],
    )

    return LaunchDescription(
        [
            aruco_pick_node,
        ]
    )