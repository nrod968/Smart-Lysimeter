import abc

class Observer(metaclass=abc.ABCMeta):
    
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'update') and 
                callable(subclass.update))

    @abc.abstractmethod
    def update(self, message):
        raise NotImplementedError

class Observable():
    def __init__(self):
        self._observers = set()
    def register(self, who):
        self._observers.add(who)
    def unregister(self, who):
        self._observers.discard(who)
    def notify(self, message):
        for observer in self._observers:
            observer.update(message)