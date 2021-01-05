import numpy as np
from scipy import integrate
np.set_printoptions(precision=5,suppress=True)

def elem_finitos(N, dx):
    phi = [lambda s: (1-s)/2 , lambda s: (1+s)/2]
    phi_linha = [1/4,-1/4,1/4]                                             #[phi[0]'**2,phi[0]'*phi[1]',phi[1]'**2]
    
    
    f = lambda dx: lambda s: ((1-s)/2)**2 * dx/2
    phi_product1 = f(dx)
    g = lambda dx: lambda s: (1/4) * (1-s) * (s+1) * dx/2                   
    phi_product2 = g(dx)
    h = lambda dx: lambda s: ((1+s)/2)**2 * dx/2
    phi_product3 = h(dx)
    phi_list = [phi_product1,phi_product2,phi_product3]                     #[phi[0]**2,phi[0]*phi[1],phi[1]**2]
    
    A_aux = []
    
    aux = -1
    for k in range(N+1):
        A_aux.append(np.zeros((2,2)))
        for i in range(2):
            for j in range(i,2):
                aux+=1
                
                part1 = integrate.quad(lambda x: phi_linha[aux] * 2/dx ,a = -1,b = 1)[0]
                part2 = integrate.quad(phi_list[aux],a = -1,b = 1)[0]
                A_aux[k][i,j] = part1 + part2
                A_aux[k][j, i] = A_aux[k][i, j]
                
                if aux == 2: aux = -1
                
        
    A = np.zeros((N+2, N+2))
    for k in range(N):
        for i in range(2):
            for j in range(2):
                A[k + i, k + j] += A_aux[k][i, j]

    A = A[1:-2, 1:-2]
    
    b = np.zeros(N-1)
    b[-1] = -A[-2, -1]

    y = np.linalg.solve(A,b)
    return A, b, y


def relative_error(y_approx,y):
    return abs(y_approx - y) / y

if __name__ == '__main__':
    N = 8
    x = np.linspace(0,1,N+1)
    dx = x[1]-x[0]

    A, b, y = elem_finitos(N,dx)
    print(f"\n A = {A} \n")
    print(f"b = {b} \n")

    F = lambda x: (1/(np.exp(-1)-np.exp(1))) * (np.exp(-x) - np.exp(x))     #Sol. exata
    y_exato = np.array([F(i) for i in x[1:-1]])
    errors = np.array([relative_error(y[i],y_exato[i]) for i in range(len(y_exato))])
    print(f"Meus y = {y} \n\ny exatos = {y_exato}\n\n")
    print(f"Erros relativos sem o 0 e o 1 = {errors}\n\n")
    