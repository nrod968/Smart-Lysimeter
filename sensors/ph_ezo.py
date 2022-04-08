from enum import Enum
import time
from sensors.sensor import SmartLysimeterSensor
from utils.data_protocol import Protocol
from utils.uart import UART

class Command(str, Enum):
    READ = "R"
    STOP_CONTINUOUS = "C,0"
    CAL_DRY = "Cal,dry"
    CAL_LOW = "Cal,low,{0}"
    CAL_MID = "Cal,mid,{0}"
    SLEEP = "Sleep"

    def __str__(self) -> str:
        return str.__str__(self)

class PHSensor(SmartLysimeterSensor):
    def __init__(self, protocol, port):
        if (protocol == Protocol.UART):
            self._backend = UART(port)

    def get_datapoint(self):
        self._backend.send_cmd(Command.STOP_CONTINUOUS)
        time.sleep(1)
        self._backend._ser.flush()
        self._backend.send_cmd(Command.READ)
        lines = self._backend.read_lines()
        for i in range(len(lines)):
            if lines[-1 * (i + 1)][0] != b'*'[0]:
                return lines[-1 * (i + 1)].decode('utf-8')