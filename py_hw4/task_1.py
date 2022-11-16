# 1) Вычислить число c заданной точностью d
# Пример:
# при d = 0.001, π = 3.142 10^(-1) ≤ d ≤10^(-10)

import random

number = random.uniform(1, 8)
degree = random.randint(-10, -1)
deg = 10 ** degree

res = round(number, degree)
print(f'Введенное число {number=}, точность округления {deg=} результат = ', res)
