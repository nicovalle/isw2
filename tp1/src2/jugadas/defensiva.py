import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir)

from acciones import *

from abc import ABCMeta, abstractmethod

class Defensiva(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def accionParaDefender(self, unaAccionOfensiva, unContexto):
        pass

    @abstractmethod
    def defenderPase(self, unaAccionOfensiva, unJugador):
        pass

    @abstractmethod
    def defenderTiro(self, unaAccionOfensiva, unJugador):
        pass
