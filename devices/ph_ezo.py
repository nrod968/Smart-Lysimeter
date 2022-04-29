from enum import Enum
import time
from weakref import CallableProxyType
from devices.sensor import Calibration, SmartLysimeterSensor
from utils.data_protocol import Protocol
from utils.uart import UART

class PHCommand(str, Enum):
    READ = "R"
    STOP_CONTINUOUS = "C,0"
    CAL_LOW = "Cal,low,{0}"
    CAL_MID = "Cal,mid,{0}"
    SLEEP = "Sleep"

    def __str__(self) -> str:
        return str.__str__(self)

class PHSensor(SmartLysimeterSensor):
    def __init__(self, protocol, port):
        if (protocol == Protocol.UART):
            self._backend = UART(port)

    def read(self):
        self._backend.send_cmd(str(PHCommand.STOP_CONTINUOUS))
        time.sleep(1)
        self._backend._ser.flush()
        self._backend.send_cmd(str(PHCommand.READ))
        while(True):
            lines = self._backend.read_lines()
            for i in range(len(lines)):
                if lines[-1 * (i + 1)][0] != b'*'[0]:
                    return lines[-1 * (i + 1)].decode('utf-8')
            time.sleep(0.1)
    
    def calibrate(self, calType, calVal):
        if (calType == Calibration.MID):
            self._backend.send_cmd(str(PHCommand.CAL_MID).format(calVal))
        elif (calType == Calibration.LOW):
            self._backend.send_cmd(str(PHCommand.CAL_LOW).format(calVal))
