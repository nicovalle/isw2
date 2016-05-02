import random
class LibroDeJugadas(object):

	def __init__(self, unDiccDeJugadasOfensivasYFrecuencia, unDiccDeJugadasDefensivasYFrecuencia):
		self._jugadasOfensivas = unDiccDeJugadasOfensivasYFrecuencia
		self._jugadasDefensivas = unDiccDeJugadasDefensivasYFrecuencia

	def jugadaOfensiva(self):
		return self.elegirJugada(self._jugadasOfensivas)

	def jugadaDefensiva(self):
		return self.elegirJugada(self._jugadasDefensivas)

	def elegirJugada(self, unDiccDeJugadasYFrecuencia):
		freq = random.random()
		accum = 0
		for key in unDiccDeJugadasYFrecuencia.keys():
			accum += unDiccDeJugadasYFrecuencia[key]
			if(freq < accum):
				return key
