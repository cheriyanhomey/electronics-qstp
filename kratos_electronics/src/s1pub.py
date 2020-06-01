import rospy
from std_msgs.msg import String
import time

def s1pub():
    pub = rospy.Publisher('/s1',String,queue_size=10)
    rospy.init_node('s1pub',anonymous=True)
    rate = rospy.Rate(1)
    i=1
    j=1
    while not rospy.is_shutdown():
        for i in range(1,10):
            green_str= "green"
            rospy.loginfo(green_str)
            pub.publish(green_str)
            time.sleep(1)
        for j in range(1,10):
            red_str = "red"
            rospy.loginfo(red_str)
            pub.publish(red_str)
            time.sleep(1)
        rate.sleep()
        i=i+1
        j=j+1
if __name__ == '__main__':
    try:
        s1pub()
    except rospy.ROSInterruptException:
        pass
