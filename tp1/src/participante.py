class Participante(object):
	
	def __init__(self, unNombre, unEmail, unConjuntoDeEquipos, unCap, unaCantidadDeFichas):
		self.nombre = unNombre
		self.equipos = unConjuntoDeEquipos
		self.cap = unCap
		self.fichas = unaCantidadDeFichas
		self.email = unEmail

	def equipos(self):
		return self.equipos

	def agregarEquipo(self, unEquipo):
		if (unEquipo.presupuesto() <= self.cap):
			equipos.add(unEquipo)

	def removerEquipo(self, unEquipo):
		equipos.discard(unEquipo)

	def cap(self):
		return self.cap

	def updateCap(unPorcentaje = 0.01):
		self.cap += (self.cap * unPorcentaje)

	def fichas(self):
		return self.fichas

	def updateFichas(self, unaAdicionDeFichas):
		self.fichas += unaAdicionDeFichas

	def ejecutarJugada(self, unaJugada):
		return unaJugada.ejecutar(self)