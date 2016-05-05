from abc import ABCMeta, abstractmethod

class Jugada(object):
	__metaclass__ = ABCMeta

	def __init__(self):
		self._accionActual = 0

#	@abstractmethod
#	def ejecutarCon(self, unEquipo):
#		pass

	def acciones(self):
		return self._acciones

	@abstractmethod
	def proximaAccion(self):
		pass

	@abstractmethod
	def nombre(self):
		pass
