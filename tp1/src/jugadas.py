#from abc import ABCMeta, abstractmethod
from jugada import *
from acciones import *

class ColectivaExterna(Jugada):
	def __init__(self, unEquipo, k=5):
		self._accionActual = 0
		self._acciones = [Pase()]*(k-1) + [TiroTresPuntos()]
		self._equipo = unEquipo
		self._nombre = "Colectiva Externa"

	def proximaAccion(self):
		self._accionActual += 1	# not so sure. Y la primer jugada?
		return self._acciones[self._accionActual]

	def nombre(self):
		return self._nombre

	def comenzarJugada(self):
		print self._nombre+" meEjecuto con "+self._equipo.nombre()

class ColectivaInterna(Jugada):
	def __init__(self, unEquipo, k=5):
		self._accionActual = 0
		self._acciones = [Pase()]*(k-1) + [TiroDosPuntos()]
		self._equipo = unEquipo
		self._nombre = "Colectiva Externa"

	def proximaAccion(self):
		pass

	def nombre(self):
		return self._nombre

	def comenzarJugada(self):
		print self._nombre+" meEjecuto con "+self._equipo.nombre()

class MVP(Jugada):
	def __init__(self, unEquipo, k=0):
		self._accionActual = 0

		### TODO -> ESTO ESTA MAL, HAY QUE VER COMO ABSTRAERLO
		moneda = random.random()
		if(moneda > 0.5):
			self._acciones = [Pase(), TiroDosPuntos()]
		else:
			self._acciones = [Pase(), TiroTresPuntos()]

		self._equipo = unEquipo
		self._nombre = "Colectiva Externa"

	def proximaAccion(self):
		pass

	def nombre(self):
		return self._nombre

	def comenzarJugada(self):
		print self._nombre+" meEjecuto con "+self._equipo.nombre()

class Contraataque(Jugada):
	def __init__(self, unEquipo, k=0):

		### TODO -> ESTO ESTA MAL, HAY QUE VER COMO ABSTRAERLO
		moneda = random.random()
		if(moneda > 0.5):
			self._acciones = [TiroDosPuntos()]
		else:
			self._acciones = [TiroTresPuntos()]

		self._equipo = unEquipo
		self._nombre = "Colectiva Externa"

	def proximaAccion(self):
		pass

	def nombre(self):
		return self._nombre

	def comenzarJugada(self):
		print self._nombre+" meEjecuto con "+self._equipo.nombre()

class HombreAHombre(Jugada):
	def __init__(self, unEquipo):
		pass

	### TODO -> la idea se entiende. habria que ver como resolver esto
	def proximaAccion(self):
		pass

	def defenderPase():
		pass

	def defenderTiro():
		pass

	def accionParaDefender(unaAccionOfensiva):
		return defenderCon(self)

	def nombre(self):
		return self._nombre
