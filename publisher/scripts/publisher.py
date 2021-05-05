#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry


def talker():
    pub = rospy.Publisher("chatter", Odometry, queue_size=10)
    rospy.init_node("talker", anonymous=True)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        odometry_msg = Odometry()
        odometry_msg.pose.pose.position.x = 1
        rospy.loginfo(odometry_msg)
        pub.publish(odometry_msg)
        rate.sleep()


if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
