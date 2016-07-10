from posicion import *
from equipo import *

class Escolta(Posicion):
	def jugadorConPosicion(self, unEquipo):
		return unEquipo.escolta()
