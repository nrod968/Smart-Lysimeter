from random import Random
from devices.ec_ezo import ECCommand
from devices.sensor import Calibration, SmartLysimeterSensor

class MockECSensor(SmartLysimeterSensor):
    def __init__(self):
        self._randgen = Random()

    def read(self):
        return self._randgen.gauss(mu=2.1, sigma=0.05)
    
    def calibrate(self, calType, calVal):
        if (calType == Calibration.DRY):
            print(str(ECCommand.CAL_DRY))
        else:
            print(str(ECCommand.CAL).format(calVal))