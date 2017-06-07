__author__ = 'joshuabarrington'

from keyboard_control import KeyboardInput
from robot import Robot
import pygame
from pygame.locals import *

pygame.init()

controller = KeyboardInput()
robot = Robot(controller)
robot.control_loop()
