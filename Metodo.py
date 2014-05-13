from Auxiliar import Auxiliar
from numpy.linalg import norm

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
			
def posicao_falsa():
        #   s,t: endpoints of an interval where we search
        #   e: half of upper bound for relative error
        #   m: maximal number of iterations
        
        r = 0.0
        fr = 0.0
        n = 1
        m = 20
        e = 0.000005
        s = 0
        t = 5
        side=0
        
        # starting values at endpoints of interval
        fs = f(s);
        ft = f(t);
        
        while n < m:
            r = (fs*t - ft*s) / (fs - ft)
            if (abs(t-s) < e*abs(t+s)):
                break
            fr = f(r)
            
            print r
            
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

#need to be teste with extreme urgency
def ponto_fixo():
    x0 = 0.0
    tol=10e-5
    maxiter=100
    e = 1
    itr = 0
    while(e > tol and itr < maxiter):
        x = f(x0)      # fixed point equation
        e = norm(x0-x) # error at the current step
        x0 = x
		print x
        itr = itr + 1
		
def newton_raphson():
    #These choices depend on the problem being solved
    x0 = 1                      #The initial value
    tolerance = 0.0000001       #7 digit accuracy is desired
    epsilon = 10^(-14)          #Don't want to divide by a number smaller than this
    
    while 1:
        y = f(x0)
        yprime = df(x0)
     
        if(abs(yprime) < epsilon):                        #Don't want to divide by a number too small
            print "WARNING: denominator is too small"
            break                                         #Leave the loop
    
        x1 = x0 - y/yprime                                #Do Newton's computation
        
        print x1
        
        if(abs(x1 - x0)/abs(x1) < tolerance):             #If the result is within the desired tolerance
            break;                                        #Done, so leave the loop
     
        x0 = x1                                           #Update x0 to start the process again                  