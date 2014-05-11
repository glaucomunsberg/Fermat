import sys, time, datetime, numpy, os

from Library import Library
from Metodo import MetodoExemplo

if __name__ == "__main__":
    firstTime = False
    os.system('clear')
    try:
        #Prepara o sistema de logs
        timeNow     = time.time()
        nomelog     = datetime.datetime.fromtimestamp(timeNow).strftime('%Y-%m-%d')
        horaSessao  = datetime.datetime.fromtimestamp(timeNow).strftime('%H:%M:%S')
        log = open('logs/'+nomelog+'.log', 'a')
        log.write('\n\n================Session Inition================\n')
        log.write('Hora: '+horaSessao+'\n')
        log.write('System Libraries OK\n')
        log.write('System Log OK\n')
    except Exception, msg:
        print 'Error: '+str(msg)

    optionMenu = False
    while(optionMenu == False):
        os.system('clear')
        print '================Fermat================'
        print 'Option - Description'
        print '     1 - Read the file and solve the problem'
        print '     2 - Solve the problem example'
        print '     0 - Exit'   
        option = 10

        while( option !=  1 and option != 2 and option != 0):
            try:
                option = int(raw_input())
            except Exception,msg:
                log.write('Principal: Error: '+str(msg))

        if option == 1:
            lib = Library(log)
            try:
                print lib.readFile(None)
            except Exception, msg:
                log.write('Error: '+str(msg)+'\n')
                print 'Error: '+str(msg)
                exit(1)
        elif option == 2:
            matriz = numpy.matrix([[4,-1,0,-1,0,0,0],[-1,4,-1,0,-1,0],[0,-1,4,0,0,-1],[-1,0,0,4,-1,0],[0,-1,0,-1,4,-1],[0,0,-1,0,-1,4]])
            metodo1 = MetodoExemplo(log)
            metodo1.preparaDados(matriz)
            metodo1.executaMetodo()

            #Manipulando Matrizes
            matriz.T
            print 'transposta\n'
            print matriz
            print 'size\n'
            print matriz.size
        elif option == 0:
            print '================End================'
            optionMenu = True
            exit()
        else:
            print 'Something is wrong. \n  \'Couse you type a wrong digit on you keyboard'
            exit()
        raw_input('Press Any key to continue')