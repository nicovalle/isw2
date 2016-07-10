from accion import *

class Pase(Accion):
    def __init__(self, unJugador, unReceptor):
        self._jugadorEjecutante = unJugador
        self._jugadorReceptor = unReceptor

    def jugadorEjecutante(self):
        return self._jugadorEjecutante

    def jugadorReceptor(self):
        return self._jugadorReceptor

    def defenderCon(unaJugadaDefensiva, unJugadorDefensivo):
        unaAccionDefensiva = unaJugadaDefensiva.defenderPase(self, unJugadorDefensivo)
        return unaAccionDefensiva
