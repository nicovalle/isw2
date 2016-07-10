from posicion import Posicion

class Escolta(Posicion):
    def __init__(self):
        self._nombre = "esoclta"

    def jugadorConPosicion(self, unEquipo):
        return unEquipo.base()
