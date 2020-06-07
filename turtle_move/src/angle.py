#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist,Point
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
theta=0

def newodom(msg):
    global roll, pitch, theta
    orientation_q = msg.pose.pose.orientation
    orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
    (roll, pitch, theta) = euler_from_quaternion (orientation_list)
    
des_ang= input("enter angle")
rospy.init_node("angle",anonymous=True)     
sub =rospy.Subscriber("/odom",Odometry,newodom)
pub = rospy.Publisher("/cmd_vel",Twist,queue_size=1)
r=rospy.Rate(1)

speed=Twist()
while not rospy.is_shutdown():
    error = des_ang - theta
    if error >0.1:
        speed.angular.z= 1
    else: 
        speed.angular.z=0
    
    pub.publish(speed)
    r.sleep