class ListaDeEstadisticas(object):
    def __init__(self, unDiccDeJugadoresYEstadisticas=dict()):
        self._estadisticas = unDiccDeJugadoresYEstadisticas

    def estadisticasDe(self, unJugador):
        return self._estadisticas[unJugador]

    def agregarEstadisticasDe(self, unJugador, estadisticasDeUnJugador):
        self._estadisticas[unJugador] = estadisticasDeUnJugador

    def removerEstadisticasDe(self, unJugador):
        self._estadisticas.pop(unJugador)
