from accion import *

class Tiro(Accion):
	__metaclass__ = ABCMeta
	def defenderCon(self, unaJugadaDefensiva):
		return unaJugadaDefensiva.defenderTiro()

	@abstractmethod
	def umbralDeExito(self, jugador):
		pass

class TiroDosPuntos(Tiro):
	def umbralDeExito(self, unJugador):
		return (unJugador.fgp() + unJugador.ppg() * 0.01)

class TiroTresPuntos(Tiro):
	def umbralDeExito(self, unJugador):
		return (unJugador._3pp() + (unJugador.ppg() / 2) * 0.01)

class Bloqueo(Accion):
    def umbralDeExito(self, unJugador):
        return (unJugador.bpg() * 0.2)

class Pase(Accion):
	def umbralDeExito(self, unJugador):
		return (1 - unJugador.to() * 0.1)

	def defenderCon(self, unaJugadaDefensiva):
		return unaJugadaDefensiva.defenderPase()

class Robar(Accion):
    def umbralDeExito(self, unJugador):
        return (unJugador.spg() * 0.2)

class Rebotar(Accion):
    def umbralDeExito(self, unJugador):
        return (unJugador.rpg() * 0.05)
