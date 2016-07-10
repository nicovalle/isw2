class Estadisticas(object):
    def __init__(self, unFGP, un3PP, unRPG, unAPG, unBPG, unSPG, unTO, unPPG):
        self._fgp = unFGP
        self.__3pp = un3PP
        self._rpg = unRPG
        self._apg = unAPG
        self._bpg = unBPG
        self._spg = unSPG
        self._to = unTO
        self._ppg = unPPG

    def fgp(self):
        return self._fgp

    def _3pp(self):
        return self.__3pp

    def rpg(self):
        return self._rpg

    def apg(self):
        return self._apg

    def bpg(self):
        return self._bpg

    def spg(self):
        return self._spg

    def to(self):
        return self._to

    def ppg(self):
        return self._ppg
