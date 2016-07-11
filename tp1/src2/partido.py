import random
import sys

from turno import *
from contexto import *
from resultado import *

class Partido(object):
    def __init__(self, unEquipo, otroEquipo):
        self._equipoA = unEquipo
        self._equipoB = otroEquipo
        self._resultado = Resultado(unEquipo, 0, otroEquipo, 0)
        self._equipoSacador = None
        self._turnoNumero = 1
        self._turnoExtra = 1

        self._cantidadDeTurnos = 40

    def jugarCon(self, unSimulador, unLogger):
        self._equipoSacador = random.choice([self._equipoA, self._equipoB])

        while(self._turnoNumero <= 40):
            unContexto = Contexto()
            unTurno = Turno(unContexto, unLogger)
            unLogger.loggearInicioTurno(self._turnoNumero)
            unLogger.loggearResultadoParcial(self._equipoA, self._equipoB, self._resultado.parcialDeEquipo(self._equipoA), self._resultado.parcialDeEquipo(self._equipoB))

            unResultadoParcial = unTurno.jugarPosesion(self.equipoSacador(), self.equipoNoSacador(), unSimulador)
            self._resultado = self._resultado.sumarA(unResultadoParcial)
            self._turnoNumero += 1
            self.invertirEquipos()

        self._resultado = Resultado(self._equipoA, 0, self._equipoB, 0)

        while(self.empatado()):
            unLogger.loggearInicioTiempoExtra()
            self.jugarTiempoExtra(unSimulador, unLogger)

        equipoGanador = self.equipoQueVaGanando()
        equipoPerdedor = self.equipoQueNoVaGanando()
        resultadoGanador = self._resultado.parcialDeEquipo(equipoGanador)
        resultadoPerdedor = self._resultado.parcialDeEquipo(equipoPerdedor)
        unLogger.loggearVictoria(equipoGanador, equipoPerdedor, resultadoGanador, resultadoPerdedor)

    def jugarTiempoExtra(self, unSimulador, unLogger):
        self._turnoExtra = 1
        while(self._turnoExtra <= 6):
            unContexto = Contexto()
            unTurno = Turno(unContexto, unLogger)
            unLogger.loggearInicioTurno(self._turnoNumero)

            unResultadoParcial = unTurno.jugarPosesion(self.equipoSacador(), self.equipoNoSacador(), unSimulador)
            self._resultado = self._resultado.sumarA(unResultadoParcial)
            self._turnoNumero += 1
            self._turnoExtra += 1

            self.invertirEquipos()

        return

    def empatado(self):
        return self._resultado.parcialDeEquipo(self._equipoA) == self._resultado.parcialDeEquipo(self._equipoB)

    def equipoQueVaGanando(self):
        resultadoEquipoA = self._resultado.parcialDeEquipo(self._equipoA)
        resultadoEquipoB = self._resultado.parcialDeEquipo(self._equipoB)
        if(resultadoEquipoA == resultadoEquipoB):
            return None
        elif(resultadoEquipoA > resultadoEquipoB):
            return self._equipoA
        else:
            return self._equipoB

    def equipoQueNoVaGanando(self):
        return self.otroEquipo(self.equipoQueVaGanando())

    def equipoSacador(self):
        return self._equipoSacador

    def equipoNoSacador(self):
        return self.otroEquipo(self.equipoSacador())

    def invertirEquipos(self):
        self._equipoSacador = self.equipoNoSacador()

    def otroEquipo(self, unEquipo):
        equipos = [self._equipoA, self._equipoB]

        if(unEquipo not in equipos):
            sys.exit("Partido.otroEquipo(): el equipo pasado como parametro no pertenece al partido.")

        equipos.remove(unEquipo)
        return equipos[0]

#    def ultimoEquipoSacador(self, unEquipo=None):
#        if(ultimoEquipoSacador is None):
#            return self._ultimoEquipoSacador
#        else:
#            self._ultimoEquipoSacador = unEquipo
