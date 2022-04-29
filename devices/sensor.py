import abc
from enum import Enum, auto

class Sensor(str, Enum):
    PH_IN = "Input pH Sensor"
    PH_DR = "Drainage pH Sensor"
    EC_IN = "Input EC Sensor"
    EC_DR = "Drainage EC Sensor"
    LEVEL_IN = "Input Level Sensor"
    LEVEL_DR = "Drainage Level Sensor"

    def __str__(self) -> str:
        return str.__str__(self)

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