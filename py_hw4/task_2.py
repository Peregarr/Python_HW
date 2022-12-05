# 2) Задайте натуральное число N. Напишите программу,
#  которая составит список простых множителей числа N.


n = int(input('Введите число: '))
temp = n
factors = []
i = 2
while i * i <= n:
    while n % i == 0:
        n = n // i
        factors.append(i)
    i += 1
if n > 1:
    factors.append(n)
print(f'Введено число {temp}. Список простых множителей {sorted(list(set(factors)))}')

