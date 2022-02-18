import abc
from tkinter import *
from typing import ClassVar

class SmartLysimeterWindow(metaclass=abc.ABCMeta):
    
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'place') and 
                callable(subclass.place))

    @abc.abstractmethod
    def place(self):
        raise NotImplementedError
    
    @abc.abstractmethod
    def unplace(self):
        raise NotImplementedError