from posicion import *
from equipo import *

class Base(Posicion):
	def jugadorConPosicion(self, unEquipo):
		return unEquipo.base()
