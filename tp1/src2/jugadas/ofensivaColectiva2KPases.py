# TODO -> PARA HACER. Tener en cuenta ultimo pase.
import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir)

from ofensivaColectiva import *
from posiciones import posicion
from acciones import accion

class OfensivaColectiva2KPases(OfensivaColectiva):
    def __init__(self, cantPases):
        self._k = cantPases
        self._posicionesFinales = [posicion.AlaPivot(), posicion.Pivot()]

#    def proximaAccionOfensiva(self, unContexto):
#        jugadorAtacante = unContexto.jugadorConPosesion()
#        equipoAtacante = unContexto.equipoAtacante()
#        pasoJugadaOfensiva = unContexto.pasoDeJugadaOfensiva()
#        cantidadPases = self._k
#
#        if(pasoJugadaOfensiva == (cantidadPases + 1)):
#            unaAccionOfensiva = accion.Tiro2Puntos(self, jugadorAtacante)
#        else:
#            if(pasoJugadaOfensiva < cantidadPases):
#                unJugadorReceptor = self.elegirJugadorDistintoA(self, jugadorAtacante, equipoAtacante)
#            elif(pasoJugadaOfensiva == cantidadPases):
#                unJugadorReceptor = self.elegirJugadorEntrePosiciones(self._posicionesFinales, equipoAtacante)
#
#            unaAccionOfensiva = accion.Pase(jugadorAtacante, unJugadorReceptor)
#
#        return unaAccionOfensiva
#
#    def elegirJugadorDistintoA(self, unJugador, unEquipo):
#        return unEquipo.jugadorDistintoA(unJugador)
#
#    def elegirJugadorEntrePosiciones(unaListaDePosiciones, unEquipo):
#        return unEquipo.jugadorEnPosiciones(listaDePosiciones)
#
