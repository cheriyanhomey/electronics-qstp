import rospy
from std_msgs.msg import Int32

def callback(message):
    rospy.loginfo(rospy.get_caller_id(),message.data)

def listner():
     rospy.init_node('clock_sub',anonymous=True)

     rospy.Subscriber("/hour",Int32,callback)
     rospy.Subscriber("/minute",Int32,callback)
     rospy.Subscriber("/second",Int32,callback)
     rospy.Subscriber("/clock",Int32,callback)

     rospy.spin()

if __name__=='__main__':
    listner()
