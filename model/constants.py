from enum import Enum, auto

EC_MIN = 1.8
EC_MAX = 2.4
PH_MIN = 5.6
PH_MAX = 6.1
DR_MIN = 30
DR_MAX = 40

class Status(Enum):
    EC_MIN_REACHED = auto()
    EC_MAX_REACHED = auto()
    EC_IN_LIMITS = auto()
    PH_MIN_REACHED = auto()
    PH_MAX_REACHED = auto()
    PH_IN_LIMITS = auto()
    DR_MIN_REACHED = auto()
    DR_MAX_REACHED = auto()
    DR_IN_LIMITS = auto()
