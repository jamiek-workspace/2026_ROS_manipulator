# urdf_launch 설치 sudo apt install ros-jazzy-urdf-launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    default_rviz_config_path = PathJoinSubstitution(
        [FindPackageShare("tf2_basic"), "rviz", "urdf.rviz"]
    )
    default_model_path = PathJoinSubstitution(
        [FindPackageShare("tf2_basic"), "urdf", "06_macroed.urdf.xacro"]
    )
    model = DeclareLaunchArgument(
        name="model", default_value=default_model_path, description="model path"
    )
    gui_arg = DeclareLaunchArgument(
        name="gui",
        default_value="false",
        choices=["true", "false"],
        description="gui display enable option",
    )
    rviz_arg = DeclareLaunchArgument(
        name="rvizconfig",
        default_value=default_rviz_config_path,
        description="rviz config option file path",
    )
    return LaunchDescription(
        [
            model,
            gui_arg,
            rviz_arg,
            IncludeLaunchDescription(
                PathJoinSubstitution(
                    [FindPackageShare("urdf_launch"), "launch", "display.launch.py"]
                ),
                launch_arguments={
                    "urdf_package": "tf2_basic",
                    "urdf_package_path": LaunchConfiguration("model"),
                    "rviz_config": LaunchConfiguration("rvizconfig"),
                    "jsp_gui": LaunchConfiguration("gui"),
                }.items(),
            ),
        ]
    )