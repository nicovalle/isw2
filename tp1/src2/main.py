from jugador import *
from tecnico import *
from equipo import *
from posiciones import posicion
from jugadas import *
from resolvedores import *
from acciones import *
from listaDeEstadisticas import *
from estadisticas import *

listaDeEstadisticas = ListaDeEstadisticas()

jugador1 = Jugador("manu", "ginobili")
estadisticasDeJugador1 = Estadisticas(0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8)
listaDeEstadisticas.agregarEstadisticasDe(jugador1, estadisticasDeJugador1)
jugador2 = Jugador("pepe", "ginobili")
estadisticasDeJugador2 = Estadisticas(0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8)
listaDeEstadisticas.agregarEstadisticasDe(jugador2, estadisticasDeJugador2)
jugador3 = Jugador("jose", "ginobili")
estadisticasDeJugador3 = Estadisticas(0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8)
listaDeEstadisticas.agregarEstadisticasDe(jugador3, estadisticasDeJugador3)
jugador4 = Jugador("tim", "ginobili")
estadisticasDeJugador4 = Estadisticas(0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8)
listaDeEstadisticas.agregarEstadisticasDe(jugador4, estadisticasDeJugador4)
jugador5 = Jugador("michael", "ginobili")
estadisticasDeJugador5 = Estadisticas(0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8)
listaDeEstadisticas.agregarEstadisticasDe(jugador5, estadisticasDeJugador5)

jugador6 = Jugador("stephen", "curry")
estadisticasDeJugador6 = Estadisticas(0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8)
listaDeEstadisticas.agregarEstadisticasDe(jugador6, estadisticasDeJugador6)
jugador7 = Jugador("pepper", "curry")
estadisticasDeJugador7 = Estadisticas(0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8)
listaDeEstadisticas.agregarEstadisticasDe(jugador7, estadisticasDeJugador7)
jugador8 = Jugador("chicken", "curry")
estadisticasDeJugador8 = Estadisticas(0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8)
listaDeEstadisticas.agregarEstadisticasDe(jugador8, estadisticasDeJugador8)
jugador9 = Jugador("rice", "curry")
estadisticasDeJugador9 = Estadisticas(0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8)
listaDeEstadisticas.agregarEstadisticasDe(jugador9, estadisticasDeJugador9)
jugador10 = Jugador("uncurry", "curry")
estadisticasDeJugador10 = Estadisticas(0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8)
listaDeEstadisticas.agregarEstadisticasDe(jugador10, estadisticasDeJugador10)

tecnico1 = Tecnico("pep", "guardiola", "unlibro")
tecnico2 = Tecnico("carlo", "antilope", "otrolibro")

equipo1 = Equipo("losSpurs", [jugador1, jugador2, jugador3, jugador4, jugador5], jugador1, tecnico1)
equipo2 = Equipo("losWarriors", [jugador6, jugador7, jugador8, jugador9, jugador10], jugador6, tecnico2)

print equipo1.jugadorEnPosicion(posicion.Base()).nombre()
print equipo2.tecnico().nombre()
