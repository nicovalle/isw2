class Contexto(object):
    def equipoAtacante(self, unEquipoOfensivo=None):
        if(unEquipoOfensivo is None):
            return self._equipoAtacante
        else:
            self._equipoAtacante = unEquipoOfensivo

    def equipoDefensor(self, unEquipoDefensor=None):
        if(unEquipoDefensor is None):
            return self._equipoDefensor
        else:
            self._equipoDefensor = unEquipoDefensor

    def jugadorConPosesion(self, unJugadorOfensivo=None):
        if(unJugadorOfensivo is None):
            return self._jugadorConPosesion
        else:
            self._jugadorConPosesion = unJugadorOfensivo

    def pasoDeJugadaOfensiva(self, pasoJugadaOfensiva=None):
        if(pasoJugadaOfensiva is None):
            return self._pasoDeJugadaOfensiva
        else:
            self._pasoDeJugadaOfensiva = pasoJugadaOfensiva

    def incrementarPasoJugadaOfensiva(self):
        self._pasoDeJugadaOfensiva += 1

    def jugadaOfensiva(self, unaJugadaOfensiva=None):
        if(unaJugadaOfensiva is None):
            return self._jugadaOfensiva
        else:
            self._jugadaOfensiva = unaJugadaOfensiva

    def jugadaDefensiva(self, unaJugadaDefensiva=None):
        if(unaJugadaDefensiva is None):
            return self._jugadaDefensiva
        else:
            self._jugadaDefensiva = unaJugadaDefensiva
