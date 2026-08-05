from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'tf2_basic'

def package_files(directory):
    data_files = []

    for path, directories, filenames in os.walk(directory):
        files = [os.path.join(path, filename) for filename in filenames]

        if not files:
            continue

        install_path = os.path.join(
            "share",
            package_name,
            path,
        )

        data_files.append((install_path, files))

    return data_files

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ("share/" + package_name + "/launch", glob(os.path.join("launch", "*.launch.py"))),
        ("share/" + package_name + "/urdf", glob(os.path.join("urdf", "*.*"))),
        ("share/" + package_name + "/rviz", glob(os.path.join("rviz", "*.*"))),
        ("share/" + package_name + "/meshes", glob(os.path.join("meshes", "*.*"))),
        (
            os.path.join("share", package_name, "data"),
            glob("data/*.yaml"),
        ),
        ("share/" + package_name + "/models", glob(os.path.join("models", "*.*"))),
        ("share/" + package_name + "/world", glob(os.path.join("world", "*.*"))),
    ]
    + package_files("models"),
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jamiek',
    maintainer_email='utauloid.kk@gmail.com',
    description='TODO: Package description',
    license='MIT',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "static_turtle_tf2_broadcaster = tf2_basic.static_turtle_tf2_broadcaster:main",
            "dynamic_turtle_tf2_broadcaster = tf2_basic.dynamic_turtle_tf2_broadcaster:main",
            "tf_listener = tf2_basic.tf_listener:main",
            "turtle_tf_listener = tf2_basic.turtle_tf_listener:main",
            "move_u2d2 = tf2_basic.move_u2d2:main",
            "move_manipulator = tf2_basic.move_manipulator:main",
            "dance_manipulator = tf2_basic.dance_manipulator:main",
            "dance_manipulator2 = tf2_basic.dance_manipulator2:main",
            "move_manipulator_action = tf2_basic.move_manipulator_action:main",
            "dance_manipulator_action = tf2_basic.dance_manipulator_action:main",
            "dance_manipulator_action2 = tf2_basic.dance_manipulator_action2:main",
            "teach_manipulator = tf2_basic.teach_manipulator:main",
            "teach_manipulator_T1 = tf2_basic.teach_manipulator_T1:main",
            "play_recorded_dance = tf2_basic.play_recorded_dance:main",
            "play_recorded_grip = tf2_basic.play_recorded_grip:main",
            "moveit_test = tf2_basic.moveit_test:main",
            "moveit_class = tf2_basic.moveit_class:main",
            "moveit_scene_monitor = tf2_basic.moveit_scene_monitor:main",
            "moveit_attached = tf2_basic.moveit_attached:main",
            "moveit_mini_project = tf2_basic.moveit_mini_project:main",
            "moveit_mini_project_thread = tf2_basic.moveit_mini_project_thread:main",
            "aruco_tf_node = tf2_basic.aruco_tf_node:main",
            "aruco_pick_node = tf2_basic.aruco_pick_node:main",
        ],
    },
)
