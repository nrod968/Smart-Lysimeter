from sensors.sensor import SmartLysimeterSensor
from utils.mcp3008 import MCP3008

class LevelSensor(SmartLysimeterSensor):
    RESISTOR_GRADIENT = 150
    V_IN = 3.3
    V_REF = 3.3
    RESISTOR_VAL = 560

    def __init__(self, channelRef, channelSense):
        self._backend = MCP3008()
        self._channelRef = channelRef
        self._channelSense = channelSense
    
    def read(self):
        refVout = (self._backend.read(self._channelRef) / MCP3008.RESOLUTION) * LevelSensor.V_REF
        refVal = (LevelSensor.RESISTOR_VAL / (refVout / LevelSensor.V_IN)) - LevelSensor.RESISTOR_VAL
        senseVout = (self._backend.read(self._channelSense) / MCP3008.RESOLUTION) * LevelSensor.V_REF
        senseVal = (LevelSensor.RESISTOR_VAL / (senseVout / LevelSensor.V_IN)) - LevelSensor.RESISTOR_VAL
        sensorValue = refVal - senseVal
        sensorValue = sensorValue / LevelSensor.RESISTOR_GRADIENT
        return sensorValue
    
    def calibrate(self):
        pass