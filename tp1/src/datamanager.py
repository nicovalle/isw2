from abc import ABCMeta, abstractmethod

#"clase abstracta con la interfaz para los data manager, cuya responsabilida es obtener y actualizar los datos del sistema"
class DataManager(object):
	__metaclass__ = ABCMeta

	@abstractmethod
	def loginUser(self, unNombreDeUsuario, unPassword):
		pass

	@abstractmethod
	def registerUser(self, unNombreDeUsuario,  unaDireccionDeEmail, unPassword):
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
	def obtenerJugador(self, unNombre, unApellido):
		pass

	@abstractmethod
	def obtenerTecnico(self, unNombre, unApellido):
		pass

	@abstractmethod
	def actualizarTecnico(self, unTecnico):
		pass

	@abstractmethod
	def obtenerEquipo(self, unNombreDeEquipo, unNombreDeDueno):
		pass

	@abstractmethod
	def actualizarEquipo(self, unEquipo):
		pass

	@abstractmethod
	def obtenerLogSimulacion(self, unaSimulacion):
		pass

	@abstractmethod
	def guardarLogSimulacion(self, unaSimulacion):
		pass
