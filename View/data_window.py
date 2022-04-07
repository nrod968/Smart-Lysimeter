import abc
from tkinter import *

from view.window import SmartLysimeterWindow

class SmartLysimeterDataWindow(SmartLysimeterWindow):
    
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'add_data_point') and 
                callable(subclass.add_data_point) and
                hasattr(subclass, 'set_history_length') and
                callable(subclass.set_history_length))

    @abc.abstractmethod
    def add_data_point(self):
        raise NotImplementedError

    @abc.abstractmethod
    def set_history_length(self, historyLength):
        raise NotImplementedError