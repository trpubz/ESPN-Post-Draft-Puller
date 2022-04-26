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
    OF2 = "OF2"
    OF3 = "OF3"
    DH = "DH"
    BN1 = "BN"
    BN2 = "BN2"
    BN3 = "BN3"
    BN4 = "BN4"
    BN5 = "BN5"
    SP1 = "SP"
    SP2 = "SP2"
    SP3 = "SP3"
    P1 = "P1"
    P2 = "P2"
    RP1 = "RP"
    RP2 = "RP2"


class Team:
    name: str
    roster: {RosSpot: Player} = {}

    def __init__(self, name):
        self.name = name

    def add_player(self, plyr: Player):
        # leftBench is a placeholder var for when a player needs to find a new pos
        leftBench: (Player, RosSpot) = ()  # used to store hitters
        penDawg: (Player, RosSpot) = ()  # used to store pitchers
        pos: list[str] = plyr.pos.split("/")
        temp = self.pencil_in_player(plyr, pos)
        # if temp is empty then player has successfully landed in a roster slot, exit
        if len(temp) == 0:
            return
        elif "P" in temp:
            penDawg = temp
        else:
            leftBench = temp

        if len(leftBench) > 0:
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
            posLBN: list[str] = leftBench[0].pos.split("/")
            posLBN.remove(leftBench[1].value)
            if posLBN is None:
                posLBN = ["DH"]
            _ = self.pencil_in_player(leftBench[0], posLBN)
        if len(penDawg) > 0:
            posPen: list[str] = penDawg[0].pos.split("/")
            posPen.remove(penDawg[1].value)
            _ = self.pencil_in_player(penDawg[0], posPen)

    def pencil_in_player(self, plyr: Player, lstPOS: list[str]) -> ():
        """
        :param plyr: Player object
        :param lstPOS: a list of POS strings
        """
        for pos in lstPOS:
            if pos == RosSpot.C.value:
                if self.roster.get(RosSpot.C) is None:
                    self.roster[RosSpot.C] = plyr
                    print(f"rostered {plyr.name} on {self.name} at {RosSpot.C}")
                    break
                # if the person in the roster spot was drafted for less money, bump them
                elif self.roster[RosSpot.C].draftedValue < plyr.draftedValue:
                    leftBench = (self.roster[RosSpot.C], RosSpot.C)
                    self.roster[RosSpot.C] = plyr
                    print(f"rostered {plyr.name} on {self.name} at {RosSpot.C}")
                    return leftBench
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
                # if the person in the roster spot was drafted for less money, bump them
                elif self.roster[RosSpot.IF2B].draftedValue < plyr.draftedValue:
                    leftBench = (self.roster[RosSpot.IF2B], RosSpot.IF2B)
                    self.roster[RosSpot.IF2B] = plyr
                    print(f"rostered {plyr.name} on {self.name} at {RosSpot.IF2B}")
                    return leftBench
            elif pos == RosSpot.IF3B.value:
                if self.roster.get(RosSpot.IF3B) is None:
                    self.roster[RosSpot.IF3B] = plyr
                    print(f"rostered {plyr.name} on {self.name} at {RosSpot.IF3B}")
                    break
                # if the person in the roster spot was drafted for less money, bump them
                elif self.roster[RosSpot.IF3B].draftedValue < plyr.draftedValue:
                    leftBench = (self.roster[RosSpot.IF3B], RosSpot.IF3B)
                    self.roster[RosSpot.IF3B] = plyr
                    print(f"rostered {plyr.name} on {self.name} at {RosSpot.IF3B}")
                    return leftBench
            elif pos == RosSpot.SS.value:
                if self.roster.get(RosSpot.SS) is None:
                    self.roster[RosSpot.SS] = plyr
                    print(f"rostered {plyr.name} on {self.name} at {RosSpot.SS}")
                    break
                # if the person in the roster spot was drafted for less money, bump them
                elif self.roster[RosSpot.SS].draftedValue < plyr.draftedValue:
                    leftBench = (self.roster[RosSpot.SS], RosSpot.SS)
                    self.roster[RosSpot.SS] = plyr
                    print(f"rostered {plyr.name} on {self.name} at {RosSpot.SS}")
                    return leftBench
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
                # if the person in the roster spot was drafted for less money, bump them
                elif self.roster[RosSpot.OF3].draftedValue < plyr.draftedValue:
                    leftBench = (self.roster[RosSpot.OF3], RosSpot.OF1)
                    self.roster[RosSpot.OF3] = plyr
                    print(f"rostered {plyr.name} on {self.name} at {RosSpot.OF3}")
                    return leftBench
                else:
                    lstPOS.append("DH")
            elif pos == RosSpot.DH.value:
                if self.roster.get(RosSpot.DH) is None:
                    self.roster[RosSpot.DH] = plyr
                    print(f"rostered {plyr.name} on {self.name} at {RosSpot.DH}")
                    break
                # if the person in the roster spot was drafted for less money, bump them
                elif self.roster[RosSpot.DH].draftedValue < plyr.draftedValue:
                    leftBench = (self.roster[RosSpot.DH], RosSpot.DH)
                    self.roster[RosSpot.DH] = plyr
                    print(f"rostered {plyr.name} on {self.name} at {RosSpot.DH}")
                    return leftBench
                else:
                    lstPOS.append("BN")
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
                else:
                    lstPOS.append("BN")
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
                else:
                    lstPOS.append("BN")
            elif pos == RosSpot.BN1.value:  # bench spots
                if self.roster.get(RosSpot.BN1) is None:
                    self.roster[RosSpot.BN1] = plyr
                    print(f"rostered {plyr.name} on {self.name} at {RosSpot.BN1}")
                    break
                elif self.roster.get(RosSpot.BN2) is None:
                    self.roster[RosSpot.BN2] = plyr
                    print(f"rostered {plyr.name} on {self.name} at {RosSpot.BN2}")
                    break
                elif self.roster.get(RosSpot.BN3) is None:
                    self.roster[RosSpot.BN3] = plyr
                    print(f"rostered {plyr.name} on {self.name} at {RosSpot.BN3}")
                    break
                elif self.roster.get(RosSpot.BN4) is None:
                    self.roster[RosSpot.BN4] = plyr
                    print(f"rostered {plyr.name} on {self.name} at {RosSpot.BN4}")
                    break
                elif self.roster.get(RosSpot.BN5) is None:
                    self.roster[RosSpot.BN5] = plyr
                    print(f"rostered {plyr.name} on {self.name} at {RosSpot.BN5}")
                    break
        return ()
