from resolvedor import *

class ResolvedorIntercepcion(Resolvedor):
    def continuarConExito(self, unaIntercepcion, unTurno, unSimulador):
        ''' Intercepcion exitosa, cambian los roles de los equipos.'''
        unContexto = unTurno.contexto()

        equipoAtacante = unContexto.equipoAtacante()
        equipoDefensor = unContexto.equipoDefensor()

        unResultado = unTurno.jugarPosesion(equipoDefensor, equipoAtacante, unSimulador)
        return unResultado

    def esExitoso(self, unaIntercepcion, unSimulador):
        numeroAleatorio = random.random()
        jugadorEjecutante = unaIntercepcion.jugadorEjecutante()
        estadisticasDeUnJugadorEjecutante = unSimulador.estadisticasDe(jugadorEjecutante)

        umbralDeExito = estadisticasDeUnJugadorEjecutante.spg() * 0.2 # + TODO MODIFICADORES

        return numeroAleatorio <= umbralDeExito
