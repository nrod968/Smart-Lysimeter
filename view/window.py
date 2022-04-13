import abc

class SmartLysimeterWindow(metaclass=abc.ABCMeta):
    
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'place') and 
                callable(subclass.place) and
                hasattr(subclass, 'unplace') and
                callable(subclass.unplace))

    @abc.abstractmethod
    def place(self):
        raise NotImplementedError
    
    @abc.abstractmethod
    def unplace(self):
        raise NotImplementedError