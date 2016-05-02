from abc import ABCMeta, abstractmethod

class Jugada(metaclass = ABCMeta):

	@abstractmethod
	def ejecutarCon(unEquipo):
		print("me ejecutaron")
		pass
