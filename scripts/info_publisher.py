#!/usr/bin/env python
import rospy
from virosquad.msg import info

def info_publisher():
    topic = rospy.Publisher('info', info, queue_size=1)
    rospy.init_node('info_publisher', anonymous=True)
    rate = rospy.Rate(10)
    
    msg = info()
    while not rospy.is_shutdown():
            msg.vehicle = 'Fusca'
            msg.info = 'Veiculo do Hitler'
            msg.description = 'Veiculo extremamente potente criado no calor da guerra'

            topic.publish(msg)
            
if __name__ == '__main__':
        try:
            info_publisher()
        except rospy.ROSInterruptException:
            pass
