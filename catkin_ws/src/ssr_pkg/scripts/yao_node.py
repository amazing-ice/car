#!/usr/bin/env python3
#coding=utf-8

import rospy
from std_msgs.msg import String

if __name__ == "__main__":
    rospy.init_node("yao_node")
    rospy.logwarn("我是瑶py")

    pub = rospy.Publisher("ge_ge", String, queue_size=10)

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        rospy.loginfo("11111")
        msg = String()
        msg.data = "求++++"
        pub.publish(msg)
        rate.sleep()