n = int(input('Введите число не больше 99: '))

x = n // 10
y = n % 10

maximum = max(x,y)
minimum = min(x,y)
print(maximum, '- большая цифра')
print(minimum, '- меньшая цифра')