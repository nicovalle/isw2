class Logger(object):

    def loggearInicioTurno(self, numeroTurno):
        print('Se inicia el turno numero ' + str(numeroTurno))
        return

    def loggearInicioTiempoExtra(self):
        print('Empate. EMPIEZA EL TIEMPO EXTRA! Se jugaran 6 turnos mas.')
        return

    def loggearVictoria(self, equipoGanador, equipoPerdedor, puntajeGanador, puntajePerdedor):
        print('El equipo ' + equipoGanador.nombre() + ' vence al equipo ' + equipoPerdedor.nombre() + ' por ' + str(puntajeGanador) + ' tantos contra ' + str(puntajePerdedor))
        return

    def loggearInicioPosesion(self, equipoAtacante):
        print('La posesion es del equipo ' + equipoAtacante.nombre())
        return

    def loggearEleccionJugada(self, unEquipo, unaJugada):
        print('El equipo '+unEquipo.nombre()+' eligio la jugada '+unaJugada.nombre())
        return

    def loggearPelotaAfuera(self):
        print('La pelota sale de la cancha!')
        return

    def loggearPaseIntento(self, paseEmisor, paseReceptor):
        print(paseEmisor.nombreCompleto() + ' se la pasa a ' + paseReceptor.nombreCompleto())
        return

    def loggearPaseExitoso(self):
        print('El pase se realiza exitosamente, y la intercepcion falla')
        return

    def loggearIntercepcionIntento(self, paseInterceptor):
        print(paseInterceptor.nombreCompleto() + ' intenta interceptar el pase')
        return

    def loggearIntercepcionExitosa(self, paseInterceptor):
        print(paseInterceptor.nombreCompleto() + ' intercepta el pase exitosamente!')
        return

    def loggearPaseIntercepcionFallido(self):
        print('El pase fallo, y nadie logro interceptar la pelota.')
        return

    def loggearBloqueoIntento(self, tirador, bloqueador):
        print(bloqueador.nombreCompleto() + ' intenta bloquear la pelota')
        return

    def loggearBloqueoExitoso(self, bloqueador):
        print(bloqueador.nnombreCompletoombre() + ' bloquea el tiro de manera exitosa!')
        return

    def loggearDobleIntento(self, tirador):
        print(tirador.nombreCompleto() + 'lanza la pelota al aro por 2 puntos')
        return

    def loggearTripleIntento(self, tirador):
        print(tirador.nombreCompleto() + 'lanza la pelota al aro por 3 puntos')
        return

    def loggearEncestarDoble(self, equipoTirador):
        print('La pelota entra! 2 puntos para ' + equipoTirador.nombre())
        return

    def loggearEncestarTriple(self, equipoTirador):
        print('La pelota entra! 3 puntos para ' + equipoTirador.nombre())
        return

    def loggearTiroFallido(self):
        print('El tiro fue errado y nadie pudo bloquear la pelota')

    def loggearReboteoInicio(self):
        print('La pelota queda rebotando y los jugadores se acercan a tratar de tomarla!')

    def loggearReboteoIntento(self, jugador, equipo):
        print(jugador.nombre() + ' del equipo ' + equipo.nombre() + ', intenta agarrar el rebote.')
        return

    def loggearReboteoExito(self, jugador, equipo):
        print(jugador.nombre() + ' del equipo ' + equipo.nombre() + ', logra agarrar el rebote!')
        return
