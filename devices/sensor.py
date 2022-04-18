import abc
from enum import Enum, auto

class Sensor(Enum):
    PH_IN = auto()
    PH_DR = auto()
    EC_IN = auto()
    EC_DR = auto()
    LEVEL_IN = auto()
    LEVEL_DR = auto()

class Calibration(Enum):
    LOW = auto()
    MID = auto()
    DRY = auto()
    SINGLE = auto()

class SmartLysimeterSensor(metaclass=abc.ABCMeta):
    
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'get_datapoint') and 
                callable(subclass.get_datapoint) and
                hasattr(subclass, 'calibrate') and
                callable(subclass.calibrate))

    @abc.abstractmethod
    def read(self):
        raise NotImplementedError

    @abc.abstractmethod
    def calibrate(self, calType, calVal):
        raise NotImplementedError