# Team Model
# by pubins.taylor
# v0.1
# created DD MMM YYYY
# lastUpdate DD MMM YYYY

from enum import Enum
import Player


class RosSpot(Enum):
    C = "C"
    IF1B = "1B"
    IF2B = "2B"
    IF3B = "3B"
    SS = "SS"
    OF1 = "OF"
    OF2 = "OF"
    OF3 = "OF"
    DH = "DH"
    BN1 = "BN1"
    BN2 = "BN2"
    BN3 = "BN3"
    BN4 = "BN4"
    BN5 = "BN5"
    SP1 = "SP"
    SP2 = "SP"
    SP3 = "SP"
    P1 = "P1"
    P2 = "P2"
    RP1 = "RP"
    RP2 = "RP"


class Team:
    name: str
    roster: {RosSpot: Player} = {}

    def __init__(self, name):
        self.name = name

    def add_player(self, plyr: Player, draftValue: int):
        # leftBench is a placeholder var for when a player needs to find a new pos
        leftBench: (Player, RosSpot)
        for pos in plyr.pos.split(", "):
            if pos == RosSpot.C.value:
                if self.roster[RosSpot.C] is None:
                    self.roster[RosSpot.C] = plyr
                    break
            elif pos == RosSpot.IF1B.value:
                if self.roster[RosSpot.IF1B] is None:
                    self.roster[RosSpot.IF1B] = plyr
                    break
                elif self.roster[RosSpot.IF1B].draftedValue < draftValue:
                    leftBench = (self.roster[RosSpot.IF1B], RosSpot.IF1B)
                    self.roster[RosSpot.IF1B] = plyr
                    break
            elif pos == RosSpot.IF2B.value:
                if self.roster[RosSpot.IF2B] is None:
                    self.roster[RosSpot.IF2B] = plyr
                    break
            elif pos == RosSpot.IF3B.value:
                if self.roster[RosSpot.IF3B] is None:
                    self.roster[RosSpot.IF3B] = plyr
                    break
            elif pos == RosSpot.SS.value:
                if self.roster.get(RosSpot.SS) is None:
                    self.roster[RosSpot.SS] = plyr
                    break
            elif pos == RosSpot.OF1.value:
                if self.roster[RosSpot.OF1] is None:
                    self.roster[RosSpot.OF1] = plyr
                    break
                elif self.roster[RosSpot.OF2] is None:
                    self.roster[RosSpot.OF2] = plyr
                    break
                elif self.roster[RosSpot.OF3] is None:
                    self.roster[RosSpot.OF3] = plyr
                    break
            elif pos == RosSpot.DH.value:
                if self.roster[RosSpot.DH] is None:
                    self.roster[RosSpot.DH] = plyr
                    break

        if leftBench is None:
            return

        posLBN: [str] = leftBench[0].pos.split(", ").remove(leftBench[1].value)
