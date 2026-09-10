cmake_minimum_required(VERSION 3.0.2)
project(cmd_vel_to_high)

find_package(catkin REQUIRED COMPONENTS
	rospy
	geometry_msgs
	unitree_legged_msgs
)

catkin_package(
	CATKIN_DEPENDS rospy geometry_msgs unitree_legged_msgs
)

include_directories(
# include
# ${catkin_INCLUDE_DIRS}
)

## Mark executable scripts for installation
catkin_install_python(PROGRAMS
	src/go1_cmd_bridge.py
	# src/out_pose_2_odom.py
	DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
