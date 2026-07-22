import os
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python import get_package_share_directory
from launch.actions import DeclareLaunchArgument


def generate_launch_description():
    param_dir = LaunchConfiguration("param_dir", default=os.path.join(get_package_share_directory("ros_basic"), "param", "my_param.yaml"))
    return LaunchDescription(
        [
            DeclareLaunchArgument("param_dir", default_value=param_dir, description="Path to the parameter file"),
            Node(
                package="ros_basic",
                executable="my_param",
                parameters=[param_dir],
                ),
        ]
    )