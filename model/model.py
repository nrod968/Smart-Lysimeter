from enum import Enum
from tinydb import TinyDB, Query
import csv

from utils.observer import Observable

class Fieldnames(Enum):
    TIMESTAMP = "Timestamp"
    PH = "pH"
    EC = "EC"
    DRAINAGE = "Drainage Rate"
class SmartLysimeterModel(Observable):
    fieldnames = [Fieldnames.TIMESTAMP, Fieldnames.PH, Fieldnames.EC, Fieldnames.DRAINAGE]
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

    def get_history_length(self):
        return self._historyLength

    def record_data_point(self, timestamp, phReading, ecReading, drainageReading):
        self._lastDataPoint =  {Fieldnames.TIMESTAMP: timestamp,
                                Fieldnames.PH: phReading,
                                Fieldnames.EC: ecReading,
                                Fieldnames.DRAINAGE: drainageReading}
        self.save_last_reading_csv()
        self.save_last_reading_db()

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