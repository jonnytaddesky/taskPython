x = int(input('Введите количство N: '))
k = int(input('Введите степень: '))

result = 0

for i in range(x):
    i += 1
    result += i**k
print(result)