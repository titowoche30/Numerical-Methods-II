import numpy as np

def f(S, k, m):
    return np.array([S[1], -10-(k/m)*S[1]])

def RugenKutta(h, v, k, m, delta):
    list_t=[]
    S=[]
    S.append([h,v])
    list_t.append(0)
    i=0
    critico=0
    hmax=0
    
    while(S[i][0]>0):
        i=i+1
        list_t.append(delta*i)
        aux1=S[i-1]+(delta/2)*f(S[i-1], k, m)
        aux2=S[i-1] + delta*(-f(S[i-1],k,m) + 2*f(aux1,k,m))
        S.append(S[i-1]+(delta/6)*(f(S[i-1],k,m)+4*f(aux1,k,m)+f(aux2,k,m)))
        
        if(S[i-1][1]*S[i][1]<0):
            critico=list_t[i-1]+delta/2
            aux1=S[i-1]+(delta/4)*f(S[i-1], k, m)
            aux2=S[i-1]+(delta/2)*(-f(S[i-1],k,m)+2*f(aux1,k,m))
            hmax=(S[i-1]+(delta/12)*(f(S[i-1],k,m)+4*f(aux1,k,m)+f(aux2,k,m)))[0]
            
    list_t.append(list_t[i-1]+delta/2)
    aux1=S[i-1]+(delta/4)*f(S[i-1], k, m)
    aux2=S[i-1]+(delta/2)*(-f(S[i-1],k,m)+2*f(aux1,k,m))
    S.append((S[i-1]+(delta/12)*(f(S[i-1],k,m)+4*f(aux1,k,m)+f(aux2,k,m))))
    
    return S[i+1],critico,hmax,list_t[i+1]


if __name__ == "__main__":
    y0 = 200
    v0 = 5
    k = 0.25
    m = 2
    
    for i in range(1,5):
        dt = 10 ** (-i)
        print('--'*8+f' delta t = {dt} '+'--'*8+'\n')
        S,critico,hmax,t=RugenKutta(y0, v0, k, m, dt)
        print("Altura máxima da trajetória = ", hmax ,"metros")
        print("Tempo decorrido até a altura máxima = ",critico,"segundos")
        print("Tempo total até a queda no mar = ",t,"segundos")
        print("velocidade no momento do impacto com o mar = ",S[1],"m/s")