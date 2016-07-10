from accionOfensiva import *

class Tiro3Puntos(AccionOfensiva):
    def __init__(self, unJugador):
        self._jugadorEjecutante = unJugador

    def jugadorEjecutante(self):
        return self._jugadorEjecutante

    def resolvedorPara(unSimulador):
        unResolvedorDeTiro3Puntos = unSimulador.resolvedorParaTiro3Puntos(self)
        return unResolvedorDeTiro3Puntos

    def defenderCon(unaJugadaDefensiva, unJugadorDefensivo):
        unaAccionDefensiva = unaJugadaDefensiva.defenderTiro(self, unJugadorDefensivo)
        return unaAccionDefensiva
