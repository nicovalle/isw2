import equipo
import random

class Jugador(object):

	def __init__(self, unNombre, unApellido):
		self._nombre = unNombre
		self._apellido = unApellido

	def nombre(self):
		return self._nombre

	def apellido(self):
		return self._apellido

	def nombreCompleto(self):
		return self._nombre+" "+self._apellido
