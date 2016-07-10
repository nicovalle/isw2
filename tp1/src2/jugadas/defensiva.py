from abc import ABCMeta, abstractmethod

class Defensiva(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, unNombre, unApellido, unLibroDeJugadas):
        pass

    @abstractmethod
    def accionParaDefender(self, unaAccionOfensiva, unContexto):
        pass

    @abstractmethod
    def defenderPase(self, unaAccionOfensiva, unJugador):
        pass

    @abstractmethod
    def defenderTiro(self, unaAccionOfensiva, unJugador):
        pass
