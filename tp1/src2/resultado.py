class Resultado(object):
    def __init__(self, equipoAtacante, parcialAtacante, equipoDefensor, parcialDefensor):
        self._equipoAtacante = equipoAtacante
        self._parcialAtacante = parcialAtacante
        self._equipoDefensor = equipoDefensor
        self._parcialDefensor = parcialDefensor

    def equipoAtacante(self):
        return self._equipoAtacante

    def parcialAtacante(self):
        return self._parcialAtacante

    def equipoDefensor(self):
        return self._equipoDefensor

    def parcialDefensor(self):
        return self._parcialDefensor
