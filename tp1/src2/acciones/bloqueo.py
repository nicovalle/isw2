from accionDefensiva import *

class Bloqueo(AccionDefensiva):
    def __init__(self, unJugador):
        self._jugadorEjecutante = unJugador

    def jugadorEjecutante(self):
        return self._jugadorEjecutante

    def resolvedorPara(self, unSimulador):
        unResolvedorDeBloqueo = unSimulador.resolvedorParaBloqueo()
        return unResolvedorDeBloqueo
