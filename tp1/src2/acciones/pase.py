from accionOfensiva import *

class Pase(AccionOfensiva):
    def __init__(self, unJugador, unReceptor):
        self._jugadorEjecutante = unJugador
        self._jugadorReceptor = unReceptor

    def jugadorEjecutante(self):
        return self._jugadorEjecutante

    def jugadorReceptor(self):
        return self._jugadorReceptor

    def resolvedorPara(self, unSimulador):
        unResolvedorDePase = unSimulador.resolvedorParaPase()
        return unResolvedorDePase

    def defenderCon(self, unaJugadaDefensiva, unJugadorDefensivo):
        unaAccionDefensiva = unaJugadaDefensiva.defenderPase(self, unJugadorDefensivo)
        return unaAccionDefensiva
