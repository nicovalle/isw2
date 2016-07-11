from accion import *

class Rebote(Accion):
    def __init__(self, unJugador):
        self._jugadorEjecutante = unJugador

    def jugadorEjecutante(self):
        return self._jugadorEjecutante

    def resolvedorPara(self, unSimulador):
        unResolvedorDeRebote = unSimulador.resolvedorParaRebote()
        return unResolvedorDeRebote
