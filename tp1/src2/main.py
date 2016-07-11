from jugador import *

from jugadas import ofensiva,defensiva
from libroDeJugadas import *
from tecnico import *

from posiciones import posicion
from equipo import *

from estadisticas import *
from registroDeEstadisticasDeJugador import *

from partido import *
from simulador import *
from logger import *
from resolvedores import *

### JUGADORES
## EQUIPO 1
jugador1 = Jugador("manu", "ginobili")
jugador2 = Jugador("tim", "ginobili")
jugador3 = Jugador("tony", "ginobili")
jugador4 = Jugador("kawhi", "ginobili")
jugador5 = Jugador("lamarcus", "ginobili")
## EQUIPO 2
jugador6 = Jugador("stephen", "curry")
jugador7 = Jugador("pepper", "curry")
jugador8 = Jugador("chicken", "curry")
jugador9 = Jugador("rice", "curry")
jugador10 = Jugador("uncurry", "curry")

### LIBRODEJUGADAS
## EQUIPO 1
unaJugadaOfensiva = ofensiva.OfensivaColectiva2KPases(4)
unaJugadaOfensiva2 = ofensiva.OfensivaColectiva3KPases(3)
unDiccOfensivo = dict({unaJugadaOfensiva: 0.5, unaJugadaOfensiva2: 0.5})
unaJugadaDefensiva = defensiva.DefensivaHombreAHombre()
unDiccDefensivo = dict({unaJugadaDefensiva: 1.0})
unLibroDeJugadas = LibroDeJugadas(unDiccOfensivo, unDiccDefensivo)
## EQUIPO 2
otraJugadaOfensiva = ofensiva.OfensivaColectiva2KPases(3)
otraJugadaOfensiva2 = ofensiva.OfensivaColectiva3KPases(5)
otraJugadaOfensiva3 = ofensiva.OfensivaMVP()
otroDiccOfensivo = dict({otraJugadaOfensiva: 0.3, otraJugadaOfensiva2: 0.3, otraJugadaOfensiva3: 0.4})
otraJugadaDefensiva = defensiva.DefensivaHombreAHombre()
otroDiccDefensivo = dict({otraJugadaDefensiva: 1.0})
otroLibroDeJugadas = LibroDeJugadas(otroDiccOfensivo, otroDiccDefensivo)

### TECNICOS
tecnico1 = Tecnico("pep", "guardiola", unLibroDeJugadas)
tecnico2 = Tecnico("carlo", "antilope", otroLibroDeJugadas)

### EQUIPOS
equipo1 = Equipo("losSpurs", [jugador1, jugador2, jugador3, jugador4, jugador5], jugador3, tecnico1)
equipo2 = Equipo("losWarriors", [jugador6, jugador7, jugador8, jugador9, jugador10], jugador6, tecnico2)

### ESTADISTICAS
## EQUIPO 1
registroDeEstadisticasDeJugador = RegistroDeEstadisticasDeJugador()
estadisticasDeJugador1 = Estadisticas(0.426, 0.429, 2.7, 2.5, 0.3, 0.8, 0.7, 6.7)
registroDeEstadisticasDeJugador.registrarEstadistica(jugador1, estadisticasDeJugador1)
estadisticasDeJugador2 = Estadisticas(0.423, 0, 4.8, 1.4, 1.3, 0.2, 1.0, 5.9)
registroDeEstadisticasDeJugador.registrarEstadistica(jugador2, estadisticasDeJugador2)
estadisticasDeJugador3 = Estadisticas(0.449, 0.250, 2.2, 5.3, 0.2, 0.6, 1.8, 10.4)
registroDeEstadisticasDeJugador.registrarEstadistica(jugador3, estadisticasDeJugador3)
estadisticasDeJugador4 = Estadisticas(0.50, 0.436, 6.3, 2.8, 1.4, 2.6, 1.6, 22.5)
registroDeEstadisticasDeJugador.registrarEstadistica(jugador4, estadisticasDeJugador4)
estadisticasDeJugador5 = Estadisticas(0.521, 1.000, 8.3, 1.0, 1.4, 0.4, 1.1, 21.9)
registroDeEstadisticasDeJugador.registrarEstadistica(jugador5, estadisticasDeJugador5)
## EQUIPO 2
# stephen curry
estadisticasDeJugador6 = Estadisticas(0.438, 0.404, 5.5, 5.2, 0.3, 1.4, 4.2, 25.1)
registroDeEstadisticasDeJugador.registrarEstadistica(jugador6, estadisticasDeJugador6)
# shaun livingston
estadisticasDeJugador7 = Estadisticas(0.488, 0, 3.2, 3.3, 0.2, 0.5, 1.2, 8.2)
registroDeEstadisticasDeJugador.registrarEstadistica(jugador7, estadisticasDeJugador7)
# harrison barnes
estadisticasDeJugador8 = Estadisticas(0.385, 0.342, 4.7, 1.3, 0.2, 0.7, 0.8, 9)
registroDeEstadisticasDeJugador.registrarEstadistica(jugador8, estadisticasDeJugador8)
# klay thompson
estadisticasDeJugador9 = Estadisticas(0.44, 0.424, 3.7, 2.3, 0.4, 1.1, 2, 24.3)
registroDeEstadisticasDeJugador.registrarEstadistica(jugador9, estadisticasDeJugador9)
# draymond green
estadisticasDeJugador10 = Estadisticas(0.431, 0.365, 9.9, 6, 1.8, 1.6, 2.4, 15.4)
registroDeEstadisticasDeJugador.registrarEstadistica(jugador10, estadisticasDeJugador10)

unLogger = Logger()
unPartido = Partido(equipo1, equipo2)
unSimulador = Simulador(registroDeEstadisticasDeJugador, unLogger)

unPartido.jugarCon(unSimulador, unLogger)
