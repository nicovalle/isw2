from abc import ABCMeta, abstractmethod

from accion import *

class AccionOfensiva(Accion):
	__metaclass__ = ABCMeta

	@abstractmethod
	def jugadorEjecutante(self):
		pass

    @abstractmethod
    def defenderCon(self, unaJugadaDefensiva, unJugador):
        pass

	@abstractmethod
	def resolvedorPara(self, unSimulador):
		pass
