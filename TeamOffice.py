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

    def add_player(self, plyr: Player):
        # leftBench is a placeholder var for when a player needs to find a new pos
        leftBench: (Player, RosSpot) = ()  # used to store hitters
        penDawg: (Player, RosSpot) = ()  # used to store pitchers
        pos = plyr.pos.split(", ")
        temp = self.pencil_in_player(plyr, pos)
        if len(temp) == 0:
            return
        elif "P" in temp:
            penDawg = temp
        else:
            leftBench = temp

        if leftBench is not None:
            # if len(leftBench(1)) == 1:
            #     if self.roster.get(RosSpot.DH) is None:
            #         self.roster[RosSpot.DH] = plyr
            #     elif self.roster.get(RosSpot.BN1) is None:
            #         self.roster[RosSpot.BN1] = plyr
            #     elif self.roster.get(RosSpot.BN2) is None:
            #         self.roster[RosSpot.BN2] = plyr
            #     elif self.roster.get(RosSpot.BN3) is None:
            #         self.roster[RosSpot.BN3] = plyr
            #     elif self.roster.get(RosSpot.BN4) is None:
            #         self.roster[RosSpot.BN4] = plyr
            #     else:
            #         self.roster[RosSpot.BN5] = plyr
            posLBN: [str] = leftBench[0].pos.split(", ").remove(leftBench[1].value)
            _ = self.pencil_in_player(plyr, posLBN)
        if penDawg is not None:
            posPen: [str] = penDawg[0].pos.split(", ").remove(penDawg[1].value)
            _ = self.pencil_in_player(plyr, posPen)

    def pencil_in_player(self, plyr: Player, pos: [str]) -> ():
        for pos in pos:
            if pos == RosSpot.C.value:
                if self.roster.get(RosSpot.C) is None:
                    self.roster[RosSpot.C] = plyr
                    print(f"rostered {plyr.name} on {self.name} at {RosSpot.C}")
                    break
            elif pos == RosSpot.IF1B.value:
                if self.roster.get(RosSpot.IF1B) is None:
                    self.roster[RosSpot.IF1B] = plyr
                    print(f"rostered {plyr.name} on {self.name} at {RosSpot.IF1B}")
                    break
                # if the person in the roster spot was drafted for less money, bump them
                elif self.roster[RosSpot.IF1B].draftedValue < plyr.draftedValue:
                    leftBench = (self.roster[RosSpot.IF1B], RosSpot.IF1B)
                    self.roster[RosSpot.IF1B] = plyr
                    print(f"rostered {plyr.name} on {self.name} at {RosSpot.IF1B}")
                    return leftBench
            elif pos == RosSpot.IF2B.value:
                if self.roster.get(RosSpot.IF2B) is None:
                    self.roster[RosSpot.IF2B] = plyr
                    print(f"rostered {plyr.name} on {self.name} at {RosSpot.IF2B}")
                    break
            elif pos == RosSpot.IF3B.value:
                if self.roster.get(RosSpot.IF3B) is None:
                    self.roster[RosSpot.IF3B] = plyr
                    print(f"rostered {plyr.name} on {self.name} at {RosSpot.IF3B}")
                    break
            elif pos == RosSpot.SS.value:
                if self.roster.get(RosSpot.SS) is None:
                    self.roster[RosSpot.SS] = plyr
                    print(f"rostered {plyr.name} on {self.name} at {RosSpot.SS}")
                    break
            elif pos == RosSpot.OF1.value:
                if self.roster.get(RosSpot.OF1) is None:
                    self.roster[RosSpot.OF1] = plyr
                    print(f"rostered {plyr.name} on {self.name} at {RosSpot.OF1}")
                    break
                elif self.roster.get(RosSpot.OF2) is None:
                    self.roster[RosSpot.OF2] = plyr
                    print(f"rostered {plyr.name} on {self.name} at {RosSpot.OF2}")
                    break
                elif self.roster.get(RosSpot.OF3) is None:
                    self.roster[RosSpot.OF3] = plyr
                    print(f"rostered {plyr.name} on {self.name} at {RosSpot.OF3}")
                    break
            elif pos == RosSpot.DH.value:
                if self.roster.get(RosSpot.DH) is None:
                    self.roster[RosSpot.DH] = plyr
                    print(f"rostered {plyr.name} on {self.name} at {RosSpot.DH}")
                    break
            elif pos == RosSpot.SP1.value:
                if self.roster.get(RosSpot.SP1) is None:
                    self.roster[RosSpot.SP1] = plyr
                    print(f"rostered {plyr.name} on {self.name} at {RosSpot.SP1}")
                    break
                elif self.roster.get(RosSpot.SP2) is None:
                    self.roster[RosSpot.SP2] = plyr
                    print(f"rostered {plyr.name} on {self.name} at {RosSpot.SP2}")
                    break
                elif self.roster.get(RosSpot.SP3) is None:
                    self.roster[RosSpot.SP3] = plyr
                    print(f"rostered {plyr.name} on {self.name} at {RosSpot.SP3}")
                    break
                elif self.roster.get(RosSpot.P1) is None:
                    self.roster[RosSpot.P1] = plyr
                    print(f"rostered {plyr.name} on {self.name} at {RosSpot.P1}")
                    break
                elif self.roster.get(RosSpot.P2) is None:
                    self.roster[RosSpot.P2] = plyr
                    print(f"rostered {plyr.name} on {self.name} at {RosSpot.P2}")
                    break
            elif pos == RosSpot.RP1.value:
                if self.roster.get(RosSpot.RP1) is None:
                    self.roster[RosSpot.RP1] = plyr
                    print(f"rostered {plyr.name} on {self.name} at {RosSpot.RP1}")
                    break
                elif self.roster.get(RosSpot.RP2) is None:
                    self.roster[RosSpot.RP2] = plyr
                    print(f"rostered {plyr.name} on {self.name} at {RosSpot.RP2}")
                    break
                elif self.roster.get(RosSpot.P1) is None:
                    self.roster[RosSpot.P1] = plyr
                    print(f"rostered {plyr.name} on {self.name} at {RosSpot.P1}")
                    break
                elif self.roster.get(RosSpot.P2) is None:
                    self.roster[RosSpot.P2] = plyr
                    print(f"rostered {plyr.name} on {self.name} at {RosSpot.P2}")
                    break
        return ()
