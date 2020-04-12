import math

def x(a, b, c):
    return ((a+b)/2)+((b-a)/2)*c

def GaussL2(a, b):
    c=-(1/3)**(1/2)
    d=(1/3)**(1/2)
    return ((b-a)/2)*(f(x(a, b, c))+f(x(a, b, d)))

def GaussL3(a, b):
    c=-(3/5)**(1/2)
    d=0
    e=(3/5)**(1/2)
    return ((b-a)/2)*((f(x(a, b, c))*((5)/(9)))+(f(x(a, b, d))*((8)/(9)))+(f(x(a, b, e))*((5)/(9))))

def GaussL4(a, b):
    c=-((3+2*(6/5)**(1/2))/7)**(1/2)
    d=-((3-2*(6/5)**(1/2))/7)**(1/2)
    e=((3-2*(6/5)**(1/2))/7)**(1/2)
    g=((3+2*(6/5)**(1/2))/7)**(1/2)
    return ((b-a)/2)*((f(x(a, b, c))*((1566598950940059)/(4503599627370496)))+(f(x(a, b, d))*((1468500338215219)/(2251799813685248)))+(f(x(a, b, e))*((5874001352860875)/(9007199254740992)))+(f(x(a, b, g))*((3133197901880117)/(9007199254740992))))


def integrate(f,points,a,b):
    '''
    Argumentos:
        f - normal or lambda function
        points - number of points  
        a e b - integration limits
    '''
    
    if not 2<=points<=4: 
        print('{} points not implemented'.format(degree))
        return 
    
    tolerance=10E-6
    result=0
    difference=1
    n=0
    
    while(difference>tolerance):
        l=0
        aux=result
        result=0
        while(l<2**n):
            if points == 2:
                result=result+GaussL2(a+(l*(b-a)/2**n), a+((l+1)*(b-a)/2**n))
            elif points ==3:
                result=result+GaussL3(a+(l*(b-a)/2**n), a+((l+1)*(b-a)/2**n))
            else:
                result=result+GaussL4(a+(l*(b-a)/2**n), a+((l+1)*(b-a)/2**n))
            l=l+1
            
        difference=abs(result-aux)
        n=n+1
        print('iteration {} = {}'.format(n,result))
        
    return result

if __name__ == '__main__':
    #f = lambda x: x**2
    #f = lambda x: 3*x + 7     
    f = lambda x: (math.sin(2*x) + 4*x**2 + 3*x)**2  
    points = int(input('Enter the number of points(2,3 or 4)\n'))
    a = int(input('Enter the a\n'))
    b = int(input('Enter the b\n'))
  
    result=integrate(f,points,a,b)
    print('\nresult =',result)
