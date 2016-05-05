import random
from equipo import *
from turno import *

class Simulador(object):
	def __init__(self, unParticipanteDesafiante, unParticipanteDesafiado, unaCantidadDeFichas=0, unaCantidadDeTurnos=40):
		self._cantidadDeTurnos = unaCantidadDeTurnos
		self._participanteDesafiante = unParticipanteDesafiante
		self._participanteDesafiado = unParticipanteDesafiado
		self._fichasApostadas = unaCantidadDeFichas

	def iniciarSimulacion(self):
		turnoNumero = 1

		moneda = random.random()
		if(moneda < 0.5):
			equipoQueAtaca = self._participanteDesafiante.equipoElegido()
			equipoQueDefiende = self._participanteDesafiado.equipoElegido()
		else:
			equipoQueAtaca = self._participanteDesafiado.equipoElegido()
			equipoQueDefiende = self._participanteDesafiante.equipoElegido()

		while (turnoNumero <= self._cantidadDeTurnos):
			print("Turno "+str(turnoNumero)+": ataca "+equipoQueAtaca.nombre()+" y defiende "+equipoQueDefiende.nombre())
			turno =  Turno(self, equipoQueAtaca, equipoQueDefiende)
			turno.empezarTurno()

			equipoQueAtaca, equipoQueDefiende = equipoQueDefiende, equipoQueAtaca
			turnoNumero += 1
