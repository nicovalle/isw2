from abc import ABCMeta, abstractmethod

from accion import *

class AccionDefensiva(Accion):
	__metaclass__ = ABCMeta

	@abstractmethod
	def jugadorEjecutante(self):
		pass

	@abstractmethod
	def resolvedorPara(self, unSimulador):
		pass
