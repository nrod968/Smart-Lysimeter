from sensors.sensor import SmartLysimeterSensor
from utils.mcp3008 import MCP3008

class LevelSensor(SmartLysimeterSensor):
    RESISTOR_GRADIENT = 150
    V_IN = 5
    RESISTOR_VAL = 500

    def __init__(self, channelRef, channelSense):
        self._backend = MCP3008()
        self._channelRef = channelRef
        self._channelSense = channelSense
    
    def read(self):
        refVout = self._backend.read(self._channelRef)
        refVal = (LevelSensor.RESISTOR_VAL / (refVout / LevelSensor.V_IN)) - LevelSensor.RESISTOR_VAL
        senseVout = self._backend.read(self._channelSense)
        senseVal = (LevelSensor.RESISTOR_VAL / (senseVout / LevelSensor.V_IN)) - LevelSensor.RESISTOR_VAL
        sensorValue = refVal - senseVal
        sensorValue = sensorValue / LevelSensor.RESISTOR_GRADIENT
    
    def calibrate(self):
        pass