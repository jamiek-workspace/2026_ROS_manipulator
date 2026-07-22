from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'ros_basic'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),
        (
            'share/' + package_name,
            ['package.xml']
        ),
        (
            'share/' + package_name + '/launch',
            glob(os.path.join('launch', '*.launch.py'))
        ),
    ],
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
            'simple_pub = ros_basic.simple_pub:main',
            'header_pub = ros_basic.header_pub:main',

            'class_pub = ros_basic.class_pub:main',
            'class_sub = ros_basic.class_sub:main',

            'class_msg_pub = ros_basic.class_msg_pub:main',
            'class_time_pub = ros_basic.class_time_pub:main',
            'class_m1_sub = ros_basic.class_m1_sub:main',
            'class_m2_sub = ros_basic.class_m2_sub:main',
            'class_mt_sub = ros_basic.class_mt_sub:main',

            'mv_turtle = ros_basic.mv_turtle:main',

            'qos_test_pub = ros_basic.qos_test_pub:main',
            'qos_test_sub = ros_basic.qos_test_sub:main',
        ],
    },
)