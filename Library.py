#
# Esta biblioteca foi criada para solucionar o problema 
#	disponibilizado pela Prof. Aline para o trabalho de
#	Calculo Numerico/UFPel/2014-1
import sys, os
from math import sqrt
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
		av = 1
		for i in range(len(self.__matrix)):
			print 'Position:'+str(i)+','+str(j)
			while j < i:
				if self.__matrix[i][j] != 0.0:
					av = 0
	    		j = j + 1
	    	if av == 1:
				if self.__matrix[i][j] == 0.0:
					av = -1
		return av

	#
	# Procura o mair valor dentro da matriz
	def findTheBiggest(self):
		self.__log.write('Preparing data in Library->findTheBigest\n')
		bigest = 0.0
		j = 0
		i = 0
		bigestIndice = i

		while(j < sqrt(self.__matrix.size)):
			while i < self.__matrix.size:
				if self.__matrix[i][j] > bigest:
					print 'value '+str(self.__matrix[i][j])
					bigest = self.__matrix[i][j]
					bigestIndice = i
				i += 1
			j += 1
		return bigest

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
		self.__log.write('Setting the Matrix: '+str(matrix) )
		self.__matrix = matrix
