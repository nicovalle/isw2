from posicion import *
from equipo import *

class Pivot(Posicion):
	def jugadorConPosicion(self, unEquipo):
		return unEquipo.pivot()
