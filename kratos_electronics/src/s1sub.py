import rospy
from std_msgs.msg import String
#function to publish data in s2
def s2pub(message):
    pub = rospy.Publisher('/s2',String,queue_size=10)
    rospy.init_node('s2pub',anonymous=True)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        if message.data == 'green':
            rospy.loginfo("red")
            pub.publish("red")
        else:
            rospy.loginfo("green")
            pub.publish("green")
            rate.sleep()

def callback(message):
    if message.data == 'green':
        rospy.loginfo( "red")
    else:
        rospy.loginfo("green")
#function to publish data in s1
def s1sub():
     rospy.init_node('s1sub',anonymous=True)
     rospy.Subscriber("/s1",String,callback)
     rospy.spin()

if __name__=='__main__':
    s1sub()
    try:
        s2pub(message)
    except rospy.ROSInterruptException:
        pass
