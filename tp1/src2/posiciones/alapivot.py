from posicion import Posicion

class AlaPivot(Posicion):
    def __init__(self):
        self._nombre = "alapivot"

    def jugadorConPosicion(self, unEquipo):
        return unEquipo.alapivot()
