from abc import ABCMeta, abstractmethod
from acciones import *

class ColectivaExterna(Jugada):
	def __init__(self, k):
		self._accionActual = 0
		self._acciones = [Pase()]*(k-1) + [TiroTresPuntos()]

	def ejecutarCon(self, unEquipo):
		if (self._acciones[self._accionActual].umbralDeExito(unEquipo.base())):
			# ????
		pass

	def proximaAccion(self):
		self._accionActual += 1		# not so sure. ¿Y la primer jugada?
		return self._acciones[self._accionActual]

class ColectivaInterna(Jugada):
	def __init__(self, k):
		self._accionActual = 0
		self._acciones = [Pase()]*(k-1) + [TiroDosPuntos()]

	def ejecutarCon(self, unEquipo):
		pass

	def proximaAccion(self):
		pass

class MVP(Jugada):
	def __init__(self, k):
		self._accionActual = 0
		self._acciones = [Pase(), Tiro()]

class Contraataque(Jugada):
	def __init__(self, k):
		self._acciones = [Tiro()]

	def ejecutarCon(self, unEquipo):
		pass

	def proximaAccion(self):
		pass

# Me parece que esta no tiene sentido definirla
#class HombreAHombre(Jugada):
#	def __init__(self, k):
#		self._accionActual = 0
#		self._acciones = [Bloquear()]
#
#	def ejecutarCon(self, unEquipo):
#		pass
#
#	def proximaAccion(self):
#		pass
#
