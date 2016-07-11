class Logger(object):

    def loggearInicioTurno(numeroTurno):
        print('Se inicia el turno numero ' + numeroTurno)
        return

    def loggearEmpate(numeroTurno):
        print('Empate en el turno numero ' + numeroTurno)
        return

    def loggearVictoria(equipoGanador, equipoPerdedor, puntajeGanador, puntajePerdedor):
        print('El equipo ' + equipoGanador.nombre + ' vence al equipo ' + equipoPerdedor.nombre + ' por ' + puntajeGanador + ' tantos contra ' + puntajePerdedor)
        return

    def loggearInicioPosesion(equipoAtacante):
        print('Se inicia la posesion del equipo ' + equipoAtacante.nombre)
        return

    def loggearPelotaAfuera():
        print('La pelota sale de la cancha!')
        return

    def loggearPaseExitoso(paseEmisor, paseReceptor, paseInterceptor):
        print paseEmisor.nombre + ' se la pasa a ' + paseReceptor.nombre + ' y ' + paseInterceptor + ' no logra interceptarla')
        return

    def loggearBloqueo(tirador, bloqueador):
        print tirador.nombre + ' lanza el balon hacia el aro, pero ' + bloqueador + ' la intercepta')
        return

    def loggearIntercepcionExito(paseEmisor, paseReceptor, paseInterceptor):
        print paseEmisor.nombre + ' se la pasa a ' + paseReceptor.nombre + ' y ' + paseInterceptor + ' no logra interceptarla')
        return

    def loggearPaseIntercepcionFracaso(paseEmisor, paseReceptor, paseInterceptor):
        print paseEmisor.nombre + ' no logra realizar el pase  a ' + paseReceptor.nombre + ' y ' + paseInterceptor + ' no logra interceptarla')
        return

    def loggearEncestarDoble(tirador, bloqueador, equipoTirador):
        print tirador.nombre + 'lanza al aro, ' + bloqueador.nombre + ' no logra interceptarla, y anota. Dos puntos para ' + equipoTirador.nombre)
        return

    def loggearEncestarTriple(tirador, bloqueador, equipoTirador):
        print tirador.nombre + 'lanza al aro, ' + bloqueador.nombre + ' no logra interceptarla, y anota. Tres puntos para ' + equipoTirador.nombre)
        return

    def loggearInicioReboteo():
        print('La pelota queda rebotando y los jugadores se acercan a tratar de tomarla!')

    def loggearReboteoIntento(jugador, equipo):
        print jugador.nombre + ' del equipo ' + equipo.nombre + ', intenta agarrar el rebote.')
        return

    def loggearReboteoExito(jugador, equipo):
        print jugador.nombre + ' del equipo ' + equipo.nombre + ', logra agarrar el rebote!')
        return
