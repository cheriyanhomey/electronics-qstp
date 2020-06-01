import rospy
from std_msgs.msg import Int32
count =0

def second():
    pub = rospy.Publisher('/second',Int32,queue_size = 10)
    rospy.init_node('clock_pub',anonymous=True)
    rate = rospy.Rate(1)
    count = int(rospy.get_time())
    sec = count
    rospy.loginfo( sec)
    pub.publish(sec)
    rate.sleep()


def minute():
    pub = rospy.Publisher('/minute',Int32,queue_size = 10)
    rospy.init_node('clock_pub',anonymous=True)
    rate = rospy.Rate(1)

    count = int(rospy.get_time())
    min= int(count /60)
    sec= count%60

    rospy.loginfo(  min)
    pub.publish( min)
    rate.sleep()


def hour():
    pub = rospy.Publisher('/hour',Int32,queue_size = 10)
    rospy.init_node('clock_pub',anonymous=True)
    rate = rospy.Rate(1)

    count = int(rospy.get_time())
    hour= int(count /3600)
    sec= count%60

    rospy.loginfo( hour)
    pub.publish( hour)

    rate.sleep()

def clock():
    pub = rospy.Publisher('/clock',Int32,queue_size = 10)
    rospy.init_node('clock_pub',anonymous=True)
    rate = rospy.Rate(1)

    count = int(rospy.get_time())
    hour= int(count /3600)
    min= int(count /60)
    sec= count%60
    rospy.loginfo(sec)
    pub.publish(sec)
    rospy.loginfo(min)
    pub.publish( min)
    rospy.loginfo( hour)
    pub.publish( hour)

    rate.sleep()

if __name__ == '__main__':

    while not rospy.is_shutdown():
        if count<60:
            second()
            clock()
        elif count<3600:
            minute()
            second()
            clock()
        elif count>3600:
            hour()
            minute()
            second()
            clock()
