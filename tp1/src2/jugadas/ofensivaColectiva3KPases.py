from ofensivaColectiva import *

class OfensivaColectiva3KPases(OfensivaColectiva):
    def __init__(self, cantPases):
        self._k = cantPases
        self._posicionesFinales = [posicion.Base(), posicion.Escolta(), posicion.Alero()]
        self._nombre = "Colectiva externa de 3 puntos luego de "+str(cantPases)+" pases"

    def nombre(self):
        return self._nombre

    def proximaAccionOfensiva(self, unContexto):
        equipoAtacante = unContexto.equipoAtacante()
        pasoJugadaOfensiva = unContexto.pasoDeJugadaOfensiva()

        if(pasoJugadaOfensiva == 0):
            unContexto.jugadorConPosesion(equipoAtacante.base())

        jugadorAtacante = unContexto.jugadorConPosesion()

        cantidadPases = self._k
        if(pasoJugadaOfensiva == (cantidadPases + 1)):
            unaAccionOfensiva = accion.Tiro3Puntos(jugadorAtacante)
        else:
            if(pasoJugadaOfensiva < cantidadPases):
                unJugadorReceptor = self.elegirJugadorDistintoA(jugadorAtacante, equipoAtacante)
            elif(pasoJugadaOfensiva == cantidadPases):
                unJugadorReceptor = self.elegirJugadorEntrePosiciones(self._posicionesFinales, equipoAtacante)

            unaAccionOfensiva = accion.Pase(jugadorAtacante, unJugadorReceptor)

        return unaAccionOfensiva
