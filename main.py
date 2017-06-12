__author__ = 'joshuabarrington'

from ps4 import *
from motor_control import Motors
import os
import sys

def control_loop():
	motors = Motors()
	controller = ps4()

	while True:
		
		controller.update()
		
		drive_axis = controller.left_analog_y  
		turn_axis = controller.right_analog_x

		if noise_check(drive_axis) or noise_check(turn_axis):
			motors.drive(drive_axis)
			motors.turn(turn_axis)
		elif controller.ps_button:
			os.system("sudo shutdown -h now")
			sys.exit
		else:
			motors.stop()

def noise_check(int):
	if 0.1 < int or int < -0.1: 
		return True

control_loop()



