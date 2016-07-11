from resolvedor import *

class ResolvedorBloqueo(Resolvedor):
    def continuarConExito(self, unBloqueo, unTurno, unSimulador):
        ''' Bloqueo exitoso, se rebotea.'''
#        unContexto = unTurno.contexto()
#
#        equipoAtacante = unContexto.equipoAtacante()
#        equipoDefensor = unContexto.equipoDefensor()
#
#        unResultado = unTurno.jugarPosesion(equipoDefensor, equipoAtacante, unSimulador)
#        return unResultado

    def esExitoso(self, unBloqueo, unSimulador):
        numeroAleatorio = random.random()
        jugadorEjecutante = unBloqueo.jugadorEjecutante()
        estadisticasDeUnJugadorEjecutante = unSimulador.estadisticasDe(jugadorEjecutante)

        umbralDeExito = estadisticasDeUnJugadorEjecutante.bpg() * 0.2 # + TODO MODIFICADORES

        return numeroAleatorio <= umbralDeExito
