#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from Auxiliar import Auxiliar
import numpy
from numpy import *
import scipy 
from scipy import *
from prettytable import *
from numpy import *
from scipy.linalg import *
from numpy.testing import *

#Methods codes
#euler constant
euler = 2.718281828459

#return t in function of f
def f(t):
    return 70*pow(euler,(-1.5*t))+2.5*pow(euler,(-0.075*t))-9

#return t in function of the derivative function of f
def df(t):
    return -105*pow(euler,(-1.5*t)) - 0.1875*pow(euler,(-0.075*t))
	
#return the numbers signal
def signal(x):
    if x<0:
        return -1
    else:
        return +1

def bissecao():
    print 'Bissecao'
    iterations = 1
    MIN_error = 0.00001

    a = 0.0
    b = 3.0
    c = 0.0
    x = PrettyTable()
    x.field_names = ['Interation','a','b','c', 'f(c)']

    while 1: # iterations <=MAX_iterations: # limit iterations to prevent infinite loop
        c = (a + b)/2 # new midpoint
        x.add_row([iterations,a,b,c, f(c)])
        if f(c) == 0 or ((b - a)/2) < MIN_error: # solution found
            break;
        iterations+=1 # increment step counter
        if signal(f(c)) == signal(f(a)):  # create  new interval
            a = c
        else:
            b = c
    print x
			
def posicao_falsa():
        #   s,t: endpoints of an interval where we search
        #   e: half of upper bound for relative error
        #   m: maximal number of iterations
        
        print 'Posicao Falsa'
        r = 0.0
        fr = 0.0
        n = 1
        m = 20
        e = 0.000005
        s = 0.0
        t = 5.0
        side=0
        
        # starting values at endpoints of interval
        fs = f(s);
        ft = f(t);
        
        table = PrettyTable()
        table.field_names = ['Interations','Interval Inferior (s)','Interval Superior(t)', 'resposta (r)' ,'f(s)','f(t)','f(r)','error']

        while 1:
            r = (fs*t - ft*s) / (fs - ft)
            if (abs(t-s) < e*abs(t+s)):
                break
            fr = f(r)
            
            table.add_row([n,s,t,r,fs,ft,fr,abs(t-s)])
            
            if (fr * ft > 0):
                #  fr and ft have same sign, copy r to t
                t = r; ft = fr
                if (side==-1):
                 fs /= 2
                side = -1
            else:
                if (fs * fr > 0):
                    # fr and fs have same sign, copy r to s
                    s = r;  fs = fr
                    if (side==+1):
                        ft /= 2
                    side = +1
                else:
                     # fr * f_ very small (looks like zero)
                     break
            n+=1
        print table

#need to be teste with extreme urgency
def ponto_fixo():
    print 'Ponto Fixo'
    x0 = 0.0
    tol=0.00001
    maxiter=100
    e = 1.0
    itr = 0
    table = PrettyTable()
    table.field_names = ['iterations','x','Error']
    while(e > tol and itr < maxiter):
        x = x0-(f(x0)/df(x0))     # fixed point equation
        e = norm(x0-x) # error at the current step
        x0 = x
        table.add_row([itr,x,e])
        itr = itr + 1
    print table
		
def newton_raphson():
    print 'Newton Raphson'
    #These choices depend on the problem being solved
    x0 = 1                      #The initial value
    tolerance = 0.0000001       #7 digit accuracy is desired
    epsilon = 10^(-14)          #Don't want to divide by a number smaller than this
    table = PrettyTable()
    table.field_names = ['Interations', 'Error', 'F(x n)','F(x n+1)']
    interation=0
    
    while 1:
        y = f(x0)
        yprime = df(x0)
     
        if(abs(yprime) < epsilon):                        #Don't want to divide by a number too small
            print "WARNING: denominator is too small"
            break                                         #Leave the loop
    
        x1 = x0 - y/yprime                                #Do Newton's computation
        
        table.add_row([interation,abs(x1-x0),x0, x1])
        
        if(abs(x1 - x0)/abs(x1) < tolerance):             #If the result is within the desired tolerance
            break;                                        #Done, so leave the loop
        x0 = x1                                           #Update x0 to start the process again  
        interation+=1  
	
    print table

def secante():
    print 'Scante'
    table = PrettyTable()
    table.field_names = ['Interations','Answer','Error']
    x0=0.0;
    x1=1.0;
    interation=0
    tolerance = 0.0000001
    while ((x1-x0) > tolerance):
        x2 = x1 - (f(x1))*((x1 - x0)/(f(x1) - f(x0)))
        table.add_row([interation,x2,(x1-x0)])
        x0 = x1
        x1 = x2
        interation+=1
    print table

def lru():
    print 'LRU'
    A = array([[4,-1,0,-1,0,0],[-1,4,-1,0,1,0],[0,-1,4,0,0,-1],[-1,0,0,4,-1,0],[0,-1,0,-1,4,-1],[0,0,-1,0,-1,4]])
    B = array([[100],[0],[0],[100],[0],[0]])
    #A =  array([[3.0,2,4],[1,1,2],[4,3,2]])
    #B= array([[1],[2],[3]])
    #print det(A)
    P, L, U = lu(A)
    print L
    print U
    x1 = solve(A,B)
    LUA= lu_factor(A)
    print LUA
    x2 = lu_solve(LUA,B)
    print x2

