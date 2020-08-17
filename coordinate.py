X = int(input('Введите координату X: '))
Y = int(input('Введите координату Y: '))

if X > 0 and Y > 0:
    print('I четверть плоскости')
elif X > 0 and Y < 0:
    print('IV четверть плоскости')
elif X < 0 and Y > 0:
    print('II четверть плоскости')
elif X < 0 and Y < 0:
    print('III четверть плоскости')