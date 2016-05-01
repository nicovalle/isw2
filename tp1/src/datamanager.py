from abc import ABCMeta, abstractmethod

"clase abstracta con la interfaz para los data manager, cuya responsabilida es obtener y actualizar los datos del sistema"
class DataManager(metaclass = ABCMeta):
	"__metaclass__ = ABCMeta"

	@abstractmethod
	def loginUser(self, unEmail, unPassword):
		pass

	@abstractmethod
	def registerUser(self, unEmail, unPassword):
		pass

	@abstractmethod
	def actualizarParticipante(self, unParticipante):
		pass

	@abstractmethod
	def actualizarTablaDeResultados(self, unaTablaDeResultados):
		pass

	@abstractmethod
	def obtenerTablaDeResultados(self):
		pass	
			
	@abstractmethod
	def actualizarParticipante(self, unParticipante):
		pass

	@abstractmethod
	def actualizarJugador(self, unJugador):
		pass
		
	@abstractmethod
	def obtenerJugador(self):
		pass
	
	@abstractmethod
	def obtenerTecnico(self):
		pass

	@abstractmethod
	def actualizarTecnico(self, unTecnico):
		pass

	@abstractmethod
	def obtenerJugada(self, unaJugada):

	@abstractmethod
	def actualizarJugada(self, unaJugada):
		pass

	@abstractmethod
	def obtenerLogSimulacion(self, unaSimulacion):
		pass

	@abstractmethod
	def guardarLogSimulacion(self, unaSimulacion):
		pass
		