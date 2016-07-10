# TODO -> PARA HACER. Tener en cuenta ultimo pase.
class OfensivaColectiva2KPases(object):
    def __init__(self, cantPases):
        self._k = cantPases

    def proximaAccionOfensiva(self, unContexto):
        jugadorAtacante = unContexto.jugadorConPosesion()
        pasoJugadaOfensiva = unContexto.pasoDeJugadaOfensiva()
        equipoAtacante = unContexto.equipoAtacante()
        e
        return self._nombre

    def elegirJugadorDistintoA(self, unJugador, unEquipo):
        return unEquipo.jugadorDistintoA(unJugador)

    def elegirJugadorEntre(unaPosicion, otraPosicion, unaOtraPosicion, unEquipo):
        return unEquipo.jugadorEnPosiciones3(unaPosicion, otraPosicion, unaOtraPosicion)

    def apellido(self):
        return self._apellido

    def nombreCompleto(self):
        return self._nombre+" "+self._apellido

    def libroDeJugadas(self):
        return self._libroDeJugadas
