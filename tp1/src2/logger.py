class Logger(object):

    def loggearInicioTurno(numeroTurno):
        #arranca el turno numero X
        return true

    def loggearEmpate(numeroTurno):
        #Empate en el turno numero X
        return true

    def loggearVictoria(equipoGanador, equipoPerdedor, puntajeGanador, puntajePerdedor):
        #El equipo A, vence al equipo B por X tantos contra Y
        return true

    def loggearInicioPosesion(equipoAtacante):
        #arranca atacando tal equipo
        return true

    def loggearPelotaAfuera():
        #la pelota se fue
        return true

    def loggearPaseExitoso(paseEmisor, paseReceptor, paseInterceptor):
        #pase exitoso entre A y B, que C no logra interceptar
        return true

    def loggearBloqueo(tirador, bloqueador):
        #A le bloquea el tiro a B
        return true

    def loggearIntercepcionExito(paseEmisor, paseReceptor, paseInterceptor):
        #A le intercepta el pase a B, cuando le hacia un pase a C
        return true

    def loggearPaseIntercepcionFracaso(paseEmisor, paseReceptor, paseInterceptor):
        #A no se la logra pasar a B y C no la logra interceptar -> sale de la cancha.
        return true

    def loggearEncestarDoble(tirador, bloqueador):
        #A lanza un doble, B no lo logra bloquear, y A convierte
        return true

    def loggearEncestarTriple(tirador, bloqueador):
        #A lanza un triple, B no lo logra bloquear, y A convierte
        return true

    def loggearReboteoIntento(jugador, equipo):
        #El jugador A del equipo B, intenta agarrar un rebote
        return true

    def loggearReboteoExito(jugador, equipo):
        #El jugador A del equipo B, logra agarrar un rebote
        return true
