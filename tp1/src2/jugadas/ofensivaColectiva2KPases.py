from ofensivaColectiva import *

class OfensivaColectiva2KPases(OfensivaColectiva):
    def __init__(self, cantPases):
        self._k = cantPases
        self._posicionesFinales = [posicion.AlaPivot(), posicion.Pivot()]
