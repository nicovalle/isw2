class Equipo(object):
	
	def __init__(self, unBase, unEscolta, unAlero, unAlaPivot, unPivot, unJugadorEstrella, unTecnico, unDueno):
		"en nuestro modelos los equipos son inmutables"
		self.base = unBase
		self.escolta = unEscolta
		self.alero = unAlero
		self.alaPivot = unAlaPivot
		self.pivot = unPivot
		self.estrella = un unJugadorEstrella
		self.tecnico = unTecnico
		self.dueno = unDueno

	"accessing messages"
	def jugadores:
		return [self.base, self.escolta, self.alero, self.alaPivot, self.pivot]

	def base:
		return self.base
		
	def escolta:
		return self.escolta

	def alero:
		return self.alero

	def alaPivot:
		return self.alaPivot

	def pivot
		return self.pivot

	def estrella:
		return estrella

	def tecnico:
		return self.tecnico

	def dueno:
		return dueno

	def presupuesto:
		return reduce(lambda x, y : x + y, (map(lambda jugador: jugador.valor, self.jugadores))