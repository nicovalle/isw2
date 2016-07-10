from posicion import *
from equipo import *

class Alero(Posicion):
	def jugadorConPosicion(self, unEquipo):
		return unEquipo.alero()
