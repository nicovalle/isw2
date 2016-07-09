class ResolvedorTiro3Puntos(object):
    #def __init__(self):

    def continuarConFallo(self, unTurno, unSimulador):
        ''' Tiro de 3 puntos fallido, se produce un reboteo'''
        unReboteo = Reboteo()
        unResultado = unReboteo.ejecutarParaUnTurno(unTurno, unSimulador)

        return unResultado

    def continuarConExito(self, unTiro, unTurno, unSimulador):
        ''' Tiro de 3 puntos exitoso, termina el turno.'''
        unResultado = unSimulador.encestarTriple(unTurno)

        return unResultado
