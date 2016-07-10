from abc import ABCMeta, abstractmethod

class Accion(object):
	__metaclass__ = ABCMeta

	@abstractmethod
	def jugadorEjecutante(self, unJugador):
		pass

from bloqueo import *
from intercepcion import *
from pase import *
from tiro2puntos import *
from tiro3puntos import *
