import equipo
import random

class Tecnico(object):

	def __init__(self, unNombre, unApellido, unLibroDeJugadas):
		self._nombre = unNombre
		self._apellido = unApellido
		self._libroDeJugadas = unLibroDeJugadas

	def nombre(self):
		return self._nombre

	def apellido(self):
		return self._apellido

	def libroDeJugadas(self):
		return self._libroDeJugadas

	def elegirJugadaOfensiva(self, unEquipo):
		unaJugadaOfensiva = self._libroDeJugadas.jugadaOfensiva()
		unEquipo.ejecutarJugada(unaJugadaOfensiva)

	def elegirJugadaDefensiva(self, unEquipo):
		unaJugadaDefensiva = self._libroDeJugadas.jugadaDefensiva()
		unEquipo.ejecutarJugada(unaJugadaDefensiva)
