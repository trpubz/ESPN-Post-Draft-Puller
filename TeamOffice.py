# Team Model
# by pubins.taylor
# v0.2
# created 20 APR 2022
# refactored for generic roster placement
# lastUpdate 26 APR 2022

from enum import Enum
import Player


class Team:
    name: str
    roster: {str: Player} = {}

    def __init__(self, name):
        self.name = name

    def add_player(self, plyr: Player):
        """

        :param plyr: Player object
        """
        if "P" in plyr.pos:
            if "SP" in plyr.pos:
                if self.roster.get("SP1") is None:
                    self.roster["SP1"] = plyr
                elif self.roster.get("SP2") is None:
                    self.roster["SP2"] = plyr
                elif self.roster.get("SP3") is None:
                    self.roster["SP3"] = plyr
                elif self.roster.get("P1") is None:
                    self.roster["P1"] = plyr
                elif self.roster.get("P2") is None:
                    self.roster["P2"] = plyr
                else:
                    self.bench_guy(plyr)
            elif "RP" in plyr.pos:
                if self.roster.get("RP1") is None:
                    self.roster["RP1"] = plyr
                elif self.roster.get("RP2") is None:
                    self.roster["RP2"] = plyr
                elif self.roster.get("P1") is None:
                    self.roster["P1"] = plyr
                elif self.roster.get("P2") is None:
                    self.roster["P2"] = plyr
                else:
                    self.bench_guy(plyr)
        else:
            if self.roster.get("BAT1") is None:
                self.roster["BAT1"] = plyr
                print(f"rostered {plyr.name} on {self.name} at BAT1")
            elif self.roster.get("BAT2") is None:
                self.roster["BAT2"] = plyr
                print(f"rostered {plyr.name} on {self.name} at BAT2")
            elif self.roster.get("BAT3") is None:
                self.roster["BAT3"] = plyr
                print(f"rostered {plyr.name} on {self.name} at BAT3")
            elif self.roster.get("BAT4") is None:
                self.roster["BAT4"] = plyr
                print(f"rostered {plyr.name} on {self.name} at BAT4")
            elif self.roster.get("BAT5") is None:
                self.roster["BA5"] = plyr
                print(f"rostered {plyr.name} on {self.name} at BAT5")
            elif self.roster.get("BAT6") is None:
                self.roster["BAT6"] = plyr
                print(f"rostered {plyr.name} on {self.name} at BAT6")
            elif self.roster.get("BAT7") is None:
                self.roster["BAT7"] = plyr
                print(f"rostered {plyr.name} on {self.name} at BAT7")
            elif self.roster.get("BAT8") is None:
                self.roster["BAT8"] = plyr
                print(f"rostered {plyr.name} on {self.name} at BAT8")
            elif self.roster.get("BAT9") is None:
                self.roster["BAT9"] = plyr
                print(f"rostered {plyr.name} on {self.name} at BAT9")
            else:
                self.bench_guy(plyr)

    def bench_guy(self, plyr: Player):
        if self.roster.get("BN1") is None:
            self.roster["BN1"] = plyr
        elif self.roster.get("BN2") is None:
            self.roster["BN2"] = plyr
        elif self.roster.get("BN3") is None:
            self.roster["BN3"] = plyr
        elif self.roster.get("BN4") is None:
            self.roster["BN4"] = plyr
        else:
            self.roster["BN5"] = plyr
