__author__ = "joshuabarrington"

from robot import Robot

from keyboard_control import KeyboardInput

controller = KeyboardInput()
robot = Robot(controller)
robot.control_loop()
