# Team Model
# by pubins.taylor
# v0.1
# created DD MMM YYYY
# lastUpdate DD MMM YYYY

from enum import Enum
import Player


class Team:
    name: str
    roster: [{Enum: Player}]

    def __init__(self, name):
        self.name = name


class RosSpot(Enum):
    C = "C"
    IF1B = "IF1B"
    IF2B = "IF2B"
    IF3B = "IF3B"
    SS = "SS"
    OF1 = "OF1"
    OF2 = "OF2"
    OF3 = "OF3"
    DH = "DH"
    BN1 = "BN1"
    BN2 = "BN2"
    BN3 = "BN3"
    BN4 = "BN4"
    BN5 = "BN5"
    SP1 = "SP1"
    SP2 = "SP2"
    SP3 = "SP3"
    P1 = "P1"
    P2 = "P2"
    RP1 = "RP1"
    RP2 = "RP2"
