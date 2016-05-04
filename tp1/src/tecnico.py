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

	def seleccionarJugadaOfensiva(self):
		#unaJugadaOfensiva = 
		return self._libroDeJugadas.obtenerCreadorJugadaOfensiva()
		#unEquipo.ejecutarJugada(unaJugadaOfensiva)

	def seleccionarJugadaDefensiva(self):
		#unaJugadaDefensiva = 
		return self._libroDeJugadas.obtenerCreadorJugadaDefensiva()
		
		#unEquipo.ejecutarJugada(unaJugadaDefensiva)
