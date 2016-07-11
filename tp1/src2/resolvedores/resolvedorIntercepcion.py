from resolvedor import *

class ResolvedorIntercepcion(Resolvedor):
    def continuarConExito(self, unaIntercepcion, unTurno, unSimulador):
        ''' Intercepcion exitosa, cambian los roles de los equipos.'''
        unSimulador.logger().loggearIntercepcionExitosa(unaIntercepcion.jugadorEjecutante())

        unContexto = unTurno.contexto()

        equipoAtacante = unContexto.equipoAtacante()
        equipoDefensor = unContexto.equipoDefensor()

        unResultado = unTurno.jugarPosesion(equipoDefensor, equipoAtacante, unSimulador)
        return unResultado

    def esExitoso(self, unaIntercepcion, unSimulador):
        unSimulador.logger().loggearIntercepcionIntento(unaIntercepcion.jugadorEjecutante())

        numeroAleatorio = random.random()
        jugadorEjecutante = unaIntercepcion.jugadorEjecutante()
        estadisticasDeUnJugadorEjecutante = unSimulador.estadisticasDe(jugadorEjecutante)

        umbralDeExito = estadisticasDeUnJugadorEjecutante.spg() * 0.2 # + TODO MODIFICADORES

        return numeroAleatorio <= umbralDeExito
