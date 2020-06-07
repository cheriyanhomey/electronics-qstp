#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist,Point
from nav_msgs.msg import Odometry


x=0.0


def newodom(msg):
    global x
   
    x= msg.pose.pose.position.x
   
     
    

rospy.init_node('foreward', anonymous=True)
sub = rospy.Subscriber("/odom",Odometry,newodom)
pub = rospy.Publisher("/cmd_vel",Twist,queue_size=1)
speed=Twist()
goal=Point()
goal.x=5   
r=rospy.Rate(1)
while not rospy.is_shutdown():
    eror=goal.x-x
    if abs(eror) >0.05:
        speed.linear.x = 0.1
    else:
        speed.linear.x=0
            
    pub.publish(speed) 
    r.sleep
    
       
    
