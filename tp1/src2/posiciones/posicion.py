from abc import ABCMeta, abstractmethod

class Posicion(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def jugadorConPosicion(self, unEquipo):
        pass
