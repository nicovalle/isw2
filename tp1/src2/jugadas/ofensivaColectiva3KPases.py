import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir)

from ofensivaColectiva import *
from posiciones import posicion
from acciones import accion

class OfensivaColectiva3KPases(OfensivaColectiva):
    def __init__(self, cantPases):
        self._k = cantPases
        self._posicionesFinales = [posicion.Base(), posicion.Escolta(), posicion.Alero()]
