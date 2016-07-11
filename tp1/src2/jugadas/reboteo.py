import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir)

from posiciones import posicion
from acciones import accion

class Reboteo(object):
    def __init__(self):
        self._ordenPosiciones = [posicion.Pivot(), posicion.AlaPivot(), posicion.Alero(), posicion.Escolta(), posicion.Base()]
        self._nombre = "Reboteo"

    def nombre(self):
        return self._nombre

    def ejecutarParaUnTurno(self, unTurno, unSimulador):
        unContexto = unTurno.contexto()
        equipoAtacante = unContexto.equipoAtacante()
        equipoDefensor = unContexto.equipoDefensor()

        for unaPosicion in self._ordenPosiciones:
            for unEquipo in [equipoDefensor, equipoAtacante]:
                unJugadorRebotante = unEquipo.jugadorEnPosicion(unaPosicion)
                unSimulador.logger().loggearReboteoIntento(unJugadorRebotante, unEquipo)
                unaAccionDeRebote = accion.Rebote(unJugadorRebotante)
                unResolvedorDeRebote = unaAccionDeRebote.resolvedorPara(unSimulador)

                resultadoReboteo = unResolvedorDeRebote.esExitoso(unaAccionDeRebote, unSimulador)

                if(resultadoReboteo):
                    unSimulador.logger().loggearReboteoExito(unJugadorRebotante, unEquipo)
                    unResultado = unTurno.jugarPosesion(equipoDefensor, equipoAtacante, unSimulador)
                    return unResultado

        unSimulador.logger().loggearReboteoFallido()
        unResultado = unSimulador.pelotaAfueraPara(unTurno)
        return unResultado
