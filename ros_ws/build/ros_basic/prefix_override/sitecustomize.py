import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/jamiek/2026_ROS_manipulator/ros_ws/install/ros_basic'
