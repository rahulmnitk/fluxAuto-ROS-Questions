#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "Number received: %d", data.data)
    	even = []
	odd = []
	# if data.data % 2 == 0:
		# even.append(data.data)
	# else:
		# odd.append(data.data)
	# rospy.loginfo("Even numbers are: ", even)
	# rospy.loginfo("Odd numbers are: ", odd)
def listener():
	rospy.init_node('subscriber', anonymous=True)
	rospy.Subscriber("chatter", Int32, callback)
	rospy.spin()

if __name__ == '__main__':
	listener()
