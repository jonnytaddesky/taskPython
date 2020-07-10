# Возвести, введенное с клавиатуры число, в степень n, 
# степень тоже вводится с клавиатуры. 
# Возведение в степень организовать с использованием циклов.

number = int(input('Enter number: '))
power = int(input('Enter power: '))

result = 1

for i in range(power):
     result *= number
print(result)
