import matplotlib.pyplot as plt

def PVI(h, v, k, m, delta):
    list_t=[]
    list_h=[]
    i=0
    list_t.append(0)
    list_h.append(h)
    critico=0                               # tempo da altura máxima
    
    while(list_h[i]>0):                     # enquanto não tiver chegado no mar
        i = i+1
        list_t.append(delta*i)
        list_h.append(list_h[i-1]+delta*v)          # y1 = y0 + delta*v0
        vant = v
        v = v+delta*(-10-(k/m)*v)
        
        if(vant*v<0):                           # Altura máxima
            critico = list_t[i-1]+delta/2
            hmax = list_h[i-1]+(delta/2)*v
            
    list_t.append(list_t[i-1]+delta/2)
    list_h.append(list_h[i-1]+(delta/2)*v)
    plt.plot(list_t,list_h)
    
    return v,list_t[i+1],critico,hmax,list_h[i+1]


if __name__ == "__main__":
    y0 = 200
    v0 = 5
    k = 0.25
    m = 2
    
    for i in range(1,5):
        dt = 10 ** (-i)
        print('--'*8+f' delta t = {dt} '+'--'*8+'\n')
        v,t,critico,hmax,valor=PVI(y0, v0, k, m, dt)
        print("Altura máxima da trajetória = ", hmax ,"metros")
        print("Tempo decorrido até a altura máxima = ",critico,"segundos")
        print("Tempo total até a queda no mar = ",t,"segundos")
        print("velocidade no momento do impacto com o mar = ",v,"m/s")











