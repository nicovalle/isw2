class ResolvedorTiro2Puntos(object):
    #def __init__(self):

    def continuarConFallo(self, unTurno, unSimulador):
        ''' Tiro de 2 puntos fallido, se produce un reboteo'''
        unReboteo = Reboteo()
        unResultado = unReboteo.ejecutarParaUnTurno(unTurno, unSimulador)

        return unResultado

    def continuarConExito(self, unTiro, unTurno, unSimulador):
        ''' Tiro de 2 puntos exitoso, termina el turno.'''
        unResultado = unSimulador.encestarDoble(unTurno)

        return unResultado
