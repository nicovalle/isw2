import jugadas
import acciones
import random

class Turno(object):
	def __init__(self, unaSimulacion, unEquipoQueAtaca, unEquipoQueDefiende):
		self._equipoAtacante = unEquipoQueAtaca
		self._equipoDefensor = unEquipoQueDefiende
		self._simulacion = unaSimulacion

	def empezarTurno(self):
		self._jugadorConPelota = self._equipoAtacante.base()
		self._jugadaOfensiva = self._equipoAtacante.elegirJugadaOfensiva()
		self._jugadaDefensiva = self._equipoDefensor.elegirJugadaDefensiva()
		print("  "+self._equipoAtacante.nombre()+" atacan con "+self._jugadaOfensiva.nombre()+" y "+self._equipoDefensor.nombre()+" defienden con "+self._jugadaDefensiva.nombre())

		self.avanzarJugada()

	def avanzarJugada(self):
		self._accionOfensiva = self._jugadaOfensiva.proximaAccion()
		self._accionDefensiva = self._jugadaDefensiva.accionParaDefender(self._accionOfensiva)
		print("La accion ofensiva es "+str(self._accionOfensiva.__class__)+" y la defensiva "+str(self._accionDefensiva.__class__))
		self.resolver(self._accionOfensiva, self._accionDefensiva)

	def resolver(self, unaAccionOfensiva, unaAccionDefensiva):
		moneda = random.random()
		# TODO -> ESTO ESTA MAL, ES HOMBRE A HOMBRE
		unJugadorDefensivo = self._equipoDefensor.base()
		# TODO -> que hacemos con el if?
		if (moneda < unaAccionDefensiva.umbralDeExito(unJugadorDefensivo)):
			print(unJugadorDefensivo.nombreCompleto()+" robo la pelota a "+self._jugadorConPelota.nombreCompleto())
			self.cambioDeRoles(unJugadorDefensivo)

		moneda = random.random()
		if (moneda < unaAccionOfensiva.umbralDeExito(self._jugadorConPelota)):
			print(self._jugadorConPelota.nombreCompleto()+" logro hacer "+str(unaAccionOfensiva.__class__))
			self.avanzarJugada()

		self._simulacion.terminoTurno(self)

	def cambioDeRoles(self, unJugador):
		self._equipoAtacante, self._equipoDefensor = self._equipoDefensor, self._equipoAtacante
		self.empezarTurno()
