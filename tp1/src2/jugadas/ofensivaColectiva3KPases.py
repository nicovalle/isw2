from ofensivaColectiva import *

class OfensivaColectiva3KPases(OfensivaColectiva):
    def __init__(self, cantPases):
        self._k = cantPases
        self._posicionesFinales = [posicion.Base(), posicion.Escolta(), posicion.Alero()]

    def proximaAccionOfensiva(self, unContexto):
        jugadorAtacante = unContexto.jugadorConPosesion()
        equipoAtacante = unContexto.equipoAtacante()
        pasoJugadaOfensiva = unContexto.pasoDeJugadaOfensiva()
        cantidadPases = self._k

        if(pasoJugadaOfensiva == (cantidadPases + 1)):
            unaAccionOfensiva = accion.Tiro3Puntos(self, jugadorAtacante)
        else:
            if(pasoJugadaOfensiva < cantidadPases):
                unJugadorReceptor = self.elegirJugadorDistintoA(self, jugadorAtacante, equipoAtacante)
            elif(pasoJugadaOfensiva == cantidadPases):
                unJugadorReceptor = self.elegirJugadorEntrePosiciones(self._posicionesFinales, equipoAtacante)

            unaAccionOfensiva = accion.Pase(jugadorAtacante, unJugadorReceptor)

        return unaAccionOfensiva
