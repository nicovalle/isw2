class Logger(object):

    def loggearinicioPosesion(equipoAtacante):
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

    def loggearIntercepcionExito(tirador, bloqueador):
        #A le intercepta el pase a B
        return true

    def loggearPaseIntercepcionFracaso(paseEmisor, paseReceptor, paseInterceptor):
        #A no se la logra pasar a B y C no la logra interceptar, sale de la cancha.
        return true

    def loggearEncesatarDoble(tirador, bloqueador):
        #A lanza un doble, B no lo logra bloquear, y convierte
        return true

    def loggearEncesatarTriple(tirador, bloqueador):
        #A lanza un triple, B no lo logra bloquear, y convierte
        return true

    def loggearReboteoIntento(jugador):
        #El jugador A del equipo B, intenta agarrar un rebote
        return true

    def loggearReboteoExito(jugador):
        #El jugador A del equipo B, logra agarrar un rebote
        return true
