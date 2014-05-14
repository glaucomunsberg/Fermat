#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, time, datetime, os

from Metodo import *

if __name__ == "__main__":
    firstTime = False
    os.system('clear')
    
    optionMenu = False
    while(optionMenu == False):
        
        os.system('clear')
        print '=====================Fermat====================='
        print 'Option - Description'
        print '     1 - Solve reading the file problem'
        print '     2 - Solve the problem example'
        print '     3 - About'
        print '     0 - Exit' 
        print ''  
        option = -1

        while( option < 0  and option < 3):
            try:
                option = int(raw_input('Your Option: '))
            except Exception,msg:
                log.write('Principal: Error: '+str(msg))

        if option == 1:    
            try:
                print lib.readFile(raw_input('Type the path to your file: '))
            except Exception, msg:
                print 'Error: '+str(msg)
                exit(1)
        elif option == 2:
            matrix=[[4.0,-1.0,0.0,-1.0,0.0,0.0],[-1.0,4.0,-1.0,0.0,-1.0,0.0],[0.0,-1.0,4.0,0.0,0.0,-1.0],[-1.0,0.0,0.0,4.0,-1.0,0.0],[0.0,-1.0,0.0,-1.0,4.0,-1.0],[0.0,0.0,-1.0,0.0,-1.0,4.0]]
            
        elif option == 3:
            print 'Biblioteca desenvolvida para solucionaro o problema'
            print '     proposto na  Aula de Calculo Numerico. Para  saber'
            print '     mais sobre o trabalho, por favor, acesse Ava/UFPel'
            print ''
            print 'Integrantes:'
            print '     Glauco Roberto'
            print '     Guilherme Cousin'
            print '     Gustavo Lima'
        elif option == 0:
            print '=====================End====================='
            optionMenu = True
            exit()
        else:
            print 'Something is wrong. \n  \'Cause you type a wrong digit on you keyboard'
            exit()


        if option == 1 or option == 2:
            os.system('clear')
            print '================Metodos Possiveis==============='
            print ' Zero de Funcoes'
            print '     1  - Bisscao'
            print '     2  - Fixed Point'
            print '     3  - Posicao Falsa'
            print '     4  - Secante'
            print '     5  - Newton Raphson'
            print ''
            print ' Sistemas'
            print '     6  - Gauss-Jacobi'
            print '     7  - LRU'
            print '     8  - Cholesky'
            print '     9  - Gauss-Seidel'
            print '     10 - Eliminação Gaussiana'
            print ''
            print '     11 - All'
            print '     0  - Voltar'
            optionMetodo = int(raw_input('Your Option: '))
            
            if optionMetodo == 0:
                os.system('clear')
            elif optionMetodo == 1:
                bissecao()
            elif optionMetodo == 2:
                ponto_fixo()
            elif optionMetodo == 3:
                posicao_falsa()
            elif optionMetodo == 4:
                secante()
            elif optionMetodo == 5:
                newton_raphson()
            elif optionMetodo == 6:
                gauss_jacobi()
            elif optionMetodo == 7:
                lru()
            elif optionMetodo == 8:
                cholesky()
            elif optionMetodo == 9:
                gauss_seidel()
            elif optionMetodo == 11:
                bissecao()
                ponto_fixo()
                posicao_falsa()
                secante()
                newton_raphson()
                gauss()
                lru()
                cholesky()
                gauss_seidel()
                gauss_jacobi()
               
            else:
                print 'Something is wrong!'
        raw_input('Press Any key to continue')
