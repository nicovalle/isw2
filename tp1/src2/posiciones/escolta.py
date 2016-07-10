from posicion import Posicion

class Escolta(Posicion):
	def jugadorConPosicion(self, unEquipo):
		return unEquipo.escolta()
