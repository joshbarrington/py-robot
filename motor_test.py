import explorerhat
import time

explorerhat.motor.one.forwards()
explorerhat.motor.two.forwards()

time.sleep(2)

explorerhat.motor.one.stop()
explorerhat.motor.two.stop()

