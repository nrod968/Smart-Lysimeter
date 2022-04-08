from datetime import datetime
from model.model import SmartLysimeterModel, Fieldnames
from sensors.dr_mock import MockDRSensor
from sensors.ec_ezo import ECSensor
from sensors.ec_mock import MockECSensor
from sensors.ph_ezo import PHSensor
from sensors.ph_mock import MockPHSensor
from utils.data_protocol import Protocol
from utils.uart import Port
class SmartLysimeterController():
    def __init__(self, model: SmartLysimeterModel, isTest=False):
        self._model = model
        if (isTest):
            self._phIn = MockPHSensor()
            self._phDr = MockPHSensor()
            self._ecIn = MockECSensor()
            self._ecDr = MockECSensor()
        else:
            self._phIn = PHSensor(Protocol.UART, Port.UART0)
            self._phDr = PHSensor(Protocol.UART, Port.UART5)
            self._ecIn = ECSensor(Protocol.UART, Port.UART2)
            self._ecDr = ECSensor(Protocol.UART, Port.UART3)
        self._dr = MockDRSensor()

    def generate_datapoint(self):
        phInVal = self._phIn.get_datapoint()
        ecInVal = self._ecIn.get_datapoint()
        phDrVal = self._phDr.get_datapoint()
        ecDrVal = self._ecDr.get_datapoint()
        drainage = self._dr.get_datapoint()
        timestamp = datetime.now()
        self.record_data_point(timestamp, phInVal, ecInVal, phDrVal, ecDrVal, drainage)

    def record_data_point(self, timestamp, phInReading, ecInReading, phDrReading, ecDrReading, drainageReading):
        if (isinstance(timestamp, float)):
            timestamp = datetime.fromtimestamp(timestamp)
        if (isinstance(timestamp, datetime)):
            timestamp = (timestamp.replace(microsecond=0)).isoformat()
        self._model.record_data_point(timestamp, phInReading, ecInReading, phDrReading, ecDrReading, drainageReading)

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