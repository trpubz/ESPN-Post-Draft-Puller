# Player Model
# by pubins.taylor
# v0.1
# created DD MMM YYYY
# lastUpdate DD MMM YYYY


class Player:
    espnid: str
    name: str
    pos: str
    draftedValue: str

    def __init__(self, espnid, name, pos, draftedValue):
        self.espnid = espnid
        self.name = name
        self.pos = pos
        self.draftedValue = draftedValue
