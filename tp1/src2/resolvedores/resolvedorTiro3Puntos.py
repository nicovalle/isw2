from resolvedor import *

class ResolvedorTiro3Puntos(Resolvedor):
    def continuarConFallo(self, unTurno, unSimulador):
        ''' Tiro de 3 puntos fallido, se produce un reboteo'''
        unSimulador.logger().loggearTiroFallido()
        unSimulador.logger().loggearReboteoInicio()

        unReboteo = reboteo.Reboteo()
        unResultado = unReboteo.ejecutarParaUnTurno(unTurno, unSimulador)

        return unResultado

    def continuarConExito(self, unTiro, unTurno, unSimulador):
        ''' Tiro de 3 puntos exitoso, termina el turno.'''
        unSimulador.logger().loggearEncestarTriple(unTurno.contexto().equipoAtacante())
        unResultado = unSimulador.encestarTriple(unTurno)

        return unResultado

    def esExitoso(self, unTiro, unSimulador):
        unSimulador.logger().loggearTripleIntento(unTiro.jugadorEjecutante())

        numeroAleatorio = random.random()
        jugadorEjecutante = unTiro.jugadorEjecutante()
        estadisticasDeUnJugadorEjecutante = unSimulador.estadisticasDe(jugadorEjecutante)

        umbralDeExito = estadisticasDeUnJugadorEjecutante._3pp() + (estadisticasDeUnJugadorEjecutante.ppg()/2) * 0.01 # + TODO MODIFICADORES

        return numeroAleatorio <= umbralDeExito
