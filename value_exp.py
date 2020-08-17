import numpy as np

PI = 3.141592

x = int(input('Введите значение x: '))
y = int(input('Введите значение y: '))

x = x * PI / 180
y = y * PI / 180

result = round((1 - np.tan(x))**(1/np.tan(x)) + np.cos(x - y), 2)

print('Ответ = {}'.format(result))