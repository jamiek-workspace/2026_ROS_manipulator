import os

from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    param_dir = LaunchConfiguration(
        "param_dir",
        default=os.path.join(get_package_share_directory("ros_basic"), "param", "turtlesim.yaml"),
    )
    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "param_dir",
                default_value=param_dir,
                description="launch parameter 를 지정하는 옵션",
            ),
            Node(package="turtlesim", executable="turtlesim_node", parameters=[param_dir]),
            ExecuteProcess(
                cmd=[
                    "ros2",
                    "service",
                    "call",
                    "/spawn",
                    "turtlesim/srv/Spawn",
                    "{x: 2.0, y: 2.0, theta: 0.0}",
                ],
                output="screen",
            ),
            Node(
                package="ros_basic",
                executable="mv_turtle_ns",
                namespace="turtle1",
                parameters=[param_dir],
            ),
            Node(
                package="ros_basic",
                executable="mv_turtle_ns",
                namespace="turtle2",
                parameters=[param_dir],
            ),
        ]
    )