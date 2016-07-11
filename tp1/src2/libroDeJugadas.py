class LibroDeJugadas(object):
    def __init__(self, unDiccDeJugadasOfensivasConFrec=dict(), unDiccDeJugadasDefensivasConFrec=dict()):
        self._ofensivas = unDiccDeJugadasOfensivasConFrec
        self._defensivas = unDiccDeJugadasDefensivasConFrec

    def jugadasDefensivasConFrecuencias(self):
        return self._defensivas

    def jugadasOfensivasConFrecuencias(self):
        return self._ofensivas

    def agregarJugadaOfensivaConFrecuencia(self, unaJugadaOfensiva, unaFrecuencia):
        self._ofensivas[unaJugadaOfensiva] = unaFrecuencia

    def agregarJugadaDefensivaConFrecuencia(self, unaJugadaDefensiva, unaFrecuencia):
        self._defensivas[unaJugadaDefensiva] = unaFrecuencia
