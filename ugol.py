# Напишите программу , в которой по извесной начальной скорости 
# V и времени полета тела T определяется угол aльфа под которым 
# тело брошено по отношению к горизонту (воспользуйтесь соотношением a = arcsin(gT/2V) ). 
# Ниже показан вывод программы, которая у вас должна получиться:

import math

g = 9.8
v = float(input('V = '))
t = float(input('T = '))

a = math.asin((g*t)/(2*v))

alpha = (a*180)/math.pi

print('Ugol = {}'.format(alpha))