from ofensiva import *

from abc import ABCMeta, abstractmethod

class OfensivaColectiva(Ofensiva):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        pass

    def proximaAccionOfensiva(self, unContexto):
        jugadorAtacante = unContexto.jugadorConPosesion()
        equipoAtacante = unContexto.equipoAtacante()
        pasoJugadaOfensiva = unContexto.pasoDeJugadaOfensiva()
        cantidadPases = self._k

        if(pasoJugadaOfensiva == (cantidadPases + 1)):
            unaAccionOfensiva = accion.Tiro2Puntos(self, jugadorAtacante)
        else:
            if(pasoJugadaOfensiva < cantidadPases):
                unJugadorReceptor = self.elegirJugadorDistintoA(self, jugadorAtacante, equipoAtacante)
            elif(pasoJugadaOfensiva == cantidadPases):
                unJugadorReceptor = self.elegirJugadorEntrePosiciones(self._posicionesFinales, equipoAtacante)

            unaAccionOfensiva = accion.Pase(jugadorAtacante, unJugadorReceptor)

        return unaAccionOfensiva
