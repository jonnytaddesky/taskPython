# Напишите программу, которая позволяет пользователю 
# ввести в консоль три координаты вектора x, y, и z, 
# с основанием у начала координат. Вычислите длину 
# этого вектора и выведите её обратно в консоль.
import math

x = int(input('Введите X: '))
y = int(input('Введите Y: '))
z = int(input('Введите Z: '))

print('Вы ввели следующие числа: X = {}; Y = {}; Z = {}'.format(x,y,z))

len_vec = math.sqrt(x**2 + y**2 + z**2)

print(len_vec)