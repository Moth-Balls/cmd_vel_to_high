# `/cmd_vel` to Unitree `/high_cmd` message

This is a ROS1 bridge node for converting a standard `/cmd_vel` topic to Unitree's `/high_cmd` topic for when you run the [unitree_ros_to_real](https://github.com/unitreerobotics/unitree_ros_to_real) package for a Unitree Go1. 


## Features
- Converts `/cmd_vel` Twist messages &rarr; `/high_cmd` messages.
- Auto start up where Go1 will raise from down position to standing
- Sends readiness signal to recieve `/high_cmd` topics from ROS


## Notes
This package does not expose any parameter functions for changing the input Twist topic. You will need to edit the `go1_cmd_bridge.py` script to change the topic. Maybe in the future I will add a parameter?

## Usage
Ensure the `unitree_legged_msgs` included in the [unitree_ros_to_real](https://github.com/unitreerobotics/unitree_ros_to_real) package is built and sourced before running bridge. The bridge won't be able to translate the messages without them.

```shell
rosrun cmd_vel_to_high go1_cmd_bridge.py
```

