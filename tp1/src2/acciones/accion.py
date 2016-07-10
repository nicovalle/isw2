from abc import ABCMeta, abstractmethod

class Accion(object):
	__metaclass__ = ABCMeta

	@abstractmethod
	def jugadorEjecutante(self, unJugador):
		pass
