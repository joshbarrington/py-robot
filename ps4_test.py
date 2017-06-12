
from ps4 import *

p = ps4()

while True:

    button_data = p.update()
    os.system('clear')
    print button_data[0:6]
    print button_data[9:]





