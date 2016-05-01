from datamanager import *
from participante import *
from equipo import *
from jugador import * 
import sys

USERS_DB = "users.txt"
EQUIPOS_DB = "equipos.txt" 
JUGADORES_DB = "jugadores.txt"
TECNICOS_DB = "tecnicos.txt"

class FileDataManager(DataManager):

	def loginUser(self, unNombreDeUsuario, unPassword):
		"userName|pass|mail|cap|fichas|equipo1,equipo2,equipo3|cap|fichas"
		lines = open(USERS_DB).readlines()
		for line in lines:
			data = line.split("|")
			if (data[0] == unNombreDeUsuario and data[1] == unPassword):
				print "ENCONTRE user " + unNombreDeUsuario
				equipos = data[3].split(",")
				userTeams = set()
				for equipo in equipos:
					unEquipo = self.obtenerEquipo(str(equipo), unNombreDeUsuario)
					if (not (unEquipo is None)):
						userTeams.add(unEquipo)
				return Participante(data[0], data[2], userTeams, float(data[4]), float(data[5]))
	
	def registerUser(self, unNombreDeUsuario,  unEmail, unPassword):
		pass
	
	def actualizarParticipante(self, unParticipante):
		pass

	def actualizarTablaDeResultados(self, unaTablaDeResultados):
		pass

	def obtenerTablaDeResultados(self):
		pass	
			
	def actualizarParticipante(self, unParticipante):
		pass

	def actualizarJugador(self, unJugador):
		pass
		
	def obtenerJugador(self, unNombre, unApellido):
		lines = open(JUGADORES_DB).readlines()
		jugador = None
		for line in lines:
			data = line.split("|")
			if (data[0] == unNombre and data[1] == unApellido):
				jugador = Jugador(unNombre, unApellido, float(data[2]), float(data[3]), float(data[4]), float(data[5]), float(data[6]), float(data[7]), float(data[8]), float(data[9]), float(data[10]))
				break
		return jugador
	
	def obtenerTecnico(self, unNombre, unApellido):
		"WIP"
		lines = open(TECNICOS_DB).readlines()
		for line in lines:
			data = line.split("|")
			if (data[0] == unNombre and data[1] == unApellido):
				return unNombre + " " + unApellido
	

	def actualizarTecnico(self, unTecnico):
		pass

	def obtenerEquipo(self, unNombreDeEquipo, unNombreDeDueno):
		"nombre|dueno|jugador1nombre jugador1apellido, ...., jugador5nombre jugador5apellido|estrellanombre estrellapellido|tecniconombre tecnicoapellido"
		lines = open(EQUIPOS_DB).readlines()
		equipo = None
		for line in lines:
			data = line.split("|")
			if (data[0] == unNombreDeEquipo and data[1] == unNombreDeDueno):
				print "ENCONTRE EQUIPO " + unNombreDeEquipo
				jugadores = data[2].split(",")
				teamPlayers = []
				estrella = self.obtenerJugador(str(data[3].split(" ")[0]), str(data[3].split(" ")[1]))
				for jugador in jugadores:
					player = self.obtenerJugador(jugador.split(" ")[0],jugador.split(" ")[1])
					if (not (player is None)):
						teamPlayers.append(player)
				tecnico = self.obtenerTecnico(str(data[4].split(" ")[0]), str(data[4].split(" ")[1]))		
				if (len(teamPlayers) == 5 and (not (estrella is None)) and (not (tecnico is None))):
					equipo = Equipo(unNombreDeEquipo, teamPlayers[0], teamPlayers[1], teamPlayers[2], teamPlayers[3], teamPlayers[4], estrella, tecnico, unNombreDeDueno)		
		return equipo

	def actualizarEquipo(self, unEquipo):
		pass

	def obtenerLogSimulacion(self, unaSimulacion):
		pass

	def guardarLogSimulacion(self, unaSimulacion):
		pass