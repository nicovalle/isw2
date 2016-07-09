class Turno(object):
    def __init__(self, unContexto):
        self._contexto = unContexto

    def jugarPosesion(self, equipoAtacante, equipoDefensor, unSimulador):
        iniciarPosesion(equipoAtacante, equipoDefensor)

        unSimulador.elegirJugadasParaTurnos(self)
        unResultado = unSimulador.elegirYEjecutarAcciones(self)

        return unResultado

    def iniciarPosesion(self, equipoAtacante, equipoDefensor):
        self._contexto.equipoAtacante(equipoAtacante)
        self._contexto.equipoDefensor(equipoDefensor)
        self._contexto.pasoDeJugadaOfensiva(0)
