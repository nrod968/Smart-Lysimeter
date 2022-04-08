import abc

class SmartLysimeterDriver(metaclass=abc.ABCMeta):
    
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'generate_datapoint') and 
                callable(subclass.generate_datapoint))

    @abc.abstractmethod
    def generate_datapoint(self):
        raise NotImplementedError