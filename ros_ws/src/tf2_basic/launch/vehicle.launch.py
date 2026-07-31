# 실행 명령어
# ros2 run turtlesim turtle_teleop_key --ros-args -r __ns:=/model/vehicle_test -r turtle1/cmd_vel:=cmd_vel
# ros2 launch tf2_basic vehicle.launch.py
# sudo apt install ros-jazzy-sdformat-urdf

import os

from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    pkg_ros_gz_sim = get_package_share_directory("ros_gz_sim")
    pkg_ros_tf2_basic = get_package_share_directory("tf2_basic")
    world_path = os.path.join(pkg_ros_tf2_basic, "world", "building_robot.sdf")
    robot_model_path = os.path.join(pkg_ros_tf2_basic, "models", "vehicle_test", "model.sdf")
    with open(robot_model_path, "r", encoding="utf-8") as f:
        robot_description = f.read()
    robot_state_publisher = Node(
         package="robot_state_publisher",
         executable="robot_state_publisher", name="robot_state_publisher",
         parameters=[{"robot_description": robot_description, "use_sim_time": True}],
         )

    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(pkg_ros_gz_sim, "launch", "gz_sim.launch.py")),
        launch_arguments={"gz_args": f"-r {world_path}"}.items(),
    )
    spawn_robot_1 = Node(
        package="ros_gz_sim",
        executable="create",
        arguments=[
            "-file", robot_model_path,
            "-name", "vehicle_1",
            "-x", "0.0",
            "-y", "2.0",
            "-z", "0.35",
        ],
        output="screen",
    )
    bridge = Node(
        package="ros_gz_bridge",
        executable="parameter_bridge",
        arguments=[
            "/model/vehicle_test/cmd_vel@geometry_msgs/msg/Twist]gz.msgs.Twist",
            "/model/vehicle_test/odometry@nav_msgs/msg/Odometry[gz.msgs.Odometry",
            "/model/vehicle_1/cmd_vel@geometry_msgs/msg/Twist]gz.msgs.Twist",
            "/model/vehicle_1/odometry@nav_msgs/msg/Odometry[gz.msgs.Odometry",
            "/model/vehicle_test/joint_state@sensor_msgs/msg/JointState@gz.msgs.Model",
            "/clock@rosgraph_msgs/msg/Clock@gz.msgs.Clock"
        ],
        remappings=[("model/vehicle_test/joint_state", "/joint_states")],
        parameters=[
            "/model/vehicle_test/cmd_vel@geometry_msgs/msg/Twist]gz.msgs.Twist",
            "/model/vehicle_test/odometry@nav_msgs/msg/Odometry[gz.msgs.Odometry",
            "/model/vehicle_1/cmd_vel@geometry_msgs/msg/Twist]gz.msgs.Twist",
            "/model/vehicle_1/odometry@nav_msgs/msg/Odometry[gz.msgs.Odometry",
        ],
    )
    return LaunchDescription([
        gz_sim,
        spawn_robot_1,
        bridge,
    ])