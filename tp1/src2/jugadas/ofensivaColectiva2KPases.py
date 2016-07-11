from ofensivaColectiva import *

class OfensivaColectiva2KPases(OfensivaColectiva):
    def __init__(self, cantPases):
        self._k = cantPases
        self._posicionesFinales = [posicion.AlaPivot(), posicion.Pivot()]
        self._nombre = "Colectiva interna de 2 puntos luego de "+str(cantPases)+" pases"

    def nombre(self):
        return self._nombre

    def proximaAccionOfensiva(self, unContexto):
        equipoAtacante = unContexto.equipoAtacante()
        pasoJugadaOfensiva = unContexto.pasoDeJugadaOfensiva()

        if(pasoJugadaOfensiva == 0):
            unContexto.jugadorConPosesion(equipoAtacante.base())

        jugadorAtacante = unContexto.jugadorConPosesion()

        cantidadPases = self._k
        if(pasoJugadaOfensiva == cantidadPases):
            unaAccionOfensiva = accion.Tiro2Puntos(jugadorAtacante)
        else:
            if(pasoJugadaOfensiva < cantidadPases-1):
                unJugadorReceptor = self.elegirJugadorDistintoA(jugadorAtacante, equipoAtacante)
            else:
                unJugadorReceptor = self.elegirJugadorEntrePosicionesDistintoA(self._posicionesFinales, jugadorAtacante, equipoAtacante)

            unaAccionOfensiva = accion.Pase(jugadorAtacante, unJugadorReceptor)

        return unaAccionOfensiva
