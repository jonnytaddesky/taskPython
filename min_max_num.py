# Организовать ввод двухзначного натурального числа с клавиатуры. 
# Программа должна определить наименьшую и наибольшую цифры, 
# которые входят в состав данного натурального числа.

while True:
    n = int(input('Введите число не больше 99: '))
    if n <= 99:
        x = n // 10
        y = n % 10
        maximum = max(x,y)
        minimum = min(x,y)
        print(maximum, '- большая цифра')
        print(minimum, '- меньшая цифра')
        break
    else:
        print('Следуйте правилам!')
        continue
       