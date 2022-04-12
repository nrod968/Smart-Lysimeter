from random import Random
from sensors.sensor import SmartLysimeterSensor

class MockECSensor(SmartLysimeterSensor):
    def __init__(self):
        self._randgen = Random()

    def get_datapoint(self):
        return self._randgen.gauss(mu=2.1, sigma=0.15)
    
    def calibrate(self):
        pass