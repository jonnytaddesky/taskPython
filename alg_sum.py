import math

x_quantity = int(input('Введите колличество иксов: '))
y = 0

for i in range(x_quantity):
    print('Введите значения Z, B, A, Betta для X{}:'.format(i+1))
    z = float(input('Z = '))
    b = float(input('B = '))
    a = float(input('A = '))
    betta = float(input('Betta = '))
    x = z**3 - b + a**2 / math.tan(betta)**2
    y += x

print('Y = {}'.format(y))
