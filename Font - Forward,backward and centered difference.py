import numpy as np


def forward_difference(f,x,h,true_value):
    results = np.array((f(x+h) - f(x)) / h)
    errors = results - true_value
    ratio_errors = errors[0:len(errors)-1] / errors[1: len(errors)]
    
    return results,errors,ratio_errors

def backward_difference(f,x,h,true_value):
    results = np.array((f(x) - f(x - h)) / h)
    errors = results - true_value
    ratio_errors = errors[0:len(errors)-1] / errors[1: len(errors)]
    
    return results,errors,ratio_errors

def centered_difference(f,x,h,true_value):
    results = np.array((f(x + h) - f(x - h)) / (2*h))
    errors = results - true_value
    ratio_errors = errors[0:len(errors)-1] / errors[1: len(errors)]
    
    return results,errors,ratio_errors


def exemplo1():
    f = lambda x: np.exp(np.sin(x))
    x = 0
    h = 1/2 ** np.arange(1,11) 
    true_value = 1
    
    print('h =',h,'\n\n')
    return f,x,h,true_value


def exemplo2():
    f = lambda x: np.sin(x)
    x = 1
    h = 1/2 ** np.arange(1,11) 
    true_value = np.cos(1)
    
    print('h =',h,'\n\n')
    return f,x,h,true_value

def exemplo3():
    f = lambda x: 1 / (1+ np.exp(-x))
    x = 1
    h = 1/2 ** np.arange(1,11) 
    true_value = 0.1966
    
    print('h =',h,'\n\n')
    return f,x,h,true_value


print('----------Exemplo 1: f(x) = exp(sen(x)) ; x = 0----------\n')
f,x,h,true_value = exemplo1()

results_f,errors_f,ratio_errors_f=forward_difference(f,x,h,true_value)
results_b,errors_b,ratio_errors_b=backward_difference(f,x,h,true_value)
results_c,errors_c,ratio_errors_c=centered_difference(f,x,h,true_value)


print('Resultados:\n\nForward: {} \n\nBackward: {} \n\nCentered: {} \n\nValor real={} \n\n'.format(results_f,results_b,results_c,true_value))
print('Erros:\n\nForward: {} \n\nBackward: {} \n\nCentered: {} \n\n'.format(errors_f,errors_b,errors_c))
print('Razão entre erro i e erro i+1:\n\nForward: {} \n\nBackward: {} \n\nCentered: {} \n\n'.format(ratio_errors_f,ratio_errors_b,ratio_errors_c))


print('----------Exemplo 2: f(x) = sen(x) ; x = 1----------\n')
f,x,h,true_value = exemplo2()

results_f,errors_f,ratio_errors_f=forward_difference(f,x,h,true_value)
results_b,errors_b,ratio_errors_b=backward_difference(f,x,h,true_value)
results_c,errors_c,ratio_errors_c=centered_difference(f,x,h,true_value)

print('Resultados:\n\nForward: {} \n\nBackward: {} \n\nCentered: {} \n\nValor real={} \n\n'.format(results_f,results_b,results_c,true_value))
print('Erros:\n\nForward: {} \n\nBackward: {} \n\nCentered: {} \n\n'.format(errors_f,errors_b,errors_c))
print('Razão entre erro i e erro i+1:\n\nForward: {} \n\nBackward: {} \n\nCentered: {} \n\n'.format(ratio_errors_f,ratio_errors_b,ratio_errors_c))


print('----------Exemplo 3: f(x) = 1 / (1+ exp(-x)) ; x = 1----------\n')
f,x,h,true_value = exemplo3()

results_f,errors_f,ratio_errors_f=forward_difference(f,x,h,true_value)
results_b,errors_b,ratio_errors_b=backward_difference(f,x,h,true_value)
results_c,errors_c,ratio_errors_c=centered_difference(f,x,h,true_value)

print('Resultados:\n\nForward: {} \n\nBackward: {} \n\nCentered: {} \n\nValor real={} \n\n'.format(results_f,results_b,results_c,true_value))
print('Erros:\n\nForward: {} \n\nBackward: {} \n\nCentered: {} \n\n'.format(errors_f,errors_b,errors_c))
print('Razão entre erro i e erro i+1:\n\nForward: {} \n\nBackward: {} \n\nCentered: {} \n\n'.format(ratio_errors_f,ratio_errors_b,ratio_errors_c))

