from abc import ABCMeta, abstractmethod

class Ofensiva(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def proximaAccionOfensiva(self, unContexto):
        pass

    @abstractmethod
    def elegirJugadorDistintoA(self, unJugador, unEquipo):
        pass

    @abstractmethod
    def elegirJugadorEntrePosiciones(self, unaListaDePosiciones, unEquipo):
        pass
