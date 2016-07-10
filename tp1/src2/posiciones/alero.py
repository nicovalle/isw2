from posicion import Posicion

class Alero(Posicion):
    def __init__(self):
        self._nombre = "alero"

    def jugadorConPosicion(self, unEquipo):
        return unEquipo.alero()
