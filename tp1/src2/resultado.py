import sys

class Resultado(object):
    def __init__(self, unEquipo, unParcialEnPtos, otroEquipo, otroParcialEnPtos):
        self._resultado = dict({unEquipo: unParcialEnPtos, otroEquipo: otroParcialEnPtos})

    def parcialDeEquipo(self, unEquipo):
        return self._resultado[unEquipo]

    def sumarA(self, otroResultado):
        if(self._resultado.viewkeys() == otroResultado._resultado.viewkeys()):
            unEquipo = self._resultado.keys()[0]
            otroEquipo = self._resultado.keys()[1]

            return Resultado(unEquipo, self._resultado[unEquipo]+otroResultado._resultado[unEquipo], otroEquipo, self._resultado[otroEquipo]+otroResultado._resultado[otroEquipo])
        else:
            sys.exit("Resultado.sumarA(): no se pueden sumar resultados con distintos equipos")
