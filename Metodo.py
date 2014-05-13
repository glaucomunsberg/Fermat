from Auxiliar import Auxiliar
from numpy.linalg import norm
from prettytable import *

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
              