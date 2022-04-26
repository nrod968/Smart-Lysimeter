from random import Random
from devices.sensor import SmartLysimeterSensor

class MockECSensor(SmartLysimeterSensor):
    def __init__(self):
        self._randgen = Random()

    def read(self):
        return self._randgen.gauss(mu=2.1, sigma=0.05)
    
    def calibrate(self):
        pass