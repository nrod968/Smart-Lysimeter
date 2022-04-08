import abc

class SmartLysimeterSensor(metaclass=abc.ABCMeta):
    
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'get_datapoint') and 
                callable(subclass.get_datapoint))

    @abc.abstractmethod
    def get_datapoint(self):
        raise NotImplementedError