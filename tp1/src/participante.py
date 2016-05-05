class Participante(object):

	def __init__(self, unNombre, unEmail, unConjuntoDeEquipos, unCap, unaCantidadDeFichas):
		self._nombre = unNombre
		self._equipos = unConjuntoDeEquipos
		self._cap = unCap
		self._fichas = unaCantidadDeFichas
		self._email = unEmail

	def nombre(self):
		return self._nombre

	def email(self):
		return self._email

	def equipos(self):
		return self._equipos

	def agregarEquipo(self, unEquipo):
		if (unEquipo.presupuesto() <= self._cap):
			self._equipos.add(unEquipo)

	def removerEquipo(self, unEquipo):
		self._equipos.discard(unEquipo)

	def seleccionarEquipo(self, nombre):
		for equipo in self._equipos:
			if (equipo.nombre() == nombre):
				self._equipoActual = equipo

	def equipoElegido(self):
		return self._equipoActual

	def cap(self):
		return self._cap

	def updateCap(unPorcentaje = 0.01):
		self._cap += (self._cap * unPorcentaje)

	def fichas(self):
		return self._fichas

	def updateFichas(self, unaAdicionDeFichas):
		self._fichas += unaAdicionDeFichas
