import random
import importlib

class LibroDeJugadas(object):

	def __init__(self, unDiccDeJugadasOfensivasYFrecuencia, unDiccDeJugadasDefensivasYFrecuencia):
		self._jugadasOfensivas = unDiccDeJugadasOfensivasYFrecuencia
		self._jugadasDefensivas = unDiccDeJugadasDefensivasYFrecuencia

	def obtenerCreadorJugadaOfensiva(self):
		return self.elegirCreadorJugadaConsiderandoFrecuencia(self._jugadasOfensivas)

	def obtenerCreadorJugadaDefensiva(self):
		return self.elegirCreadorJugadaConsiderandoFrecuencia(self._jugadasDefensivas)

	def elegirCreadorJugadaConsiderandoFrecuencia(self, unDiccDeJugadasYFrecuencia):
		freq = random.random()
		accum = 0
		for key in unDiccDeJugadasYFrecuencia.keys():
			accum += unDiccDeJugadasYFrecuencia[key]
			if(freq < accum):
				module = importlib.import_module('jugadas')
				return getattr(module, key)
