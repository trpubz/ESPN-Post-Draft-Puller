# Player Model
# by pubins.taylor
# v0.3
# created 20 APR 2022
# TODO: add player stats as properties; need to create logic for subclassing hitters/pitchers
# lastUpdate 26 APR 2022

from collections import namedtuple
from json import JSONEncoder


class Player:

    def __init__(self, espnid, fgid, name, pos, tm):
        self.idESPN = espnid
        self.idFangraphs = fgid
        self.name = name
        self.pos = pos
        self.tm = tm
        self.draftedTeam: str = ""
        self.draftedValue: int = 0

    def set_draft_details(self, tm: str, value: str):
        """
        Updates the player properties draftedTeam and draftedValue
        :param tm: Drafting team name
        :param value: Winning auction value
        """
        self.draftedTeam = tm
        self.draftedValue = value

    def __eq__(self, other: (str, str)):
        if self.name == other[0] and self.tm == self.team_map(other[1]):
            return True
        else:
            return False

    @staticmethod
    def team_map(tm: str) -> str:
        """
        ESPN likes to use weird MLB Team abbreviations.  This reference function aligns MLB abbreviations with TRPKeys.
        :param tm: the player's MLB tm that EPSN uses on the Draft Recap page
        :return: the corrected string in-line with TRPKeys
        """
        if tm == "CHW":
            return "CWS"
        elif tm == "KCR":
            return "KC"
        elif tm == "SDP":
            return "SD"
        elif tm == "SFG":
            return "SF"
        elif tm == "WSN":
            return "WSH"
        else:
            return tm