def cholesky():
    A= array([[4,-1,0,-1,0,0],[-1,4,-1,0,1,0],[0,-1,4,0,0,-1],[-1,0,0,4,-1,0],[0,-1,0,-1,4,-1],[0,0,-1,0,-1,4]])
    L = scipy.linalg.cholesky(A, lower=True)
    U = scipy.linalg.cholesky(A, lower=False)

    B = scipy.array([[100],[0],[0],[100],[0],[0]])
    f = cho_factor(A)
    print f
    print "A:"
    print A

    print "L:"
    print L

    print "U:"
    print U
    S=cho_solve((f),B)
    print S

def gauss():
    print 'GAUSS not implemented yet'

def printM(m):                                 ##printM() imprime uma matriz na tela
  """Imprime a matriz"""
  for j in m:
    for elem in j:
      print "%3f" % elem,
    print ""
  print ""
 
##### Inicio da funcao que aplica os metodos  ######
 
def gauss_jacobi():
  mat = [1.0, -1.0/4.0, 0.0, -1.0/4.0, 0.0, 0.0, 25.0], [0.0, 1.0, -4.0/15.0, -1.0/15.0, -4.0/-15.0, 0.0, 20.0/3.0], [0.0, 0.0, 1.0, -1.0/56.0, -1.0/14.0, -15/56, 25.0/14.0], [0.0, 0.0, 0.0, 1.0, -60.0/209.0, -1.0/209.0, 7100.0/209.0],[0.0, 0.0, 0.0, 0.0, 1.0, -225.0/712.0, 2275.0/178.0],[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 100.0/21.0]
  MaX = 500
  ErroR = 0.0000001
  COLUNAS = 0
  numIT = 1                  
  switchh = False  
 
##### Aplica o metodo Gauss-Jacobi ######
 
  LINHAS = len(mat)                              ## numero de linhas
  for C in mat[0]:
    COLUNAS += 1                                 ## numero de colunas
 
  print ">> Dimensao da Matriz: [%d][%d]\n" %(LINHAS, COLUNAS)  ## Imprime numero de Linhas X Colunas
 
  ###### Primeira iteracao ######
  B = list(zip(*mat)[-1])                        ## B[] Vetor que guarda a ultima coluna da matriz
  X0 = [B[i]/mat[i][i] for i in xrange(LINHAS)]  ## Guarda o result de X[i]= b1/a11 , X[i]=b2/a22 etc..
  X1 = list(X0)                                  ## X1(atual) = X0(anterior)
 
  ###### Segunda iteracao em diante.. ######
  numIT += 1                  
  while not switchh:
    sup = 0
    div = 0
 
    for i in xrange(LINHAS):
      X1[i] = B[i]
      for j in xrange(COLUNAS-1):
        if ( i != j):
          X1[i]=  (X1[i] - (mat[i][j] * X0[j]))
      X1[i] =  (1/mat[i][i] * X1[i])
      aux = X1[i] - X0[i]
      if (aux < 0) :
        aux = aux * -1
      aux2 = X1[i]
      if (aux2 < 0):
        aux2 = aux2 * -1
      if (aux > sup):
        sup = aux
      if (aux2 > div):
        div = aux2
    X0 = list(X1)
    if (sup / div) <= ErroR:
      switchh = True
      numIT += 1
    if int(numIT) > int(MaX):
      print ">> **Impossivel** encontrar resultado em %s *iteracoes*.\n" % MaX  
      return
  
  printM(mat)                                      ## Imprime MAT
  my_cont = 0
  print "*** GauSS-JaCoBi ***"
  for i in X0:                                     ## Imprime  X, resultados de gauss-jacobi
    print "X%d = %f" % ((my_cont+1), i)
    my_cont += 1
  print "\n>> Numero de iteracoes: %d " % numIT
  print ">> Valor do erro: %s" % ErroR
 
####### Fim do Gauss-Jacobi #########
 
####### Inicio da Regrecao  #########
 
  print "\n\n*** Regressao/Eliminação ***"
 
  for a in xrange(1, LINHAS):                      ## Checar a a triangular inferior esta zerada,
    for b in xrange(0, COLUNAS):                 ## se nao estiver nao calcula regressao/elim
      if (int(a) != int(b)):
        if (int(mat[a][b]) != 0):
          print ">> **Impossivel** calcular com triangular inferior *diferente de 0*\n"
          return
      elif (int(a) == int(b)):
          break
         
  switchh = False
  i = LINHAS-1
  j = i
  B[j] = B[j] / mat[i][j]
  i -= 1
  j = i
  t = 0
  numIT = 1
  COLUNAS -= 1
 
  while not (switchh):
    div = 0
    numIT += 1
    for t in xrange(j+1, COLUNAS):
      div = div + (mat[i][t] * B[t])
    B[j] = (B[j] - div) / mat[i][j]
    if int(i) == 0:
      switchh = True
    i -= 1
    j = i
 
  my_cont = 0
  for i in B:                                 ## Imprime B, vetor que guarda resultados da regressao/elim
    print "B%d = %f" % ((my_cont+1), i)
    my_cont += 1
 
 
####### Fim da Regressao #########
              
