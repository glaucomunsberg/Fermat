import sys, time, datetime
from MetodoExemplo import MetodoExemplo

if __name__ == "__main__":
	
	#Prepara o sistema de logs
	timeNow     = time.time()
	nomelog     = datetime.datetime.fromtimestamp(timeNow).strftime('%Y-%m-%d')
	horaSessao  = datetime.datetime.fromtimestamp(timeNow).strftime('%H:%M:%S')
    log = open(nomelog+'.log', 'a')
    log.write('\n\n====Sessão Início====\n')
    log.write('Hora: '+horaSessao+'\n')

    #Executa um exemplo de método
    metodo1 = MetodoExemplo(log)
    metodo1.preparaDados(matriz)
    metodo1.executaMetodo()