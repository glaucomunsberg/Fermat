import sys, os
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
	def isSolvable(self,matrix):
		self.__log.write('Preparing data in Library->isSolvable\n')
		j = 0
		aux = 1

		for i in range(len(mat)):
			while j < i:
				if mat[i][j] != 0.0:
					aux = 0
				j = j + 1
			if aux == 1:
				if mat[i][j] == 0.0:
					aux = -1
		return aux
	
	#
	# Procura o mair valor dentro da matriz
	def findTheBiggest(self, matrix):
		self.__log.write('Preparing data in Library->findTheBigest\n')
		bigest = 0
		bigestIndice = i

		while i < len(mat):
			if abs(mat[i][j]) > bigest:
				bigest = matrix[i][j]
				bigestIndice = i
			i += 1
		return bigestIndice

	#
	# le uma matriz de um arquivo, sendo ela separada por um
	#	um espaco e quadratica
	def readFile(self, path):
		self.__log.write('Preparing data in Library->readFile\n')
		arq = open('exemplo.txt')
		return [[float(x) for x in line.split()] for line in arq]
