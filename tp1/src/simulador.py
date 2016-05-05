import random
from equipo import *
from turno import *

class Simulador(object):
	def __init__(self, unParticipanteDesafiante, unParticipanteDesafiado, unaCantidadDeFichas=0, unaCantidadDeTurnos=40):
		self._cantidadDeTurnos = unaCantidadDeTurnos
		self._participanteDesafiante = unParticipanteDesafiante
		self._participanteDesafiado = unParticipanteDesafiado
		self._fichasApostadas = unaCantidadDeFichas
		self._turnoNumero = 1

		moneda = random.random()
		if(moneda < 0.5):
			self._equipoQueAtaca = self._participanteDesafiante.equipoElegido()
			self._equipoQueDefiende = self._participanteDesafiado.equipoElegido()
		else:
			self._equipoQueAtaca = self._participanteDesafiado.equipoElegido()
			self._equipoQueDefiende = self._participanteDesafiante.equipoElegido()

	def iniciarTurno(self):
		print("Turno numero "+str(self._turnoNumero)+":")
		unTurno = Turno(self, self._equipoQueAtaca, self._equipoQueDefiende)
		unTurno.empezarTurno()

	def terminoTurno(self, unTurno):
		self._equipoQueAtaca, self._equipoQueDefiende = self._equipoQueDefiende, self._equipoQueAtaca
		self._turnoNumero += 1

		# TODO -> que hacemos con el if?
		if (self._turnoNumero > self._cantidadDeTurnos):
			self.terminarSimulacion()


		self.iniciarTurno()
	def terminarSimulacion(self):
		print "Se acabo todo"
		exit()
