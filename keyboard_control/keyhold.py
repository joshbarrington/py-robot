__author__ = 'joshuabarrington'

import curses
import os
from motor_control import Motors


def main(win):
    win.nodelay(True)
    key = ""
    win.clear()
    win.addstr("Detected key:")
    motors = Motors()
    while 1:
        try:
            key = win.getkey()
            win.clear()
            win.addstr("Detected key:")
            win.addstr(str(key))
            motors.drive(str(key))
            if key == os.linesep:
                break
        except Exception as e:
            motors.stop()
            pass


curses.wrapper(main)
