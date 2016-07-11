import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir)

from abc import ABCMeta, abstractmethod

from posiciones import posicion
from acciones import accion
import random

class Ofensiva(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def nombre(self):
        pass

    @abstractmethod
    def proximaAccionOfensiva(self, unContexto):
        pass

    def elegirJugadorDistintoA(self, unJugador, unEquipo):
        return unEquipo.jugadorDistintoA(unJugador)

    def elegirJugadorEntrePosicionesDistintoA(self, unaListaDePosiciones, unJugador, unEquipo):
        return unEquipo.jugadorEntrePosicionesDistintoA(unaListaDePosiciones, unJugador)

from ofensivaColectiva import *
from ofensivaColectiva2KPases import *
from ofensivaColectiva3KPases import *
from ofensivaMVP import *
from ofensivaContraataque import *
