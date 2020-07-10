import math

g = 9.8
v = float(input('V = '))
t = float(input('T = '))

a = math.asin((g*t)/(2*v))

alpha = (a*180)/math.pi

print('Ugol = {}'.format(alpha))