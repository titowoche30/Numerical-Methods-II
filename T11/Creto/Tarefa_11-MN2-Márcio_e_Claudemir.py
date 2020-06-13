import numpy as np

def potencia_regular(A):
    v = np.ones((A.shape[0],1))
    tolerancia = 1E-10

    lambda_ = 0
    dif = 1

    while dif > tolerancia:
        lambda_velho=lambda_
        x1 = v / np.linalg.norm(v)
        v = A.dot(x1)
        lambda_ = x1.T.dot(v)
        dif = abs((lambda_-lambda_velho)/lambda_)

        #print('autovetor = \n ',x1)
        #print('autovalor = ',lambda_,'\n')

    return x1,lambda_


if __name__ == '__main__':
    A1 = np.array([[40,8,4,2,1],[8,30,12,6,2],[4,12,20,1,2],[2,6,1,25,4],[1,2,2,4,5]])
    A2 = np.array([[5,2,1],[2,3,1],[1,1,2]])
    A = (A1,A2)

    print('Matriz [0]: \n\n',A[0],'\n')
    print('Matriz [1]: \n\n',A[1],'\n')

    digit = int(input('Escolha uma das matrizes\n'))

    if not 0<=digit<=1: 
        print('Dígito inválido') 
        exit(0)
        
    vetor,valor = potencia_regular(A[digit])

    print('\nautovetor do autovalor dominante = \n',vetor)
    print('autovalor dominante = ',valor)
