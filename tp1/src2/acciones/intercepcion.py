from AccionDefensiva import *

class Intercepcion(AccionDefensiva):
    def __init__(self, unJugador):
        self._jugadorEjecutante = unJugador

    def jugadorEjecutante(self):
        return self._jugadorEjecutante

    def resolvedorPara(self, unSimulador):
        unResolvedorDeIntercepcion = unSimulador.resolvedorParaIntercepcion(self)
        return unResolvedorDeIntercepcion
