import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir)

from abc import ABCMeta, abstractmethod
from resolvedores import *

class Accion(object):
	__metaclass__ = ABCMeta

	@abstractmethod
	def jugadorEjecutante(self):
		pass

	@abstractmethod
	def resolvedorPara(self, unSimulador):
		pass

from bloqueo import *
from intercepcion import *
from pase import *
from tiro2puntos import *
from tiro3puntos import *
from rebote import *
