from accionOfensiva import *

class Tiro2Puntos(AccionOfensiva):
    def __init__(self, unJugador):
        self._jugadorEjecutante = unJugador

    def jugadorEjecutante(self):
        return self._jugadorEjecutante

    def resolvedorPara(self, unSimulador):
        unResolvedorDeTiro2Puntos = unSimulador.resolvedorParaTiro2Puntos()
        return unResolvedorDeTiro2Puntos

    def defenderCon(self, unaJugadaDefensiva, unJugadorDefensivo):
        unaAccionDefensiva = unaJugadaDefensiva.defenderTiro(self, unJugadorDefensivo)
        return unaAccionDefensiva
