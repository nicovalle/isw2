import equipo

class Posicion(object):

	def __init__(self, posicion):
		self._posicion = posicion

	def nombre(self):
		return self._posicion

	def jugadorConPosicion(self, unEquipo):
		return getattr(unEquipo, self._posicion.lower().replace(" ",""))()
		#return metodoPosicion()
