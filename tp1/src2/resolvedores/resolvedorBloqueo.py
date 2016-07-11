from resolvedor import *

class ResolvedorBloqueo(Resolvedor):
    def continuarConExito(self, unBloqueo, unTurno, unSimulador):
        ''' Bloqueo exitoso, se rebotea.'''
        unSimulador.logger().loggearBloqueoExitoso(unBloqueo.jugadorEjecutante())
        unSimulador.logger().loggearReboteoInicio()

        unReboteo = reboteo.Reboteo()
        unResultado = unReboteo.ejecutarParaUnTurno(unTurno, unSimulador)

        return unResultado

    def esExitoso(self, unBloqueo, unSimulador):

        numeroAleatorio = random.random()
        jugadorEjecutante = unBloqueo.jugadorEjecutante()
        estadisticasDeUnJugadorEjecutante = unSimulador.estadisticasDe(jugadorEjecutante)

        umbralDeExito = estadisticasDeUnJugadorEjecutante.bpg() * 0.2 # + TODO MODIFICADORES

        return numeroAleatorio <= umbralDeExito
