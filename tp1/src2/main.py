from jugador import *
from tecnico import *
from equipo import *
from posicion import *

jugador1 = Jugador("manu", "ginobili")
jugador2 = Jugador("pepe", "ginobili")
jugador3 = Jugador("jose", "ginobili")
jugador4 = Jugador("tim", "ginobili")
jugador5 = Jugador("michael", "ginobili")

jugador6 = Jugador("stephen", "curry")
jugador7 = Jugador("pepper", "curry")
jugador8 = Jugador("chicken", "curry")
jugador9 = Jugador("rice", "curry")
jugador10 = Jugador("uncurry", "curry")

tecnico1 = Tecnico("pep", "guardiola", "unlibro")
tecnico2 = Tecnico("carlo", "antilope", "otrolibro")

equipo1 = Equipo("losSpurs", [jugador1, jugador2, jugador3, jugador4, jugador5], jugador1, tecnico1)
equipo2 = Equipo("losWarriors", [jugador6, jugador7, jugador8, jugador9, jugador10], jugador6, tecnico2)

print equipo1.jugadorEnPosicion(Posicion("asd")).nombre()
print equipo2.tecnico().nombre()
