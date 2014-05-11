#
# Esta biblioteca foi criada para solucionar o problema 
#	disponibilizado pela Prof. Aline para o trabalho de
#	Calculo Numerico/UFPel/2014-1
import sys, os, numpy
class Library:
	__matrix = None
	__log = None

	def __init__(self,log):
		self.__log = log
		self.__log.write('Class Init : Library\n')
		self.__matrix = None
	
	#
	# Metodo que verifica que a matriz 
	#	esta com a parte inferior zerada
	def isSolvable(self):
		self.__log.write('Preparing data in Library->isSolvable\n')
		j = 0
		aux = 1

		for i in range(len(self.__matrix)):
			while j < i:
				if self.__matrix.item(i,j) != 0.0:
					aux = 0
				j = j + 1
			if aux == 1:
				print 'val: '+str(self.__matrix.item(i,j))
				if self.__matrix.item(i,j) == 0.0:
					aux = -1
		return aux
	
	#
	# Procura o mair valor dentro da matriz
	def findTheBiggest(self):
		self.__log.write('Preparing data in Library->findTheBigest\n')
		bigest = 0
		bigestIndice = i

		while i < len(__matrix):
			if abs(__matrix.item((i,j))) > bigest:
				bigest = matrix.item((i,j))
				bigestIndice = i
			i += 1
		return bigestIndice

	#
	# le uma matriz de um arquivo, sendo ela separada por um
	#	um espaco e quadratica
	def readFile(self, path):
		self.__log.write('Preparing data in Library->readFile\n')
		
		try:
			arq = open(path)
			matrix = [[float(x) for x in line.split(' ')] for line in arq]
			self.setFromMatrix(matrix)
			self.__log.write(str(__matrix))
		except Exception, msg:
			self.__log.write('Error: '+str(msg))
			return None
		return 1

	#
	# Le uma matriz normal e a seta no formato do numPy
	def setFromMatrix(self, matrix):
		self.__matrix = numpy.matrix(matrix)
