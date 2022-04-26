from enum import Enum, auto
from tinydb import TinyDB
import csv

from utils.observer import Observable

class Fieldnames(str, Enum):
    TIMESTAMP = "Timestamp"
    PH_IN = "Input pH"
    EC_IN = "Input EC"
    PH_DR = "Drainage pH"
    EC_DR = "Drainage EC"
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

    def record_data_point(self, timestamp, phInReading, ecInReading, phDrReading, ecDrReading, drainageReading):
        if (drainageReading is None):
            drainageReading = 0.00
        self._lastDataPoint =  {str(Fieldnames.TIMESTAMP): timestamp,
                                str(Fieldnames.PH_IN): round(phInReading, 2),
                                str(Fieldnames.EC_IN): round(ecInReading, 2),
                                str(Fieldnames.PH_DR): round(phDrReading, 2),
                                str(Fieldnames.EC_DR): round(ecDrReading, 2),
                                str(Fieldnames.DRAINAGE): round(drainageReading, 2)}
        self.save_last_reading_csv()
        self.save_last_reading_db()
        self.notify(SmartLysimeterMessage.NEW_READING)

    def save_last_reading_csv(self):
        try:
            with open(self._csvFileName, 'r+', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=SmartLysimeterModel.fieldnames)
                if (csvfile.readline() == ''):
                    writer.writeheader()
                writer.writerow(self._lastDataPoint)
        except:
            with open(self._csvFileName, 'w', newline='') as csvfile:
                pass
            with open(self._csvFileName, 'r+', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=SmartLysimeterModel.fieldnames)
                if (csvfile.readline() == ''):
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