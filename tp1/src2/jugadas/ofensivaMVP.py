from ofensiva import *

class OfensivaMVP(Ofensiva):
    def __init__(self):
        self._nombre = "MVP"

    def nombre(self):
        return self._nombre

    def proximaAccionOfensiva(self, unContexto):
        equipoAtacante = unContexto.equipoAtacante()
        pasoJugadaOfensiva = unContexto.pasoDeJugadaOfensiva()

        if(pasoJugadaOfensiva == 0):
            unContexto.jugadorConPosesion(equipoAtacante.base())

        jugadorAtacante = unContexto.jugadorConPosesion()
        jugadorEstrella = equipoAtacante.jugadorEstrella()

        if(pasoJugadaOfensiva == 0 and jugadorAtacante != jugadorEstrella):
            unaAccionOfensiva = accion.Pase(jugadorAtacante, jugadorEstrella)
        else:
            unaAccionOfensiva = random.choice([accion.Tiro2Puntos(jugadorEstrella), accion.Tiro3Puntos(jugadorEstrella)])

        return unaAccionOfensiva
