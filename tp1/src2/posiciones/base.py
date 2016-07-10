from posicion import Posicion

class Base(Posicion):
	def jugadorConPosicion(self, unEquipo):
		return unEquipo.base()
