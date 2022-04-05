from enum import Enum, auto
from tinydb import TinyDB
import csv

from utils.observer import Observable

class Fieldnames(str, Enum):
    TIMESTAMP = "Timestamp"
    PH = "pH"
    EC = "EC"
    DRAINAGE = "Drainage Rate"

    def __str__(self) -> str:
        return str.__str__(self)

class SmartLysimeterMessage(Enum):
    HISTORY_LEN_CHANGED = auto()
    NEW_READING = auto()

class SmartLysimeterModel(Observable):
    fieldnames = [str(el) for el in Fieldnames]

    def __init__(self, dbFileName, csvFileName, historyLength=10):
        super().__init__()
        self._lastDataPoint = {}
        self._lastNDataPoints = {}
        self._historyLength = historyLength
        self._db = TinyDB(dbFileName)
        self._csvFileName = csvFileName
        self._currRecord = 0

    def set_history_length(self, historyLength):
        self._historyLength = historyLength
        self.notify(SmartLysimeterMessage.HISTORY_LEN_CHANGED)

    def get_history_length(self):
        return self._historyLength

    def record_data_point(self, timestamp, phReading, ecReading, drainageReading):
        self._lastDataPoint =  {str(Fieldnames.TIMESTAMP): timestamp,
                                str(Fieldnames.PH): round(phReading, 2),
                                str(Fieldnames.EC): round(ecReading, 2),
                                str(Fieldnames.DRAINAGE): round(drainageReading, 2)}
        self.save_last_reading_csv()
        self.save_last_reading_db()
        self.notify(SmartLysimeterMessage.NEW_READING)

    def save_last_reading_csv(self):
        with open(self._csvFileName, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=SmartLysimeterModel.fieldnames)
            writer.writeheader()
            writer.writerow(self._lastDataPoint)
    def save_last_reading_db(self):
        self._currRecord = self._db.insert(self._lastDataPoint)

    def get_last_reading(self):
        return self._lastDataPoint

    def get_history(self):
        readings = []
        for i in range(self._historyLength):
            if (i >= self._currRecord):
                break
            readings.append(self._db.get(doc_id=(self._currRecord - i)))
        readings.reverse()
        return readings