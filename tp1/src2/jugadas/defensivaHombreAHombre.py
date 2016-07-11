from defensiva import *

class DefensivaHombreAHombre(Defensiva):
    def __init__(self):
        self._nombre = "Hombre a Hombre"

    def nombre(self):
        return self._nombre

    def accionParaDefender(self, unaAccionOfensiva, unContexto):
        equipoDefensor = unContexto.equipoDefensor()
        equipoAtacante = unContexto.equipoAtacante()

        jugadorAtacante = unaAccionOfensiva.jugadorEjecutante()
        unaPosicion = equipoAtacante.posicionDe(jugadorAtacante)
        jugadorDefensor = equipoDefensor.jugadorEnPosicion(unaPosicion)

        unaAccionDefensiva = unaAccionOfensiva.defenderCon(self, jugadorDefensor)
        return unaAccionDefensiva

    def defenderPase(self, unPase, jugadorDefensor):
        unaAccionDefensiva = accion.Intercepcion(jugadorDefensor)
        return unaAccionDefensiva

    def defenderTiro(self, unTiro, jugadorDefensor):
        unaAccionDefensiva = accion.Bloqueo(jugadorDefensor)
        return unaAccionDefensiva
