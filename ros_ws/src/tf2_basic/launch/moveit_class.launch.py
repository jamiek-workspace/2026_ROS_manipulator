"""OpenManipulator-X MoveItPy, move_group, RViz 실행 launch."""

from pathlib import Path

import yaml
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def load_yaml(path: Path) -> dict:
    """YAML 파일을 ROS parameter dictionary로 읽는다."""
    with path.open("r", encoding="utf-8") as stream:
        return yaml.safe_load(stream) or {}


def generate_launch_description() -> LaunchDescription:
    moveit_config_share = Path(
        get_package_share_directory(
            "open_manipulator_moveit_config"
        )
    )
    description_share = Path(
        get_package_share_directory(
            "open_manipulator_description"
        )
    )
    moveit_utils_share = Path(
        get_package_share_directory(
            "moveit_configs_utils"
        )
    )

    robot_config_dir = (
        moveit_config_share
        / "config"
        / "open_manipulator_x"
    )

    urdf_xacro = (
        description_share
        / "urdf"
        / "open_manipulator_x"
        / "open_manipulator_x.urdf.xacro"
    )

    srdf_file = (
        robot_config_dir
        / "open_manipulator_x.srdf"
    )
    kinematics_file = (
        robot_config_dir
        / "kinematics.yaml"
    )
    joint_limits_file = (
        robot_config_dir
        / "joint_limits.yaml"
    )
    controllers_file = (
        robot_config_dir
        / "moveit_controllers.yaml"
    )

    ompl_file = (
        moveit_config_share
        / "config"
        / "ompl_planning.yaml"
    )
    ompl_defaults_file = (
        moveit_utils_share
        / "default_configs"
        / "ompl_defaults.yaml"
    )

    use_sim_time = LaunchConfiguration("use_sim_time")
    node_executable = LaunchConfiguration("node_executable")

    robot_description = {
        "robot_description": ParameterValue(
            Command(
                [
                    "xacro ",
                    str(urdf_xacro),
                    " use_sim:=",
                    use_sim_time,
                ]
            ),
            value_type=str,
        )
    }

    robot_description_semantic = {
        "robot_description_semantic": (
            srdf_file.read_text(encoding="utf-8")
        )
    }

    robot_description_kinematics = {
        "robot_description_kinematics": load_yaml(
            kinematics_file
        )
    }

    robot_description_planning = {
        "robot_description_planning": load_yaml(
            joint_limits_file
        )
    }

    ompl_parameters = load_yaml(ompl_defaults_file)
    ompl_parameters.update(load_yaml(ompl_file))

    planning_pipeline_parameters = {
        "planning_pipelines": ["ompl"],
        "default_planning_pipeline": "ompl",
        "ompl": ompl_parameters,
    }

    controller_parameters = load_yaml(controllers_file)

    common_moveit_parameters = [
        robot_description,
        robot_description_semantic,
        robot_description_kinematics,
        robot_description_planning,
        planning_pipeline_parameters,
        controller_parameters,
        {"use_sim_time": use_sim_time},
    ]

    moveit_py_parameters = {
        "moveit_manage_controllers": True,
        "plan_request_params": {
            "planning_attempts": 1,
            "planning_pipeline": "ompl",
            "planner_id": "RRTConnectkConfigDefault",
            "max_velocity_scaling_factor": 0.3,
            "max_acceleration_scaling_factor": 0.3,
            "planning_time": 5.0,
        },
        "planning_scene_monitor_options": {
            "name": "planning_scene_monitor",
            "robot_description": "robot_description",
            "joint_state_topic": "/joint_states",
            "attached_collision_object_topic": (
                "/attached_collision_object"
            ),
            "publish_planning_scene_topic": (
                "/planning_scene"
            ),
            "monitored_planning_scene_topic": (
                "/monitored_planning_scene"
            ),
            "wait_for_initial_state_timeout": 10.0,
        },
    }

    move_group_node = Node(
        package="moveit_ros_move_group",
        executable="move_group",
        name="move_group",
        output="screen",
        parameters=common_moveit_parameters,
    )

    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="screen",
        parameters=common_moveit_parameters,
    )

    moveit_py_node = Node(
        package="tf2_basic",
        executable=node_executable,
        name="open_manipulator_controller",
        output="screen",
        parameters=[
            *common_moveit_parameters,
            moveit_py_parameters,
        ],
    )

    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "use_sim_time",
                default_value="false",
                description="Gazebo의 /clock 사용 여부",
            ),
            DeclareLaunchArgument(
                "node_executable",
                default_value="moveit_class",
                description=(
                    "tf2_basic setup.py에 등록된 실행 파일"
                ),
            ),
            move_group_node,
            rviz_node,
            moveit_py_node,
        ]
    )