from tinydb import TinyDB, Query
import csv

class SmartLysimeterModel():
    fieldnames = ["date_time", "pH", "EC", "Drainage Rate"]
    def __init__(self, dbFileName, csvFileName, n=10):
        self._lastDataPoint = {}
        self._lastNDataPoints = {}
        self._n = n
        self._db = TinyDB(dbFileName)
        self._csvFileName = csvFileName

    def record_data_point(self, dateTime, phReading, ecReading, drainageReading):
        self._lastDataPoint =  {"date_time": dateTime,
                                "pH": phReading,
                                "EC": ecReading,
                                "Drainage Rate": drainageReading}
        self.save_last_reading_csv()
        self.save_last_reading_db()

    def save_last_reading_csv(self):
        with open(self._csvFileName, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=SmartLysimeterModel.fieldnames)
            writer.writeheader()
            writer.writerow(self._lastDataPoint)
    def save_last_reading_db(self):
        self._db.insert(self._lastDataPoint)

    def get_last_reading(self):
        return self._lastDataPoint