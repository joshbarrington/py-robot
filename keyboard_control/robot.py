__author__ = "joshuabarrington"

from motor_control import Motors


class Robot:
    def __init__(self, controller):
        self.controller = controller
        self.motors = Motors()

    def control_loop(self):
        if pygame.key.get_pressed():
            key = self.controller.read_command()
            self.motors.drive(key)
        else:
            self.motors.stop()
