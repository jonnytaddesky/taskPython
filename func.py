import math
import itertools
import numpy

# def step(x, m):
#     x = 1
#     m = 1
#     result = 1
#     for t in range(m):
#         result *= x
#         return result


# def func():
x1, x2, dx = -1.1, 0.3, 0.2
m1, m2, dm = 1, 5, 1
for i, j in itertools.product(range(-1.1, 0.3, 0.2), range(1, 5, 1)):
    print(i + j)