import sys

class RegistroDeEstadisticasDeJugador(object):
    def __init__(self, unDiccDeJugadoresYEstadisticas=dict()):
        self._estadisticas = unDiccDeJugadoresYEstadisticas

    def estadisticasDe(self, unJugador):
        return self._estadisticas[unJugador]

    def actualizarEstadistica(self, unJugador, unaEstadistica):
        if(unJugador not in self._estadisticas.keys()):
            sys.exit("RegistroDeEstadisticasDeJugador.actualizarEstadistica(): no se encontro al jugador, no se puede actualizar")

    def registrarEstadistica(self, unJugador, unaEstadistica):
        if(unJugador in self._estadisticas.keys()):
            self.actualizarEstadistica(unJugador, unaEstadistica)
        else:
            self._estadisticas[unJugador] = unaEstadistica
