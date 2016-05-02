import equipo
import random

from abc import ABCMeta, abstractmethod

class Accion(object):
	__metaclass__ = ABCMeta

	def __init__(self, modificador):

	@abstractmethod
	def umbralDeExito(self, unJugador):
		pass
