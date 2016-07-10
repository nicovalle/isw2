from posicion import Posicion

class Pivot(Posicion):
    def __init__(self):
        self._nombre = "pivot"

    def jugadorConPosicion(self, unEquipo):
        return unEquipo.pivot()
