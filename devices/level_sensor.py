from devices.sensor import SmartLysimeterSensor
from devices.mcp3008 import MCP3008

class LevelSensor(SmartLysimeterSensor):
    RESISTOR_GRADIENT = 150
    V_IN = 3.3
    V_REF = 3.3
    RESISTOR_VAL = 560

    def __init__(self, channelRef, channelSense, bus, device):
        self._backend = MCP3008(bus=bus, device=device)
        self._channelRef = channelRef
        self._channelSense = channelSense
    
    def read(self):
        refVal = self._backend.read(self._channelRef)
        print("ReferenceADCVal_" + str(self._channelRef) + ": " + str(refVal))
        refVout = (refVal / (MCP3008.RESOLUTION - 1)) * LevelSensor.V_REF
        print("ReferenceVout_" + str(self._channelRef) + ": " + str(refVout))
        refVal = (LevelSensor.RESISTOR_VAL / (refVout / LevelSensor.V_IN)) - LevelSensor.RESISTOR_VAL
        print("ReferenceRVal_" + str(self._channelRef) + ": " + str(refVal))
        senseVal = self._backend.read(self._channelSense)
        print("SenseADCVal_" + str(self._channelSense) + ": " + str(senseVal))
        senseVout = (senseVal / (MCP3008.RESOLUTION - 1)) * LevelSensor.V_REF
        print("SenseVout_" + str(self._channelSense) + ": " + str(senseVout))
        senseVal = (LevelSensor.RESISTOR_VAL / (senseVout / LevelSensor.V_IN)) - LevelSensor.RESISTOR_VAL
        print("SenseRVal_" + str(self._channelSense) + ": " + str(senseVal))
        sensorValue = refVal - senseVal
        print("SensorRaw: " + str(refVal))
        sensorValue = sensorValue / LevelSensor.RESISTOR_GRADIENT
        return sensorValue

    def read1(self):
        refVal = self._backend.read(self._channelRef)
        print("ReferenceADCVal_" + str(self._channelRef) + ": " + str(refVal))
        refVout = (((MCP3008.RESOLUTION - 1) / refVal) - 1)
        print("ReferenceIntermediate_" + str(self._channelRef) + ": " + str(refVout))
        refVal = (LevelSensor.RESISTOR_VAL / refVout)
        print("ReferenceRVal_" + str(self._channelRef) + ": " + str(refVal))

        senseVal = self._backend.read(self._channelSense)
        print("SenseADCVal_" + str(self._channelSense) + ": " + str(senseVal))
        senseVout = (((MCP3008.RESOLUTION - 1) / senseVal) - 1)
        print("SenseIntermediate_" + str(self._channelSense) + ": " + str(senseVout))
        senseVal = (LevelSensor.RESISTOR_VAL / senseVout)
        print("SenseRVal_" + str(self._channelSense) + ": " + str(senseVal))
        sensorValue = (refVal - senseVal) / LevelSensor.RESISTOR_GRADIENT
        if (sensorValue <= 0):
            sensorValue = 0.0000001
        return sensorValue
    
    def calibrate(self):
        pass