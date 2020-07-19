from random import randrange
import random
import math
import numpy as np

MAX_VALUE =  2.5

lenList = int(input('Введите длинну массива: '))
maxNumber = int(input('Введите число разброса: ')) 

arrayList = []
result = 0

for i in range(lenList):
    arrayList.append(float(round(randrange(maxNumber)*random.random(), 2)))
print(arrayList)

for i in arrayList:
    if math.fabs(i) > MAX_VALUE:
        result += i**2
print(round(result, 2)) 
