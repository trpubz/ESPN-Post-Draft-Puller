# Player Model
# by pubins.taylor
# v0.1
# created DD MMM YYYY
# lastUpdate DD MMM YYYY

from collections import namedtuple
from json import JSONEncoder


class Player:
    idESPN: str
    idFangraphs: str
    name: str
    pos: str
    tm: str
    draftedTeam: str
    draftedValue: str

    def __init__(self, espnid, fgid, name, pos, tm):
        self.idESPN = espnid
        self.idFangraphs = fgid
        self.name = name
        self.pos = pos
        self.tm = tm

    def set_draft_details(self, tm: str, value: str):
        self.draftedTeam = tm
        self.draftedValue = value

    def __eq__(self, other: (str, str)):
        if self.name == other[0] and self.tm == other[1]:
            return True
        else:
            return False


#
# def customPlayerDecoder(dictPlayer):
#     return namedtuple('X', dictPlayer.keys())(*dictPlayer.values())

#
# class PlayerEncoder(JSONEncoder):
#     def default(self, o):
#         return o.__dict__
