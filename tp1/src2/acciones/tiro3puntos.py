from accion import *

class Tiro3Puntos(Accion):
    def __init__(self, unJugador):
        self._jugadorEjecutante = unJugador

    def jugadorEjecutante(self):
        return self._jugadorEjecutante

    def defenderCon(unaJugadaDefensiva, unJugadorDefensivo):
        unaAccionDefensiva = unaJugadaDefensiva.defenderTiro(self, unJugadorDefensivo)
        return unaAccionDefensiva
