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
        log.write('\n\n=====================Session Inition=====================n')
        log.write('Hora: '+horaSessao+'\n')
        log.write('System Libraries OK\n')
        log.write('System Log OK\n')
    except Exception, msg:
        print 'Error: '+str(msg)

    optionMenu = False
    while(optionMenu == False):
        
        os.system('clear')
        print '=====================Fermat====================='
        print 'Option - Description'
        print '     1 - Read the file and solve the problem'
        print '     2 - Solve the problem example'
        print '     3 - About'
        print '     0 - Exit' 
        print ''  
        option = 10

        while( option !=  1 and option != 2 and option != 0 and option != 3):
            try:
                option = int(raw_input('Your Option: '))
            except Exception,msg:
                log.write('Principal: Error: '+str(msg))

        lib = Library(log)
        
        if option == 1:    
            try:
                print lib.readFile(raw_input('Type the path to your file: '))
            except Exception, msg:
                log.write('Error: '+str(msg)+'\n')
                print 'Error: '+str(msg)
                exit(1)
        elif option == 2:
            lib.setFromMatrix([[4,-1,0,-1,0,0,0],[-1,4,-1,0,-1,0],[0,-1,4,0,0,-1],[-1,0,0,4,-1,0],[0,-1,0,-1,4,-1],[0,0,-1,0,-1,4]])
            
        elif option == 3:
            print 'Biblioteca desenvolvida para solucionaro o problema'
            print ' proposto na  Aula de Calculo Numerico. Para  saber'
            print ' mais sobre o trabalho, por favor, acesse Ava/UFPel'
            print ''
            print 'Integrantes:'
            print ' Glauco Roberto'
            print ' Guilherme Cousin'
            print ' Gustavo Lima'
        elif option == 0:
            print '=====================End====================='
            optionMenu = True
            exit()
        else:
            print 'Something is wrong. \n  \'Cause you type a wrong digit on you keyboard'
            exit()

        log.flush()
        if option == 1 or option == 2:
            lib.isSolvable()
        raw_input('Press Any key to continue')