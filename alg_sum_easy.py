# Найти алгебраическую сумму для выражения: 1k + 2k + 3k + … + Nk. 
# N и степень k вводит пользователь.

x = int(input('Введите количство N: '))
k = int(input('Введите степень: '))

result = 0

for i in range(x):
    i += 1
    result += i**k
print(result)