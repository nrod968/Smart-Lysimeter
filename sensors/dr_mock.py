from random import Random
from sensors.sensor import SmartLysimeterSensor

class MockDRSensor(SmartLysimeterSensor):
    def __init__(self):
        self._randgen = Random()

    def read(self):
        return self._randgen.gauss(mu=35.0, sigma=2.0)

    def calibrate(self):
        pass