from accionOfensiva import *

class Tiro3Puntos(AccionOfensiva):
    def __init__(self, unJugador):
        self._jugadorEjecutante = unJugador

    def jugadorEjecutante(self):
        return self._jugadorEjecutante

    def resolvedorPara(self, unSimulador):
        unResolvedorDeTiro3Puntos = unSimulador.resolvedorParaTiro3Puntos()
        return unResolvedorDeTiro3Puntos

    def defenderCon(self, unaJugadaDefensiva, unJugadorDefensivo):
        unaAccionDefensiva = unaJugadaDefensiva.defenderTiro(self, unJugadorDefensivo)
        return unaAccionDefensiva
