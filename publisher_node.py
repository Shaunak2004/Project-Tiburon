#!/usr/bin/env python
# FOR MOVING THE TURTLE IN A CIRCLE
import rospy
from geometry_msgs.msg import Twist
import sys

def move_turtle(linear_vel, angular_vel):
    rospy.init_node('publisher_node', anonymous = True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
    rate = rospy.Rate(10)

    vel = Twist()

    while True:

        vel.linear.x = linear_vel
        vel.linear.y = 0
        vel.linear.z = 0

        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = angular_vel

        rospy.loginfo('linear velocity :%f, angular velocity : %f', linear_vel, angular_vel)

        pub.publish(vel)
        rate.sleep()

if __name__ == '__main__':
    try:
        move_turtle(float(sys.argv[1]), float(sys.argv[2]))
    except rospy.ROSInterruptException:
        pass