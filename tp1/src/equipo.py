import jugador

class Equipo(object):

	def __init__(self, unNombre, unBase, unEscolta, unAlero, unAlaPivot, unPivot, unJugadorEstrella, unTecnico, unDueno):
		"en nuestro modelos los equipos son inmutables"
		self._nombre = unNombre
		self._base = unBase
		self._escolta = unEscolta
		self._alero = unAlero
		self._alaPivot = unAlaPivot
		self._pivot = unPivot
		self._estrella = unJugadorEstrella
		self._tecnico = unTecnico
		self._dueno = unDueno

	"accessing messages"

	def nombre(self):
		return self._nombre

	def jugadores(self):
		return [self._base, self._escolta, self._alero, self._alaPivot, self._pivot]

	def base(self):
		return self._base

	def escolta(self):
		return self._escolta

	def alero(self):
		return self._alero

	def alaPivot(self):
		return self._alaPivot

	def pivot(self):
		return self._pivot

	def estrella(self):
		return self._estrella

	def tecnico(self):
		return self._tecnico

	def dueno(self):
		return self._dueno

	def presupuesto(self):
		return reduce(lambda x, y : x + y, (map(lambda jugador: jugador.precio(), self.jugadores())))

	def ejecutarJugada(self, unaJugada):
		unaJugada.ejecutarCon(self)

	def elegirJugadaOfensiva(self):
		creadorJugada = self._tecnico.seleccionarJugadaOfensiva()
		return creadorJugada(self, 3)

	def elegirJugadaDefensiva(self):
		creadorJugada = self._tecnico.seleccionarJugadaDefensiva()
		return creadorJugada(self)
