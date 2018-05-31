__author__ = 'joshuabarrington'

import explorerhat


class Motors:
    def drive(self, key):
        if key == "w":
            explorerhat.motor.one.fowards()
            explorerhat.motor.two.forwards()
        elif key == "s":
            explorerhat.motor.one.backwards()
            explorerhat.motor.two.backwards()
        elif key == "a":
            explorerhat.motor.one.fowards()
            explorerhat.motor.two.backwards()
        elif key == "d":
            explorerhat.motor.one.backwards()
            explorerhat.motor.two.forwards()

    def stop(self):
        explorerhat.motor.one.stop()
        explorerhat.motor.two.stop()

