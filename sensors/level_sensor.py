from sensors.sensor import SmartLysimeterSensor
from utils.mcp3008 import MCP3008

class LevelSensor(SmartLysimeterSensor):
    RESISTOR_GRADIENT = 150

    def __init__(self, channelRef, channelSense):
        self._backend = MCP3008()
        self._channelRef = channelRef
        self._channelSense = channelSense
    
    def read(self):
        refVal = self._backend.read(self._channelRef)
        senseVal = self._backend.read(self._channelSense)
        sensorValue = refVal - senseVal
        sensorValue = sensorValue / LevelSensor.RESISTOR_GRADIENT
    
    def calibrate(self):
        pass