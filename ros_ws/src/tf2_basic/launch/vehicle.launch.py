# 실행 명령어
# ros2 run turtlesim turtle_teleop_key --ros-args -r __ns:=/model/vehicle_test -r turtle1/cmd_vel:=cmd_vel
# ros2 launch tf2_basic vehicle.launch.py

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
    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(pkg_ros_gz_sim, "launch", "gz_sim.launch.py")),
        launch_arguments={"gz_args": f"-r {world_path}"}.items(),
    )
    bridge = Node(
        package="ros_gz_bridge",
        executable="parameter_bridge",
        arguments=[
            "/model/vehicle_test/cmd_vel@geometry_msgs/msg/Twist]gz.msgs.Twist",
            "/model/vehicle_test/odometry@nav_msgs/msg/Odometry[gz.msgs.Odometry",
        ],
    )
    return LaunchDescription([gz_sim, bridge])