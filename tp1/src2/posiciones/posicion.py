from abc import ABCMeta, abstractmethod

class Posicion(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def jugadorConPosicion(self, unEquipo):
        pass

from base import *
from escolta import *
from alapivot import *
from pivot import *
from alero import *
