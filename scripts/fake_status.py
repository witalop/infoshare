#!/usr/bin/env python
import rospy
import random
from std_msgs.msg import Int32
from geometry_msgs.msg import Twist

def battery_status_publisher():
    
    topic1 = rospy.Publisher('status/battery', Int32, queue_size=1)
    topic2 = rospy.Publisher('status/gps', Twist, queue_size=1)
    
    msg1 = Int32()
    msg2 = Twist()
    while not rospy.is_shutdown():
        msg1.data = random.randint(0,100)
        topic1.publish(msg1)

        msg2.linear.x = random.randint(-100,100)
        msg2.linear.y = random.randint(-100,100)
        msg2.linear.z = random.randint(-100,100)
        msg2.angular.x = random.randint(-100,100)
        msg2.angular.y = random.randint(-100,100)
        msg2.angular.z = random.randint(-100,100)
        topic2.publish(msg2)
            
if __name__ == '__main__':
    try:
        rospy.init_node('info_publisher', anonymous=True)
        battery_status_publisher()
        gps_status_publisher()
    except rospy.ROSInterruptException:
        pass
