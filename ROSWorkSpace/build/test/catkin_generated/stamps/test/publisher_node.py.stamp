#!/usr/bin/env
import rospy
from std_msgs.msg import String
from test.msg import Position

def talk_to_me():
    pub = rospy.Publisher('talking_topic', Position, queue_size=10)
    rospy.init_node('publisher_node', anonymous=True)
    rate = rospy.Rate(100)
    rospy.loginfo("Publisher Node Started.")
    j = 0
    while not rospy.is_shutdown():
        msg = Position()
        msg.message = "My Position is"
        msg.x = 2.0
        msg.y = j

        pub.publish(msg)
        j = j + 0.5
        rate.sleep()

if __name__ == '__main__':
    try:
        talk_to_me()
    
    except rospy.ROSInterruptException:
        pass

