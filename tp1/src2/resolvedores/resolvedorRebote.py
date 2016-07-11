from resolvedor import *

class ResolvedorRebote(Resolvedor):
    def esExitoso(self, unRebote, unSimulador):
        numeroAleatorio = random.random()
        jugadorEjecutante = unRebote.jugadorEjecutante()
        estadisticasDeUnJugadorEjecutante = unSimulador.estadisticasDe(jugadorEjecutante)

        umbralDeExito = estadisticasDeUnJugadorEjecutante.rpg() * 0.05 # + TODO MODIFICADORES

        return numeroAleatorio <= umbralDeExito
