from time import sleep
from devices.pump import Pump

p = Pump(17)

p.start()
sleep(10)
p.stop()
sleep(10)
p.start()