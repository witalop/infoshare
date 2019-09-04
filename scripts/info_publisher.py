#!/usr/bin/env python
import rospy
import json
from infoshare.msg import info
from std_msgs.msg import Int32
from geometry_msgs.msg import Twist

msg = info()

def battery(content):
    msg.battery = content.data

def gps(content):
    msg.gps.linear.x = content.linear.x
    msg.gps.linear.y = content.linear.y
    msg.gps.linear.z = content.linear.z
    msg.gps.angular.x = content.angular.x
    msg.gps.angular.y = content.angular.y
    msg.gps.angular.z = content.angular.z

def info_publisher():
    with open('/home/ubuntu/catkin_ws/src/infoshare/scripts/info.json') as json_file:
        data = json.load(json_file)

    topic = rospy.Publisher('info/'+ str(data['id']), info, queue_size=1)
    rospy.init_node('info_publisher', anonymous=True)
    rate = rospy.Rate(1)
        
    msg.header.stamp = rospy.get_rostime()
    msg.id = data['id']
    msg.vehicle = data['vehicle']
    msg.info = data['info']
    msg.details = data['details']

    rospy.Subscriber('status/battery', Int32, battery)
    rospy.Subscriber('status/gps', Twist, gps)

    while not rospy.is_shutdown():
        topic.publish(msg)
        rate.sleep()
            
if __name__ == '__main__':
    try:
        info_publisher()
    except rospy.ROSInterruptException:
        pass