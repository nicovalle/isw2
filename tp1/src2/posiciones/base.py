from posicion import Posicion

class Base(Posicion):
    def __init__(self):
        self._nombre = "base"

    def jugadorConPosicion(self, unEquipo):
        return unEquipo.base()
