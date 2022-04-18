from datetime import datetime
from model.model import SmartLysimeterModel, Fieldnames
from devices.dr_mock import MockDRSensor
from devices.ec_ezo import ECSensor
from devices.ec_mock import MockECSensor
from devices.level_sensor import LevelSensor
from devices.ph_ezo import PHSensor
from devices.ph_mock import MockPHSensor
from devices.sensor import Calibration, Sensor
from utils.data_protocol import Protocol, Port
from devices.pump import Pump
import os
class SmartLysimeterController():
    def __init__(self, model: SmartLysimeterModel, isTest=False):
        self._model = model
        self._pumpIn = Pump(Pump.INPUT_PIN)
        self._pumpDr = Pump(Pump.DRAINAGE_PIN)
        if (isTest):
            self._phIn = MockPHSensor()
            self._phDr = MockPHSensor()
            self._ecIn = MockECSensor()
            self._ecDr = MockECSensor()
            self._dr = MockDRSensor()
        else:
            self._phIn = PHSensor(Protocol.UART, Port.UART0)
            self._phDr = PHSensor(Protocol.UART, Port.UART5)
            self._ecIn = ECSensor(Protocol.UART, Port.UART2)
            self._ecDr = ECSensor(Protocol.UART, Port.UART3)
            self._levIn = LevelSensor(channelRef=0, channelSense=1)
            self._levDr = LevelSensor(channelRef=2, channelSense=3)

    def generate_datapoint(self):
        phInVal = self._phIn.read()
        ecInVal = self._ecIn.read()
        phDrVal = self._phDr.read()
        ecDrVal = self._ecDr.read()
        drainage = self._dr.read()
        #levInVal = self._levIn.read()
        #levDrVal = self._levDr.read()
        #drainage = (abs(levDrVal - levInVal)) / levInVal
        timestamp = datetime.now()
        self.record_data_point(timestamp, phInVal, ecInVal, phDrVal, ecDrVal, drainage)

    def record_data_point(self, timestamp, phInReading, ecInReading, phDrReading, ecDrReading, drainageReading):
        if (isinstance(timestamp, float)):
            timestamp = datetime.fromtimestamp(timestamp)
        if (isinstance(timestamp, datetime)):
            timestamp = (timestamp.replace(microsecond=0)).isoformat()
        self._model.record_data_point(timestamp, phInReading, ecInReading, phDrReading, ecDrReading, drainageReading)

    def calibrate_sensor(self, sensorType: Sensor, calType: Calibration, calVal):
        if (sensorType == Sensor.PH_IN):
            self._phIn.calibrate(calType, calVal)
        elif (sensorType == Sensor.PH_DR):
            self._phDr.calibrate(calType, calVal)
        elif (sensorType == Sensor.EC_IN):
            self._ecDr.calibrate(calType, calVal)
        elif (sensorType == Sensor.EC_DR):
            self._ecDr.calibrate(calType, calVal)
    
    def shutdown(self):
        os.system("sudo shutdown -h now")
    
    def drain_tanks(self):
        

    def get_history_length(self) -> int:
        return self._model.get_history_length()
    def set_history_length(self, historyLength: int) -> None:
        self._model.set_history_length(historyLength)

    def get_last_reading(self):
        reading = self._model.get_last_reading()
        reading[Fieldnames.TIMESTAMP] = datetime.fromisoformat(reading[Fieldnames.TIMESTAMP])
        return reading
    def get_last_pH_in_reading(self) -> float:
        reading = self._model.get_last_reading()
        return reading[Fieldnames.PH_IN]
    def get_last_EC_in_reading(self) -> float:
        reading = self._model.get_last_reading()
        return reading[Fieldnames.EC_IN]
    def get_last_pH_dr_reading(self) -> float:
        reading = self._model.get_last_reading()
        return reading[Fieldnames.PH_DR]
    def get_last_EC_dr_reading(self) -> float:
        reading = self._model.get_last_reading()
        return reading[Fieldnames.EC_DR]
    def get_last_drainage_reading(self) -> float:
        reading = self._model.get_last_reading()
        return reading[Fieldnames.DRAINAGE]
    def get_timestamp_last_reading(self):
        reading = self._model.get_last_reading()
        return datetime.fromisoformat(reading[Fieldnames.TIMESTAMP])
    
    def get_history(self):
        readings = self._model.get_history()
        for reading in readings:
            reading[Fieldnames.TIMESTAMP] = datetime.fromisoformat(reading[Fieldnames.TIMESTAMP])
        return readings
    def get_pH_in_history(self) -> float:
        readings = self._model.get_history()
        phReadings = []
        for reading in readings:
            phReadings.append(reading[Fieldnames.PH_IN])
        return phReadings
    def get_EC_in_history(self) -> float:
        readings = self._model.get_history()
        ecReadings = []
        for reading in readings:
            ecReadings.append(reading[Fieldnames.EC_IN])
        return ecReadings
    def get_pH_dr_history(self) -> float:
        readings = self._model.get_history()
        phReadings = []
        for reading in readings:
            phReadings.append(reading[Fieldnames.PH_DR])
        return phReadings
    def get_EC_dr_history(self) -> float:
        readings = self._model.get_history()
        ecReadings = []
        for reading in readings:
            ecReadings.append(reading[Fieldnames.EC_DR])
        return ecReadings
    def get_drainage_history(self) -> float:
        readings = self._model.get_history()
        drainageReadings = []
        for reading in readings:
            drainageReadings.append(reading[Fieldnames.DRAINAGE])
        return drainageReadings
    def get_timestamp_history(self):
        readings = self._model.get_history()
        timestampReadings = []
        for reading in readings:
            timestampReadings.append(datetime.fromisoformat(reading[Fieldnames.TIMESTAMP]))
        return timestampReadings