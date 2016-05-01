import equipo
import random

class Jugador(object):
	
	def __init__(self, unNombre, unApellido, unFPG, un3PP, unRPG, unAPG, unBPG, unSPG, unTO, unPPG, unPrecio):
		self._nombre = unNombre
		self._apellido = unApellido
		self._fpg = unFPG
		self.__3pp = un3PP
		self._rpg = unRPG
		self._apg = unAPG
		self._bpg = unBPG
		self._spg = unSPG
		self._to = unTO
		self._ppg = unPPG
		self._modificadorDeTiroPorPaseExitoso = 0
		self._modificadorDeTiroPorCansancio = 0
		self._precio = unPrecio


	def igualA(otroJugador):
		"no nos interesan los modificadores de tiro para la comparacion"
		igual = self._nombre == otroJugador.nombre()
		igual = igual and (self._apellido == otroJugador.apellido())
		igual = igual and (self._fpg == otroJugador.fpg())
		igual = igual and (self.__3pp == otroJugador._3pp())
		igual = igual and (self._rpg == otroJugador.rpg())
		igual = igual and (self._apg == otroJugador.apg())
		igual = igual and (self._spg == otroJugador.spg())
		igual = igual and (self._bpg == otroJugador.bpg())
		igual = igual and (self._to == otroJugador.to())
		igual = igual and (self._ppg == otroJugador.ppg())
		return igual

	def nombre(self):
		return self._nombre

	def apellido(self):
		return self._apellido

	def fpg(self):
		return self._fpg

	def _3pp(self):
		return self.__3pp

	def rpg(self):
		return self._rpg

	def apg(self):
		return self._apg

	def spg(self):
		return self._spg

	def to(self):
		return self._to

	def ppg(self):
		return self._ppg

	def precio(self):
		return self._precio
			
	def modificadorDeTipoPorPaseExitoso(self):
		return self._modificadorDeTiroPorPaseExitoso

	def actualizarModificadorDeTiroPorPaseExitoso(self, unNuevoModificador):
		self._modificadorDeTiroPorPaseExitoso = min(0.3, unNuevoModificador)

	def modificadorDeTiroPorCansancio(self):
		return self._modificadorDeTiroPorCansancio

	def actualizarModificadoDeTiroPorCansancio(self, unModificador):
		self._modificadorDeTiroPorCansancio += unModificador

	def ejecutarAccion(self, unaAccion):
		unaAccion.ejecutarAccionCon(self)

	def elegirPase(self, unEquipo):
		eleccion = random.choice(unEquipo.jugadores())
		while (eleccion.igualA(self)):
			eleccion = random.choice(unEquipo.jugadores())
		return eleccion
			