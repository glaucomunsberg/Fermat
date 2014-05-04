import sys, time, datetime, numpy
from MetodoExemplo import MetodoExemplo

if __name__ == "__main__":

    #Matrizes base
    matriz = numpy.matrix([[4,-1,0,-1,0,0,0],[-1,4,-1,0,-1,0],[0,-1,4,0,0,-1],[-1,0,0,4,-1,0],[0,-1,0,-1,4,-1],[0,0,-1,0,-1,4]])

    #Prepara o sistema de logs
    timeNow     = time.time()
    nomelog     = datetime.datetime.fromtimestamp(timeNow).strftime('%Y-%m-%d')
    horaSessao  = datetime.datetime.fromtimestamp(timeNow).strftime('%H:%M:%S')
    log = open(nomelog+'.log', 'a')
    log.write('\n\n====Sessao Inicio====\n')
    log.write('Hora: '+horaSessao+'\n')
    
    #Executa um exemplo de metodo
    metodo1 = MetodoExemplo(log)
    metodo1.preparaDados(matriz)
    metodo1.executaMetodo()

    #Manipulando Matrizes
    matriz.T
    print 'transposta\n'
    print matriz
    print 'size\n'
    print matriz.size