from tinydb import TinyDB, Query
import csv

class SmartLysimeterModel():
    fieldnames = ["date_time", "pH", "EC", "Drainage Rate"]
    def __init__(self, dbFileName, csvFileName, numRecords=10):
        self._lastDataPoint = {}
        self._lastNDataPoints = {}
        self._numRecords = numRecords
        self._db = TinyDB(dbFileName)
        self._csvFileName = csvFileName
        self._currRecord = 0

    def set_num_records(self, num_records):
        self._numRecords = num_records

    def get_num_records(self):
        return self._numRecords

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
        self._currRecord = self._db.insert(self._lastDataPoint)

    def get_last_reading(self):
        return self._lastDataPoint

    def get_last_n_readings(self):
        readings = []
        for i in range(self._numRecords):
            if (i > self._numRecords):
                break
            readings.append(self._db.get(doc_id=(self._currRecord - i)))
        readings.reverse()
        return readings