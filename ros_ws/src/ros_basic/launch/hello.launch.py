from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ros_basic',
            executable='class_msg_pub',
            name='message_pub',
            output='screen',
        ),
        Node(
            package='ros_basic',
            executable='class_time_pub',
            name='time_pub',
            output='screen',
        ),
        Node(
            package='ros_basic',
            executable='class_m1_sub',
            name='m1sub',
            output='screen',
        ),
        Node(
            package='ros_basic',
            executable='class_m2_sub',
            name='m2sub',
            output='screen',
        ),
        Node(
            package='ros_basic',
            executable='class_mt_sub',
            name='mtsub',
            output='screen',
        ),
    ])