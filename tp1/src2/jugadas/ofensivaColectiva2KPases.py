# TODO -> PARA HACER. Tener en cuenta ultimo pase.
class Tecnico(object):
    def __init__(self, unNombre, unApellido, unLibroDeJugadas):
        self._nombre = unNombre
        self._apellido = unApellido
        self._libroDeJugadas = unLibroDeJugadas

    def nombre(self):
        return self._nombre

    def apellido(self):
        return self._apellido

    def nombreCompleto(self):
        return self._nombre+" "+self._apellido

    def libroDeJugadas(self):
        return self._libroDeJugadas
