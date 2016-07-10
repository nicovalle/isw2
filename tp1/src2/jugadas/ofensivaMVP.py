from ofensiva import *

class OfensivaMVP(Ofensiva):
    def proximaAccionOfensiva(self, unContexto):
        jugadorAtacante = unContexto.jugadorConPosesion()
        equipoAtacante = unContexto.equipoAtacante()
        jugadorEstrella = equipoAtacante.jugadorEstrella()
        pasoJugadaOfensiva = unContexto.pasoDeJugadaOfensiva()

        if(pasoJugadaOfensiva == 0 and jugadorAtacante != jugadorEstrella):
            unaAccionOfensiva = accion.Pase(jugadorAtacante, jugadorEstrella)
        else:
            unaAccionOfensiva = random.choice([accion.Tiro2Puntos(jugadorEstrella), accion.Tiro3Puntos(jugadorEstrella)])

        return unaAccionOfensiva
