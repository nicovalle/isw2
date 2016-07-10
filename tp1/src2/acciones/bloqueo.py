from accion import *

class Bloqueo(Accion):
    def __init__(self, unJugador):
        self._jugadorEjecutante = unJugador

    def jugadorEjecutante(self):
        return self._jugadorEjecutante
    # TODO -> Jugador Receptor? O sea, el receptor de la accion, el que es bloqueado
