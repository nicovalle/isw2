from defensiva import *

class DefensivaHombreAHombre(Defensiva):
    def accionParaDefender(self, unaAccionOfensiva, unContexto):
        equipoDefensor = unContexto.equipoDefensor()
        equipoAtacante = unContexto.equipoAtacante()

        jugadorAtacante = unPase.jugadorEjecutante()
        unaPosicion = equipoAtacante.posicionDe(jugadorAtacante)
        jugadorDefensor = equipoDefensor.jugadorEnPosicion(unaPosicion)

        unaAccionDefensiva = unaAccionOfensiva.defenderCon(self, jugadorDefensor)
        return unaAccionDefensiva

    def defenderPase(self, unPase, jugadorDefensor):
        unaAccionDefensiva = Intercepcion(jugadorDefensor)
        return unaAccionDefensiva

    def defenderTiro(self, unTiro, jugadorDefensor):
        unaAccionDefensiva = Bloqueo(jugadorDefensor)
        return unaAccionDefensiva
