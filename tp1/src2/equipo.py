import random
from posicion import Posicion

class Equipo(object):
    def __init__(self, unNombre, losJugadores, elMVP, unTecnico):
        self._nombre = unNombre
        self._tecnico = unTecnico
        self._mvp = elMVP
        self._jugadores = [(losJugadores[0], Posicion("Base")),
							(losJugadores[1], Posicion("Escolta")),
							(losJugadores[2], Posicion("Alero")),
							(losJugadores[3], Posicion("Ala Pivot")),
							(losJugadores[4], Posicion("Pivot"))]

	def nombre(self):
		return self._nombre

    def tecnico(self):
        return self._tecnico

    def jugadores(self):
        return self._jugadores

    def mvp(self):
        return self._mvp

    def posicionDe(self, unJugador):
        for jugpos in self._jugadores:
            if(jugpos[0] == unJugador):
                return jugpos[1]

    def jugadorEnPosicion(self, unaPosicion):
        return unaPosicion.jugadorConPosicion(self)

    def base(self):
        return self._jugadores[0][0]

    def escolta(self):
        return self._jugadores[1][0]

    def alero(self):
        return self._jugadores[2][0]

    def alapivot(self):
        return self._jugadores[3][0]
    
    def pivot(self):
        return self._jugadores[4][0]