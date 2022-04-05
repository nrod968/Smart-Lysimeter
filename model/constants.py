from enum import Enum, auto

EC_MIN = 1.8
EC_MAX = 2.4
PH_MIN = 5.6
PH_MAX = 6.1
DR_MIN = 30
DR_MAX = 40

NUM_TICKS = 10
EC_MAX_TICK = 2.8
EC_MIN_TICK = 1.3
EC_TICK_LEN = (EC_MAX_TICK - EC_MIN_TICK) / NUM_TICKS
PH_MAX_TICK = 6.5
PH_MIN_TICK = 5.0
PH_TICK_LEN = (PH_MAX_TICK - PH_MIN_TICK) / NUM_TICKS
DR_MAX_TICK = 50
DR_MIN_TICK = 20
DR_TICK_LEN = (DR_MAX_TICK - DR_MIN_TICK) / NUM_TICKS

class Status(Enum):
    EC_IN_MIN_REACHED = auto()
    EC_IN_MAX_REACHED = auto()
    EC_IN_WITHIN_LIMITS = auto()
    EC_DR_MIN_REACHED = auto()
    EC_DR_MAX_REACHED = auto()
    EC_DR_WITHIN_LIMITS = auto()
    PH_IN_MIN_REACHED = auto()
    PH_IN_MAX_REACHED = auto()
    PH_IN_WITHIN_LIMITS = auto()
    PH_DR_MIN_REACHED = auto()
    PH_DR_MAX_REACHED = auto()
    PH_DR_WITHIN_LIMITS = auto()
    DR_MIN_REACHED = auto()
    DR_MAX_REACHED = auto()
    DR_WITHIN_LIMITS = auto()
    TANK_TOO_FULL = auto()
    TANK_WITHIN_LIMITS = auto()
