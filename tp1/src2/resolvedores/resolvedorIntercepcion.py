from resolvedor import *

class ResolvedorIntercepcion(Resolvedor):
    #def __init__(self):

    def continuarConExito(self, unaIntercepcion, unTurno, unSimulador):
        ''' Intercepcion exitosa, cambian los roles de los equipos.'''
        unContexto = unTurno.contexto()

        equipoAtacante = unContexto.equipoAtacante()
        equipoDefensor = unContexto.equipoDefensor()

        unResultado = unTurno.jugarPosesion(equipoDefensor, equipoAtacante, unSimulador)
        return unResultado
