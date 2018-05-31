__author__ = "joshuabarrington"

import explorerhat


class Motors:

    # Axis = left_analog_y
    def drive(self, axis):
        if axis < -0.7:  # Forwards
            explorerhat.motor.one.forwards()
            explorerhat.motor.two.forwards()
        elif axis > 0.7:  # Backwards
            explorerhat.motor.one.backwards()
            explorerhat.motor.two.backwards()

    # Axis = right_analog_x
    def turn(self, axis):
        if axis > 0.7:  # Right
            explorerhat.motor.one.backwards()
            explorerhat.motor.two.forwards()
        elif axis < -0.7:  # Left
            explorerhat.motor.one.forwards()
            explorerhat.motor.two.backwards()

    def stop(self):
        explorerhat.motor.one.stop()
        explorerhat.motor.two.stop()
