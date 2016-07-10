from ofensivaColectiva import *

class OfensivaColectiva3KPases(OfensivaColectiva):
    def __init__(self, cantPases):
        self._k = cantPases
        self._posicionesFinales = [posicion.Base(), posicion.Escolta(), posicion.Alero()]
