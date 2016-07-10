from abc import ABCMeta, abstractmethod

class Posicion(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        pass

    def __eq__(self, other):
        return self._nombre == other._nombre

    def __ne__(self, other):
        return not self.__eq__(other)

    @abstractmethod
    def jugadorConPosicion(self, unEquipo):
        pass

from base import *
from escolta import *
from alapivot import *
from pivot import *
from alero import *
