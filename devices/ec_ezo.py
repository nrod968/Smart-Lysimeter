from enum import Enum
import time
from devices.sensor import SmartLysimeterSensor
from utils.data_protocol import Protocol
from utils.uart import UART

class ECCommand(str, Enum):
    READ = "R"
    STOP_CONTINUOUS = "C,0"
    CAL_DRY = "Cal,dry"
    CAL = "Cal,{0}"
    SLEEP = "Sleep"

    def __str__(self) -> str:
        return str.__str__(self)

class ECSensor(SmartLysimeterSensor):
    def __init__(self, protocol, port):
        if (protocol == Protocol.UART):
            self._backend = UART(port)

    def read(self):
        self._backend.send_cmd(str(ECCommand.STOP_CONTINUOUS))
        time.sleep(1)
        self._backend._ser.flush()
        self._backend.send_cmd(str(ECCommand.READ))
        while(True):
            lines = self._backend.read_lines()
            for i in range(len(lines)):
                if lines[-1 * (i + 1)][0] != b'*'[0]:
                    return lines[-1 * (i + 1)].decode('utf-8')
            time.sleep(0.1)

    def calibrate(self, calType, calVal):
        if (calType == ECCommand.CAL_DRY):
            self._backend.send_cmd(calType)
        else:
            self._backend.send_cmd(str(calType).format(calVal))
