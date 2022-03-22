from datetime import datetime
from random import Random
from time import time

from controller.controller import SmartLysimeterController
from model.model import SmartLysimeterModel

class SmartLysimeterDriver():
    def __init__(self, model: SmartLysimeterModel):
        self._model = model
        self._randgen = Random()
    
    def generate_datapoint(self):
        ph = self._randgen.gauss(mu=5.85, sigma=0.15)
        ec = self._randgen.gauss(mu=2.1, sigma=0.15)
        drainage = self._randgen.gauss(mu=35.0, sigma=2.0)
        #timestamp = str(datetime.now())
        timestamp = time()
        self._model.record_data_point(timestamp, ph, ec, drainage)