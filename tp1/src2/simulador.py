from resolvedores import resolvedor
from resultado import *

import random
import sys

class Simulador(object):
    def __init__(self, unRegistroDeEstadisticas, unLogger):
        self._estadisticasJugadores = unRegistroDeEstadisticas
        self._logger = unLogger

    def estadisticasDe(self, unJugador):
        return self._estadisticasJugadores.estadisticasDe(unJugador)

    def logger(self):
        return self._logger

    ### Eleccion de jugadas
    def elegirJugadasParaTurno(self, unTurno):
        unContexto = unTurno.contexto()

        unaJugadaOfensiva = self.obtenerJugadaOfensivaParaTurno(unTurno)
        unContexto.jugadaOfensiva(unaJugadaOfensiva)

        unaJugadaDefensiva = self.obtenerJugadaDefensivaParaTurno(unTurno)
        unContexto.jugadaDefensiva(unaJugadaDefensiva)

    def obtenerJugadaOfensivaParaTurno(self, unTurno):
        unContexto = unTurno.contexto()
        equipoAtacante = unContexto.equipoAtacante()

        unTecnico = equipoAtacante.tecnico()
        unaJugadaOfensiva = self.elegirJugadaOfensivaConTecnico(unTecnico)
        self._logger.loggearEleccionJugada(equipoAtacante, unaJugadaOfensiva)

        return unaJugadaOfensiva

    def obtenerJugadaDefensivaParaTurno(self, unTurno):
        unContexto = unTurno.contexto()
        equipoDefensor = unContexto.equipoDefensor()

        unTecnico = equipoDefensor.tecnico()
        unaJugadaDefensiva = self.elegirJugadaDefensivaConTecnico(unTecnico)
        self._logger.loggearEleccionJugada(equipoDefensor, unaJugadaDefensiva)

        return unaJugadaDefensiva

    def elegirJugadaOfensivaConTecnico(self, unTecnico):
        unLibroDeJugadas = unTecnico.libroDeJugadas()
        unDiccDeJugadasConFrec = unLibroDeJugadas.jugadasOfensivasConFrecuencias()

        unaFrecuencia = random.random()
        unaJugadaOfensiva = self.elegirJugadaConFrecuencia(unDiccDeJugadasConFrec, unaFrecuencia)

        return unaJugadaOfensiva

    def elegirJugadaDefensivaConTecnico(self, unTecnico):
        unLibroDeJugadas = unTecnico.libroDeJugadas()
        unDiccDeJugadasConFrec = unLibroDeJugadas.jugadasDefensivasConFrecuencias()

        unaFrecuencia = random.random()
        unaJugadaDefensiva = self.elegirJugadaConFrecuencia(unDiccDeJugadasConFrec, unaFrecuencia)

        return unaJugadaDefensiva

    def elegirJugadaConFrecuencia(self, unDiccDeJugadasConFrec, unaFrecuencia):
        acumulado = 0
        for key in unDiccDeJugadasConFrec.keys():
            acumulado += unDiccDeJugadasConFrec[key]
            if(unaFrecuencia < acumulado):
                return key
        sys.exit("Simulador.elegirJugadaConFrecuencia(): no se pudo elegir jugada.")

    ### Ejecucion de jugadas
    def elegirYEjecutarAcciones(self, unTurno):
        unContexto = unTurno.contexto()

        unaJugadaOfensiva = unContexto.jugadaOfensiva()
        unaAccionOfensiva = unaJugadaOfensiva.proximaAccionOfensiva(unContexto)

        unaJugadaDefensiva = unContexto.jugadaDefensiva()
        unaAccionDefensiva = unaJugadaDefensiva.accionParaDefender(unaAccionOfensiva, unContexto)

        unResultado = self.ejecutarAcciones(unaAccionOfensiva, unaAccionDefensiva, unTurno)

        return unResultado

    def ejecutarAcciones(self, unaAccionOfensiva, unaAccionDefensiva, unTurno):
        ''' Me fijo si la accion ofensiva o la defensiva tienen exito, y continua el juego en base a esos resultados.'''
        unContexto = unTurno.contexto()

        unResolvedorDeAccionOfensiva = unaAccionOfensiva.resolvedorPara(self)
        unResultadoOfensivo = unResolvedorDeAccionOfensiva.esExitoso(unaAccionOfensiva, self)

        unResolvedorDeAccionDefensiva = unaAccionDefensiva.resolvedorPara(self)
        unResultadoDefensivo = unResolvedorDeAccionDefensiva.esExitoso(unaAccionDefensiva, self)

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

    def resolvedorParaTiro3Puntos(self):
        unResolvedorDeTiro3Puntos = resolvedor.ResolvedorTiro3Puntos()
        return unResolvedorDeTiro3Puntos

    ### Fin de turno
    def pelotaAfueraPara(self, unTurno):
        self._logger.loggearPelotaAfuera()

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
