#!/usr/bin/env python
# For moving turtle in a D shape.
import rospy
from geometry_msgs.msg import Twist
import sys
import math as m

def move_turtle_in_straight_line():
    rospy.init_node('publisher_node_1', anonymous = True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
    rate = rospy.Rate(10)

    vel = Twist()

    print("let's move the turtle bot")
    speed = int(input('input your speed: '))
    distance = int(input('give the distance you want: '))
    isForward = int(input(' Forward?: '))

    if(isForward):
        vel.linear.x = abs(speed)
    else:
        vel.linear.x = -abs(speed)
        
   
    vel.linear.y = 0
    vel.linear.z = 0

    vel.angular.x = 0
    vel.angular.y = 0
    vel.angular.z = 0

    while not rospy.is_shutdown():
        t0 = rospy.Time.now().to_sec()
        current_distance = 0

        while(current_distance<distance):
            pub.publish(vel)
            t1 = rospy.Time.now().to_sec()
            current_distance = speed * (t1-t0)
        vel.linear.x = 0
        pub.publish(vel)


        

      

if __name__ == '__main__':
    try:
        move_turtle_in_D()
    except rospy.ROSInterruptException:
        pass