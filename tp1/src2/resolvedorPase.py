class ResolvedorPase(object):
    #def __init__(self):

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
