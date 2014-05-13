from Auxiliar import Auxiliar

class MetodoExemplo:
	__matriz = None
	__log = None

	def __init__(self, log):
		self.__log = log
		self.__log.write('Class Init: Modelo\n')
	
	def preparaDados(self,matriz):
		#Executa
		self.__log.write('Preparing data in '+self.__class__.__name__+'\n')
		self.__matriz = matriz

	def executaMetodo(self):
		#Executa
		'Executed'
		
#Methods codes
#euler constant
euler = 2.71828

#return t in function of f
def f(t):
    return 70*pow(euler,(-1.5*t))+2.5*pow(euler,(-0.075*t))-9

#return the numbers signal
def signal(x):
    if x<0:
        return -1
    else:
        return +1

def bissecao():

    iterations = 1
    MAX_iterations = 20
    MIN_error = 0.00001

    a = 0.0
    b = 3.0
    c = 0.0
    print "Iteration\ta\t\tb\t\tc\t\tf(c)"
    while 1: # iterations ≤ MAX_iterations: # limit iterations to prevent infinite loop
        c = (a + b)/2 # new midpoint
        print iterations,"\t\t",a,"\t",b,"\t",c,"\t",f(c)
        if f(c) == 0 or ((b - a)/2) < MIN_error: # solution found
            break;
        iterations+=1 # increment step counter
        if signal(f(c)) == signal(f(a)):  # create  new interval
            a = c
        else:
            b = c

