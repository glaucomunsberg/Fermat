class ModeloExemplo:
	__matriz = None
	__log = None

	def __init__(self, log):
		self.__log = log
		self.__log.write('Classe: ModeloExemplo \n')
	
	def preparaDados(self,matriz):
		#Executa
		self.__log.write('Preparando dados em')
		self.__matriz = matriz

	def executaMetodo(self):
		#Executa
		'executou'
