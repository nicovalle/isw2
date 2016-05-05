import equipo
import random
#import turno

class Simulador(object):
	def __init__(self, unParticipanteDesafiante, otroParticipanteDesafiado, unaCantidadDeFichas=0, unaCantidadDeTurnos=40):
		self._cantidadDeTurnos = unaCantidadDeTurnos
		self._participanteDesafiante = unParticipanteDesafiante
		self._participanteDesafiado = otroParticipanteDesafiado
		self._fichasApostadas = unaCantidadDeFichas

	def iniciarSimulacion(self):
		self._turnosRestantes = self._cantidadDeTurnos

		moneda = random.Random()
		if(moneda < 0.5):
			self._equipoAtacante = self._participanteDesafiante.equipo()
			self._equipoDefensor = self._participanteDesafiado.equipo()
		else:
			self._equipoAtacante = self._participanteDesafiado.equipo()
			self._equipoDefensor = self._participanteDesafiante.equipo()

		while (self._turnosRestantes > 0):
#			self._turnoActual =  Turno(self, self._equipoAtacante, self._equipoDefensor)
			tmp = self._equipoAtacante
			self._equipoAtacante = self._equipoDefensor
			self._equipoDefensor = tmp
			self._turnosRestantes -= 1
