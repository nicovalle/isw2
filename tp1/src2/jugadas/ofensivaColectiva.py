from ofensiva import *

from abc import ABCMeta, abstractmethod

class OfensivaColectiva(Ofensiva):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def proximaAccionOfensiva(self, unContexto):
        pass
