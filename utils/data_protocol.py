import abc
from enum import Enum, auto

class Protocol(Enum):
    UART = auto()

class EZODataProtocol(metaclass=abc.ABCMeta):
    
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'read_line') and 
                callable(subclass.read_line) and
                hasattr(subclass, 'read_lines') and
                callable(subclass.read_lines) and 
                hasattr(subclass, 'send_cmd') and
                callable(subclass.send_cmd) and
                hasattr(subclass, 'flush') and 
                callable(subclass.flush))

    @abc.abstractmethod
    def read_line(self):
        raise NotImplementedError

    @abc.abstractmethod
    def read_lines(self):
        raise NotImplementedError
    
    @abc.abstractmethod
    def send_cmd(self, cmd):
        raise NotImplementedError
    
    @abc.abstractmethod
    def flush(self, cmd):
        raise NotImplementedError