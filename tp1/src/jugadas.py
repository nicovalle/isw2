from abc import ABCMeta, abstractmethod
from acciones import *

class ColectivaExterna(Jugada):
	def __init__(self, k, unEquipo):
		self._accionActual = 0
		self._acciones = [Pase()]*(k-1) + [TiroTresPuntos()]
		self._equipo = unEquipo

	def proximaAccion(self):
		self._accionActual += 1		# not so sure. ¿Y la primer jugada?
		return self._acciones[self._accionActual]

class ColectivaInterna(Jugada):
	def __init__(self, k, unEquipo):
		self._accionActual = 0
		self._acciones = [Pase()]*(k-1) + [TiroDosPuntos()]
		self._equipo = unEquipo

	def proximaAccion(self):
		pass

class MVP(Jugada):

	def __init__(self, k, unEquipo):
		self._accionActual = 0
		self._acciones = [Pase(), Tiro()]
		self._equipo = unEquipo

class Contraataque(Jugada):
	def __init__(self, k, unEquipo):
		self._acciones = [Tiro()]
		self._equipo = unEquipo

	def proximaAccion(self):
		pass

class HombreAHombre(Jugada):
	#la idea se entiende. habria que ver como resolver esto
	def defenderPase():
		pass

	def defenderTiro():
		pass

	def accionParaDefender(unaAccionOfensiva):
		return defenderCon(self)
