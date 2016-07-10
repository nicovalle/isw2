from accionOfensiva import *

class Tiro2Puntos(AccionOfensiva):
    def __init__(self, unJugador):
        self._jugadorEjecutante = unJugador

    def jugadorEjecutante(self):
        return self._jugadorEjecutante

    def resolvedorPara(unSimulador):
        unResolvedorDeTiro2Puntos = unSimulador.resolvedorParaTiro2Puntos(self)
        return unResolvedorDeTiro2Puntos

    def defenderCon(unaJugadaDefensiva, unJugadorDefensivo):
        unaAccionDefensiva = unaJugadaDefensiva.defenderTiro(self, unJugadorDefensivo)
        return unaAccionDefensiva
