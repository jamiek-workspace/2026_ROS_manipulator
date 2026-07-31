import os

from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def generate_launch_description():
    pkg_ros_gz_sim = get_package_share_directory("ros_gz_sim")
    pkg_tf2_basic = get_package_share_directory("tf2_basic")

    world_path = os.path.join(
        pkg_tf2_basic,
        "world",
        "building_robot.sdf",
    )

    sdf_path = os.path.join(
        pkg_tf2_basic,
        "models",
        "vehicle_test",
        "model.sdf",
    )

    urdf_path = os.path.join(
        pkg_tf2_basic,
        "urdf",
        "vehicle_test.urdf",
    )

    with open(urdf_path, "r", encoding="utf-8") as file:
        robot_description = file.read()

    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                pkg_ros_gz_sim,
                "launch",
                "gz_sim.launch.py",
            )
        ),
        launch_arguments={"gz_args": f"-r {world_path}"}.items(),
    )

    spawn_robot = Node(
        package="ros_gz_sim",
        executable="create",
        output="screen",
        arguments=[
            "-file",
            sdf_path,
            "-name",
            "vehicle_1",
            "-x",
            "0.0",
            "-y",
            "2.0",
            "-z",
            "0.35",
        ],
    )

    bridge = Node(
        package="ros_gz_bridge",
        executable="parameter_bridge",
        output="screen",
        arguments=[
            "/model/vehicle_1/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist",
            "/model/vehicle_1/odometry@nav_msgs/msg/Odometry@gz.msgs.Odometry",
            "/model/vehicle_1/joint_state@sensor_msgs/msg/JointState@gz.msgs.Model",
            "/model/vehicle_test/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist",
            "/model/vehicle_test/odometry@nav_msgs/msg/Odometry@gz.msgs.Odometry",
            "/model/vehicle_test/joint_state@sensor_msgs/msg/JointState@gz.msgs.Model",
            "/clock@rosgraph_msgs/msg/Clock@gz.msgs.Clock",
            "/world/empty/model/vehicle_1/link/camera_link/sensor/front_camera/camera_info@sensor_msgs/msg/CameraInfo@gz.msgs.CameraInfo",
            "/world/empty/model/vehicle_1/link/camera_link/sensor/front_camera/image@sensor_msgs/msg/Image@gz.msgs.Image",
            "/world/empty/model/vehicle_test/link/camera_link/sensor/front_camera/camera_info@sensor_msgs/msg/CameraInfo@gz.msgs.CameraInfo",
            "/world/empty/model/vehicle_test/link/camera_link/sensor/front_camera/image@sensor_msgs/msg/Image@gz.msgs.Image",
        ],
        remappings=[
            (
                "/model/vehicle_1/joint_state",
                "/joint_states",
            ),
            (
                "/model/vehicle_test/joint_state",
                "/joint_states",
            ),
            (
                "/world/empty/model/vehicle_1/link/camera_link/sensor/front_camera/camera_info",
                "/vehicle_1/camera/camera_info",
            ),
            (
                "/world/empty/model/vehicle_1/link/camera_link/sensor/front_camera/image",
                "/vehicle_1/camera/image_raw",
            ),
            (
                "/world/empty/model/vehicle_test/link/camera_link/sensor/front_camera/camera_info",
                "/vehicle_test/camera/camera_info",
            ),
            (
                "/world/empty/model/vehicle_test/link/camera_link/sensor/front_camera/image",
                "/vehicle_test/camera/image_raw",
            ),
        ],
    )

    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[
            {
                "robot_description": robot_description,
                "use_sim_time": True,
            }
        ],
    )

    # 우선 RViz에서 로봇 내부 TF를 확인하기 위한 임시 TF
    # 실제 주행 시에는 odometry 기반 동적 TF로 교체해야 함
    odom_to_chassis = Node(
        package="tf2_ros",
        executable="static_transform_publisher",
        output="screen",
        arguments=[
            "--x",
            "0.0",
            "--y",
            "2.0",
            "--z",
            "0.35",
            "--yaw",
            "0.0",
            "--pitch",
            "0.0",
            "--roll",
            "0.0",
            "--frame-id",
            "odom",
            "--child-frame-id",
            "chassis",
        ],
    )

    return LaunchDescription(
        [
            gz_sim,
            spawn_robot,
            bridge,
            robot_state_publisher,
            odom_to_chassis,
        ]
    )