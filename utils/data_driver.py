from datetime import datetime
from random import Random
from time import time

from controller.controller import SmartLysimeterController
from model.model import SmartLysimeterModel
from utils.driver import SmartLysimeterDriver
from utils.uart import UART, Port

class SmartLysimeterDataDriver(SmartLysimeterDriver):
    def __init__(self, controller: SmartLysimeterController):
        self._controller = controller
        self._randgen = Random()
        self._phIn = UART(Port.UART0)
        self._phDr = UART(Port.UART5)
        self._ecIn = UART(Port.UART2)
        self._ecDr = UART(Port.UART3)
    
    def generate_datapoint(self):
        phInVal = self._phIn.get_datapoint()
        ecInVal = self._ecIn.get_datapoint()
        phDrVal = self._phDr.get_datapoint()
        ecDrVal = self._ecDr.get_datapoint()
        drainage = self._randgen.gauss(mu=35.0, sigma=2.0)
        timestamp = datetime.now()
        self._controller.record_data_point(timestamp, phInVal, ecInVal, phDrVal, ecDrVal, drainage)