#!/usr/bin/env python
import rospy
import json
from virosquad.msg import info

def info_publisher():
    topic = rospy.Publisher('info', info, queue_size=1)
    rospy.init_node('info_publisher', anonymous=True)
    rate = rospy.Rate(1)
    
    msg = info()
    while not rospy.is_shutdown():
        with open('/home/witalo/catkin_ws/src/virosquad/scripts/info.json') as json_file:
            data = json.load(json_file)

        msg.header.stamp = rospy.get_rostime()
        msg.id = data['id']
        msg.vehicle = data['vehicle']
        msg.info = data['info']
        msg.details = data['details']
        topic.publish(msg)
            
if __name__ == '__main__':
    try:
        info_publisher()
    except rospy.ROSInterruptException:
        pass
