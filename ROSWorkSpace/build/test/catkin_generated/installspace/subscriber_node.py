#!usr/bin/env
import rospy
from std_msgs.msg import String
from test.msg import Position


def callback(data):
    rospy.loginfo("%s X: %f Y: %f", data.message, data.x, data.y)


def listener():
    rospy.init_node("subscriber_node", anonymous = True)
    rospy.Subscriber('talking_topic', Position, callback)
    rospy.spin()

if __name__ == "__main__":
    try:
        listener()

    except rospy.ROSInterruptException:
        pass
