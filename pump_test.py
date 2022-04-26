from time import sleep
from devices.pump import Pump
import RPi.GPIO as GPIO

p = Pump(17)
p2 = Pump(6)

p.start()
p2.start()
print("on")
sleep(10)
p.stop()
p2.stop()
print("off")
sleep(10)
p.start()
p2.start()
print("on")
sleep(10)
p.stop()
p2.stop()
print("off")