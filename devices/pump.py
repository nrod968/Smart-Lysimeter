#from gpiozero import DigitalOutputDevice

class Pump:
    INPUT_PIN = 17
    DRAINAGE_PIN = 18
    def __init__(self, pin):
        self._pin = pin
        self._backend = DigitalOutputDevice(pin)

    def start(self):
        self._backend.on()
    
    def stop(self):
        self._backend.off()

### DELETE BEFORE IMPLEMENTATION ###
class DigitalOutputDevice:
    def __init__(self, pin):
        pass
    def on(self):
        pass
    def off(self):
        pass