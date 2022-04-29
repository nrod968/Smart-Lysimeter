from random import Random
from devices.ph_ezo import PHCommand
from devices.sensor import Calibration, SmartLysimeterSensor

class MockPHSensor(SmartLysimeterSensor):
    def __init__(self):
        self._randgen = Random()

    def read(self):
        return self._randgen.gauss(mu=5.85, sigma=0.05)

    def calibrate(self, calType, calVal):
        if (calType == Calibration.MID):
            print(str(PHCommand.CAL_MID).format(calVal))
        elif (calType == Calibration.LOW):
            print(str(PHCommand.CAL_LOW).format(calVal))
