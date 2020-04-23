import math
import numpy as np
import time

def X(xi, xf, ak):
    return ((xi+xf)/2)+((xf-xi)/2)*ak

def xs_simples(s,a, b):
    return ((a+b)/2)+(((b-a)/2)*math.tanh(s))

def xs_dupla(s,a, b):
    return ((a+b)/2)+(((b-a)/2)*math.tanh((math.pi/2) * math.sinh(s)))

def exp_simples(s,a, b,f):
    return (f(xs_simples(s,a,b)))*(((b-a)/2)*(1/(math.cosh(s)**2)))

def exp_dupla(s,a, b,f):
    return (f(xs_dupla(s,a,b)))*(((b-a)/2)*((math.pi/2)*(math.cosh(s)/((math.cosh((math.pi/2)*math.sinh(s)))**2))))



def GaussL4(a, b,f,lim_inf,lim_sup,simples=True):
    w1 = (1/2)-(math.sqrt(5/6))/6
    w2 = (1/36)*(18+math.sqrt(30))
    c=-((3+2*(6/5)**(1/2))/7)**(1/2)
    d=-((3-2*(6/5)**(1/2))/7)**(1/2)
    e=((3-2*(6/5)**(1/2))/7)**(1/2)
    g=((3+2*(6/5)**(1/2))/7)**(1/2)
    
    if simples:
        return ((b-a)/2)*((exp_simples(X(a, b, c),lim_inf,lim_sup,f))*w1+(exp_simples(X(a, b, d),lim_inf,lim_sup,f))*w2+(exp_simples(X(a, b, e),lim_inf,lim_sup,f))*w2+(exp_simples(X(a, b, g),lim_inf,lim_sup,f))*w1)
    else: 
        return ((b-a)/2)*((exp_dupla(X(a, b, c),lim_inf,lim_sup,f))*w1+(exp_dupla(X(a, b, d),lim_inf,lim_sup,f))*w2+(exp_dupla(X(a, b, e),lim_inf,lim_sup,f))*w2+(exp_dupla(X(a, b, g),lim_inf,lim_sup,f))*w1)


def integrate(f,c,lim_inf,lim_sup):
    # grau do legendre = n integra polinômios f de grau até 2n -1

    '''
    Argumentos:
        f - funcao lambda ou normal
        grau - grau do polinomio de Legendre
        a e b - limites de integração
    '''

    tolerancia=10E-4
    intervalo = np.linspace(1,c,math.floor(c))
    aux_c=resultado_c=0
    for i in intervalo:
        print('c =',i)
        aux_c=resultado_c    
        resultado=0
        diferenca=1
        n=0
        a,b = -i,i                       #limites da integral numérica
        t0=time.time()
        while(diferenca>tolerancia):
            l=0
            aux=resultado
            resultado=0
            while(l<2**n):
                #resultado=resultado+GaussL4(a+(l*(b-a)/2**n), a+((l+1)*(b-a)/2**n),f,lim_inf,lim_sup)
                # Pra exponenciacao dupla, manda False no último parâmetro
                resultado=resultado+GaussL4(a+(l*(b-a)/2**n), a+((l+1)*(b-a)/2**n),f,lim_inf,lim_sup,False)
                l=l+1
                
            diferenca=abs(resultado-aux)
            n=n+1
            print('iteracao {} = {}'.format(n,resultado))
            if time.time() - t0 >= 300:
                print('Tempo limite atingido')
                break
        resultado_c = resultado
        print('Resultado=',resultado_c)
        print('Diferenca absoluta em relacao ao c anterior= {} \n'.format(abs(aux_c-resultado_c)))
        
    return resultado


f = lambda x: 1/((x**2)**(1/3))
#f = lambda x: 1/ (math.sqrt(4-x**2))
#f = lambda x: 1/(x**(1/2))
c=6
lim_inf,lim_sup=-1,1             #limites da integral original
#f = exp_simples(a,b,f)
resultado = integrate(f,c,lim_inf,lim_sup)











