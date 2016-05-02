from abc import ABCMeta, abstractmethod

class ColectivaExterna(Jugada):
	def __init__(self, k):
		self._accionActual = 0

		# appendear k pases en acciones, por ultimo el tiro
		self._acciones = [Pase(), Pase(), Pase(), TiroTresPuntos()]

	def ejecutarCon(self, unEquipo):
		pass

	def acciones(self):
		return self._acciones

	def proximaAccion(self):
		pass
