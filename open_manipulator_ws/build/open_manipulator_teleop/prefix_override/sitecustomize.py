import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/jamiek/2026_ROS_manipulator/open_manipulator_ws/install/open_manipulator_teleop'
