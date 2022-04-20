from devices.level_sensor import LevelSensor
from time import sleep

levIn = LevelSensor(channelRef=0, channelSense=1, bus=1, device=0)
levDr = LevelSensor(channelRef=2, channelSense=3, bus=1, device=0)

while(True):
    drVal = levDr.read1()
    inVal = levIn.read1()
    print("In: " + str(inVal) + " inches")
    print("In: " + str(drVal) + " inches")
    drainageRate = ((abs(inVal - drVal)) / drVal) * 100
    print("Drainage Rate: " + str(drainageRate) + "%")
    sleep(1)