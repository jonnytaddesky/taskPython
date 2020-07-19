import numpy as np

def calc(x, m):
    result = 1
    for j in np.arange(m):
        result *= x
    return result    

def power():
    z = 0
    for x in np.arange(-1.1, 0.3, 0.2):
        for m in np.arange(1, 5, 1):
            z = calc(x, m)*calc(np.sin(x*m),m)
            print('Значение функции = {} При m = {}'.format(z, m)) 
        print('Вычислено при x = {}'.format(x))

power()