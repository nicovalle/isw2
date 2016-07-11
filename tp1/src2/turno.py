class Turno(object):
    def __init__(self, unContexto, unLogger = None):
        self._contexto = unContexto
        self._logger = unLogger

    def contexto(self):
        return self._contexto

    def jugarPosesion(self, equipoAtacante, equipoDefensor, unSimulador):
        iniciarPosesion(equipoAtacante, equipoDefensor)

        unSimulador.elegirJugadasParaTurnos(self)
        unResultado = unSimulador.elegirYEjecutarAcciones(self)

        return unResultado

    def iniciarPosesion(self, equipoAtacante, equipoDefensor):
        self._contexto.equipoAtacante(equipoAtacante)
        self._contexto.equipoDefensor(equipoDefensor)
        self._contexto.pasoDeJugadaOfensiva(0)
        self._logger.loggearInicioPosesion(self._contexto.equipoAtacante())
