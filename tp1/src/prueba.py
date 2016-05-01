from jugador import *
from equipo import *
from participante import *


jugador1 = Jugador("manu", "ginobili", 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 1234.1)
jugador2 = Jugador("pepe", "ginobili", 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 1234.2)
jugador3 = Jugador("jose", "ginobili", 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 1234.3)
jugador4 = Jugador("tim", "ginobili", 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 1234.4)
jugador5 = Jugador("michael", "ginobili", 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 1234.5)

equipo = Equipo("spurs", jugador1, jugador2, jugador3, jugador4, jugador5, jugador1, "pep guardiola", "nico")

print equipo.nombre()
print equipo.base().nombre()
print equipo.alero().nombre()
print equipo.escolta().nombre()
print equipo.alaPivot().nombre()
print equipo.pivot().nombre()
print equipo.estrella().nombre()
print equipo.tecnico()
print equipo.dueno()

participante = Participante("nicolas vallejo", "nicopr08@gmail.com", set(), 10000000, 0)
participante.agregarEquipo(equipo)
print (map(lambda equipo: equipo.nombre(), participante.equipos()))