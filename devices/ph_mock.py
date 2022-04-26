from random import Random
from devices.sensor import SmartLysimeterSensor

class MockPHSensor(SmartLysimeterSensor):
    def __init__(self):
        self._randgen = Random()

    def read(self):
        return self._randgen.gauss(mu=5.85, sigma=0.05)

    def calibrate(self):
        pass