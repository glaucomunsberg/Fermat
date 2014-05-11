from Auxiliar import Auxiliar

class MetodoExemplo:
	__matriz = None
	__log = None

	def __init__(self, log):
		self.__log = log
		self.__log.write('Class Init: Modelo\n')
	
	def preparaDados(self,matriz):
		#Executa
		self.__log.write('Preparing data in '+self.__class__.__name__+'\n')
		self.__matriz = matriz

	def executaMetodo(self):
		#Executa
		'Executed'
