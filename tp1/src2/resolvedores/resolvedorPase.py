from resolvedor import *

class ResolvedorPase(Resolvedor):
    def continuarConFallo(self, unTurno, unSimulador):
        ''' Pase fallido, intercepcion fallida, la pelota sale de la cancha y termina el turno'''
        unResultado = unSimulador.pelotaAfueraPara(unTurno)
        return unResultado

    def continuarConExito(self, unPase, unTurno, unSimulador):
        ''' Pase exitoso, se cambia que jugador tiene posesion de la pelota, se aumenta un paso de la jugada ofensiva, y se sigue jugando.'''
        unReceptor = unPase.jugadorReceptor()

        unContexto = unTurno.contexto()
        unContexto.jugadorConPosesion(unReceptor)
        unContexto.incrementarPasoJugadaOfensiva()

        unResultado = unSimulador.elegirYEjecutarAcciones(unTurno)
        return unResultado

    def esExitoso(self, unPase, unSimulador):
        numeroAleatorio = random.random()
        jugadorEjecutante = unPase.jugadorEjecutante()
        estadisticasDeUnJugadorEjecutante = unSimulador.estadisticasDe(jugadorEjecutante)

        umbralDeExito = 1 - estadisticasDeUnJugadorEjecutante.to() * 0.1

        return numeroAleatorio <= umbralDeExito
