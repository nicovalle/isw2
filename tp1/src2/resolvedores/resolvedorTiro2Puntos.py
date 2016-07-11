from resolvedor import *

class ResolvedorTiro2Puntos(Resolvedor):
    def continuarConFallo(self, unTurno, unSimulador):
        ''' Tiro de 2 puntos fallido, se produce un reboteo'''
        unSimulador.logger().loggearTiroFallido()
        unSimulador.logger().loggearReboteoInicio()

        unReboteo = reboteo.Reboteo()
        unResultado = unReboteo.ejecutarParaUnTurno(unTurno, unSimulador)

        return unResultado

    def continuarConExito(self, unTiro, unTurno, unSimulador):
        ''' Tiro de 2 puntos exitoso, termina el turno.'''
        unSimulador.logger().loggearEncestarDoble(unTurno.contexto().equipoAtacante())
        unResultado = unSimulador.encestarDoble(unTurno)

        return unResultado

    def esExitoso(self, unTiro, unSimulador):
        unSimulador.logger().loggearDobleIntento(unTiro.jugadorEjecutante())

        numeroAleatorio = random.random()
        jugadorEjecutante = unTiro.jugadorEjecutante()
        estadisticasDeUnJugadorEjecutante = unSimulador.estadisticasDe(jugadorEjecutante)

        umbralDeExito = estadisticasDeUnJugadorEjecutante.fgp() + estadisticasDeUnJugadorEjecutante.ppg() * 0.01 # + TODO MODIFICADORES

        return numeroAleatorio <= umbralDeExito
