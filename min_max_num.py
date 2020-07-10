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
       