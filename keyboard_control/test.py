__author__ = 'joshuabarrington'

import sys
last = None

def evaluate(line):
    if(line == "w"):
        print("holding w")
    if(line == "a"):
        print("holding a")
    if(line == "s"):
        print("holding s")
    if(line == "d"):
       print("holding d")


while(last != 'q'):
    sys.stdout.write("Command: ")
    sys.stdout.flush()
    last = raw_input()
    evaluate(last)
