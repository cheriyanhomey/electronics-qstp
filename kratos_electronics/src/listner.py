import rospy
from std_msgs.msg import String

def callback(message):
    rospy.loginfo(rospy.get_caller_id()+ "i heard %s",message.data)

def listner():
     rospy.init_node('listener',anonymous=True)
     rospy.Subscriber("/new",String,callback)
     rospy.spin()

if __name__=='__main__':
    listner()
