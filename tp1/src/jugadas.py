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
		accion = self._acciones[self._accionActual]
		self._accionActual += 1
		return accion

	def nombre(self):
		return self._nombre

class ColectivaInterna(Jugada):
	def __init__(self, unEquipo, k=5):
		self._accionActual = 0
		self._acciones = [Pase()]*(k-1) + [TiroDosPuntos()]
		self._equipo = unEquipo
		self._nombre = "Colectiva Interna"

	def proximaAccion(self):
		accion = self._acciones[self._accionActual]
		self._accionActual += 1
		return accion

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
		self._nombre = "MVP"

	def proximaAccion(self):
		accion = self._acciones[self._accionActual]
		self._accionActual += 1
		return accion

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
		self._nombre = "Contraataque"

	def proximaAccion(self):
		accion = self._acciones[0]
		return accion

	def nombre(self):
		return self._nombre

	def comenzarJugada(self):
		print self._nombre+" meEjecuto con "+self._equipo.nombre()

class HombreAHombre(Jugada):
	def __init__(self, unEquipo):
		self._nombre = 'Hombre a Hombre'
		pass

	def proximaAccion(self):
		pass

	### TODO -> la idea se entiende. habria que ver como resolver esto
	def defenderPase(self):
		return Robar()

	def defenderTiro(self):
		return Bloqueo()

	def accionParaDefender(self, unaAccionOfensiva):
		return unaAccionOfensiva.defenderCon(self)

	def nombre(self):
		return self._nombre
