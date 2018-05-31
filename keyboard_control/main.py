__author__ = 'joshuabarrington'

from keyboard_control import KeyboardInput
from robot import Robot

controller = KeyboardInput()
robot = Robot(controller)
robot.control_loop()
