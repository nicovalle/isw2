import jugadas
import acciones

class Turno(object):
	def __init__(self, unaSimulacion, unEquipoQueAtaca, unEquipoQueDefiende):
		self._equipoAtacante = unEquipoQueAtaca
		self._equipoDefensor = unEquipoQueDefiende

	def empezarTurno(self):
		jugadaOfensiva = self._equipoAtacante.elegirJugadaOfensiva()
		jugadaDefensiva = self._equipoDefensor.elegirJugadaDefensiva()
