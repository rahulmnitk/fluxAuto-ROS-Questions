#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
def publisher():
	pub = rospy.Publisher('chatter', Int32, queue_size=10)
        rospy.init_node('publisher', anonymous=True)
        rate = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown():
        	for i in range(0,51):
			rospy.loginfo(i)
			pub.publish(i)
        	rate.sleep()

if __name__ == '__main__':
	try:
		publisher()
        except rospy.ROSInterruptException:      
		pass
