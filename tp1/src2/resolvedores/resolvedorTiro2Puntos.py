from resolvedor import *

class ResolvedorTiro2Puntos(Resolvedor):
    def continuarConFallo(self, unTurno, unSimulador):
        ''' Tiro de 2 puntos fallido, se produce un reboteo'''
        unReboteo = Reboteo()
        unResultado = unReboteo.ejecutarParaUnTurno(unTurno, unSimulador)

        return unResultado

    def continuarConExito(self, unTiro, unTurno, unSimulador):
        ''' Tiro de 2 puntos exitoso, termina el turno.'''
        unResultado = unSimulador.encestarDoble(unTurno)

        return unResultado

    def esExitoso(self, unTiro, unSimulador):
        numeroAleatorio = random.random()
        jugadorEjecutante = unTiro.jugadorEjecutante()
        estadisticasDeUnJugadorEjecutante = unSimulador.estadisticasDe(jugadorEjecutante)

        umbralDeExito = estadisticasDeUnJugadorEjecutante.fgp() + estadisticasDeUnJugadorEjecutante.ppg() * 0.01 # + TODO MODIFICADORES

        return numeroAleatorio <= umbralDeExito
