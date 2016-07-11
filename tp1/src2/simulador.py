from resolvedores import resolvedor

class Simulador(object):
    def __init__(self, unaListaDeEstadisticas):
        self._estadisticasJugadores = unaListaDeEstadisticas

    def estadisticasDe(self, unJugador):
        return self._estadisticasJugadores.estadisticasDe(self, unJugador)

    ### Eleccion de jugadas
    def elegirJugadasParaTurno(self, unTurno):
        unContexto = unTurno.contexto()

        unaJugadaOfensiva = obtenerJugadaOfensivaParaTurno(unTurno)
        unContexto.jugadaOfensiva(unaJugadaOfensiva)

        unaJugadaDefensiva = obtenerJugadaDefensivaParaTurno(unTurno)
        unContexto.jugadaDefensiva(unaJugadaDefensiva)

    def obtenerJugadaOfensivaParaTurno(self, unTurno):
        unContexto = unTurno.contexto()
        equipoAtacante = contexto.equipoAtacante()

        unTecnico = equipoAtacante.tecnico()
        unaJugadaOfensiva = elegirJugadaOfensivaConTecnico(unTecnico)

        return unaJugadaOfensiva

    def obtenerJugadaDefensivaParaTurno(self, unTurno):
        unContexto = unTurno.contexto()
        equipoDefensor = contexto.equipoDefensor()

        unTecnico = equipoDefensor.tecnico()
        unaJugadaDefensiva = elegirJugadaDefensivaConTecnico(unTecnico)

        return unaJugadaDefensiva

    def elegirJugadaOfensivaConTecnico(self, unTecnico):
        unLibroDeJugadas = unTecnico.libroDeJugadas()
        unDiccDeJugadasConFrec = unLibroDeJugadas.jugadasOfensivasConFrecuencias()

        unaFrecuencia = random.random()

        unaJugadaOfensiva = elegirJugadaConFrecuencia(unDiccDeJugadasConFrec, unaFrecuencia)

        return unaJugadaOfensiva

    def elegirJugadaDefensivaConTecnico(self, unTecnico):
        unLibroDeJugadas = unTecnico.libroDeJugadas()
        unDiccDeJugadasConFrec = unLibroDeJugadas.jugadasDefensivasConFrecuencias()

        unaFrecuencia = random.random()

        unaJugadaDefensiva = elegirJugadaConFrecuencia(unDiccDeJugadasConFrec, unaFrecuencia)

        return unaJugadaDefensiva

    def elegirJugadaConFrecuencia(self, unDiccDeJugadasConFrec, unaFrecuencia):
        # TODO
        return false


    ### Ejecucion de jugadas
    def elegirYEjecutarAcciones(self, unTurno):
        unContexto = unTurno.contexto()

        unaJugadaOfensiva = unContexto.jugadaOfensiva()
        unaAccionOfensiva = unaJugadaOfensiva.proximaAccionOfensiva(unContexto)

        unaJugadaDefensiva = unContexto.jugadaDefensiva()
        unaAccionDefensiva = unaJugadaDefensiva.accionParaDefender(unaAccionOfensiva, unContexto)

        unResultado = ejecutarAcciones(unaAccionOfensiva, unaAccionDefensiva, unTurno)

        return unResultado

    def ejecutarAcciones(self, unaAccionOfensiva, unaAccionDefensiva, unTurno):
        ''' Me fijo si la accion ofensiva o la defensiva tienen exito, y continua el juego en base a esos resultados.'''
        unContexto = unTurno.contexto()

        unResolvedorDeAccionOfensiva = unaAccionOfensiva.resolvedorPara()
        unResultadoOfensivo = unResolvedorDeAccionOfensiva.esExitoso(unaAccionOfensiva)

        unResolvedorDeAccionDefensiva = unaAccionDefensiva.resolvedorPara()
        unResultadoDefensivo = unResolvedorDeAccionDefensiva.esExitoso(unaAccionDefensiva)

        if(unResultadoDefensivo):
            unResultado = unResolvedorDeAccionDefensiva.continuarConExito(unaAccionDefensiva, unTurno, self)
        else:
            if(unResultadoOfensivo):
                unResultado = unResolvedorDeAccionOfensiva.continuarConExito(unaAccionOfensiva, unTurno, self)
            else:
                unResultado = unResolvedorDeAccionOfensiva.continuarConFallo(unTurno, self)

        return unResultado

    ### Resolvedores
    def resolvedorParaBloqueo(self):
        unResolvedorDeBloqueo = resolvedor.ResolvedorBloqueo()
        return unResolvedorDeBloqueo

    def resolvedorParaIntercepcion(self):
        unResolvedorDeIntercepcion = resolvedor.ResolvedorIntercepcion()
        return unResolvedorDeIntercepcion

    def resolvedorParaPase(self):
        unResolvedorDePase = resolvedor.ResolvedorPase()
        return unResolvedorDePase

    def resolvedorParaTiro2Puntos(self):
        unResolvedorDeTiro2Puntos = resolvedor.ResolvedorTiro2Puntos()
        return unResolvedorDeTiro2Puntos

    def resolvedorParaTiro3Puntos(self, unTiro3Puntos):
        unResolvedorDeTiro3Puntos = resolvedor.ResolvedorTiro3Puntos()
        return unResolvedorDeTiro3Puntos

    ### Fin de turno
    def pelotaAfueraPara(self, unTurno):
        unContexto = unTurno.contexto()
        equipoAtacante = unContexto.equipoAtacante()
        equipoDefensor = unContexto.equipoDefensor()

        return Resultado(equipoAtacante, 0, equipoDefensor, 0)

    def encestarDoble(self, unTurno):
        unContexto = unTurno.contexto()
        equipoAtacante = unContexto.equipoAtacante()
        equipoDefensor = unContexto.equipoDefensor()

        return Resultado(equipoAtacante, 2, equipoDefensor, 0)

    def encestarTriple(self, unTurno):
        unContexto = unTurno.contexto()
        equipoAtacante = unContexto.equipoAtacante()
        equipoDefensor = unContexto.equipoDefensor()

        return Resultado(equipoAtacante, 3, equipoDefensor, 0)
