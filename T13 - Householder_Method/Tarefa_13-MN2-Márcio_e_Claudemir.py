import numpy as np
import scipy.linalg as sci
np.set_printoptions(precision=5,suppress=True)


def potencia_inverso(A):
    v = np.ones((A.shape[0],1))
    tolerancia = 1E-10
    
    LU,piv = sci.lu_factor(A)               #LU tem o U na parte superior e o L na inferior
    
    lambda_ = 0
    dif = 1

    while dif > tolerancia:
        lambda_velho=lambda_
        x1 = v / np.linalg.norm(v)
        v = sci.lu_solve((LU, piv), x1)
        lambda_ = x1.T.dot(v)
        dif = abs((lambda_-lambda_velho)/lambda_)

        #print('autovetor = \n ',x1)
        #print('autovalor = ',lambda_,'\n')
        
    lambda_ = 1/lambda_
    return x1,lambda_

def potencia_deslocamento(A,desloc):
    A = A - (desloc*np.eye(A.shape[0]))

    vetor,valor = potencia_inverso(A)
    valor += desloc
    
    return vetor,valor

def eigen(A):
    desloc = np.linspace(4,50,5)       #Deslocamentos pra matriz A da tarefa
    autovetores,autovalores = [],[]
    
    for p in desloc:
        #print('\nDeslocamento = ',p)
        vetor,valor=potencia_deslocamento(A,p)
        autovetores.append(vetor)
        autovalores.append(valor)
        #print('autovetor = \n',vetor)
        #print('autovalor = ',valor)

    return autovetores,autovalores    

def householder(A):
    n = A.shape[0]
    H = np.eye(n)
    A_ant = A
    
    for i in range(n-2):
        H_i = matriz_householder(A_ant, i)
        A = H_i.T.dot(A_ant).dot(H_i)
        A_ant = A
        H = H.dot(H_i)
        
    print('Matriz tridiagonal A_barra = \n',A,'\n')
    print("Matriz acumulada H de householder = \n",H,'\n')
    return A, H


def matriz_householder(A, i):
    n = A.shape[0]
    w,z = np.zeros(n),np.zeros(n)                  #w e w'
    
    
    w[i+1:n] = A[i+1:n,i]
    z[i+1] = np.linalg.norm(w) 
    N = w - z
    N /= np.linalg.norm(N)
    
    H = np.eye(n) - (2*np.outer(N,N))
    #print("Matriz de householder = ",H,'\n')
    return H



if __name__ == '__main__':
    A = np.array([[40, 8, 4, 2, 1], [8, 30, 12, 6, 2], [4, 12, 20, 1, 2], [2, 6, 1, 25, 4],[1, 2, 2, 4, 5]])
    n = A.shape[0]
    
    A_barra, H = householder(A)
    
    autovetores,autovalores = eigen(A_barra)
    autovetores = np.array([i.reshape(n) for i in autovetores])
    
    print('Autovetores e Autovalores de A_barra = \n')
    for i in range(n):
        print(autovetores[i],'---',autovalores[i])
    
    print('\n Autovetores e Autovalores de A = \n')
    autovetores_A = H.dot(autovetores.T)
    for i in range(n):
        print(autovetores_A[:,i],'---',autovalores[i])    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
