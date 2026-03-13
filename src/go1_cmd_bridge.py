#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from unitree_legged_msgs.msg import HighCmd, BmsCmd, LED


class Go1Bridge:
    def __init__(self):
        rospy.init_node('go1_cmd_bridge')

        # Publishers and Subscribers
        self.cmd_pub = rospy.Publisher('/high_cmd', HighCmd, queue_size=10)
        self.vel_sub = rospy.Subscriber('/cmd_vel', Twist, self.vel_callback)

        self.latest_twist = Twist()
        self.rate = rospy.Rate(100)  # 100 Hz

        rospy.loginfo("Go1 Bridge Node Initialized. Listening to /cmd_vel...")

    def vel_callback(self, msg):
        self.latest_twist = msg

    def run(self):
        # Get time
        start_time = rospy.get_time()
        
        while not rospy.is_shutdown():
            current_time = rospy.get_time()
            elapsed = current_time - start_time
            
            high_cmd = HighCmd()
            
            high_cmd.head = [0xFE, 0xEF]
            high_cmd.levelFlag = 0xEE
            
            # Start up
            if elapsed < 2.0:
                # Force Stand / Neutral position
                high_cmd.mode = 1
                rospy.loginfo_once("Bridge: Phase 1 - Force Stand")
            elif elapsed < 4.0:
                # Send readiness signal for receiving /high_cmd not from remote control
                high_cmd.mode = 6 
                rospy.loginfo_once("Bridge: Phase 2 - Mode 6 Transition")
            else:
                # Activate Walking Mode
                high_cmd.mode = 2
                high_cmd.gaitType = 1 # 1 for Trot
                high_cmd.velocity = [self.latest_twist.linear.x, self.latest_twist.linear.y]
                high_cmd.yawSpeed = self.latest_twist.angular.z
                high_cmd.footRaiseHeight = 0.08 # Standard foot raise height
                rospy.loginfo_once("Bridge: ACTIVE - Listening to /cmd_vel")

            # Default safety values
            high_cmd.bodyHeight = 0.0
            high_cmd.euler = [0.0, 0.0, 0.0]

            self.cmd_pub.publish(high_cmd)
            self.rate.sleep()


if __name__ == '__main__':
    try:
        bridge = Go1Bridge()
        bridge.run()
    except rospy.ROSInterruptException:
        pass
