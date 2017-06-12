
from ps4 import *

p = ps4()

while True:

    p.update()
	
    a = p.left_analog_y
    b = p.right_analog_x

    if a is not None:
	print a
    else:
	pass







