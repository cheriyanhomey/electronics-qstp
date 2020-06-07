#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
rospy.init_node('circle', anonymous=True)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)


r = float(input("enter radius" ))
v = float(input("enter velocity"))
rate= rospy.Rate(1)
twist=Twist()

twist.linear.x =v
twist.angular.z = v*r
while not rospy.is_shutdown():
    pub.publish(twist)
    rate.sleep()
    
    
