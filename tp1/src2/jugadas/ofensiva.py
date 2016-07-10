import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir)

from abc import ABCMeta, abstractmethod

from posiciones import *
from acciones import *
import random

class Ofensiva(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def proximaAccionOfensiva(self, unContexto):
        pass

    def elegirJugadorDistintoA(self, unJugador, unEquipo):
        return unEquipo.jugadorDistintoA(unJugador)

    def elegirJugadorEntrePosiciones(unaListaDePosiciones, unEquipo):
        return unEquipo.jugadorEnPosiciones(listaDePosiciones)
