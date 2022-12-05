# Задайте число. Составьте список чисел Фибоначчи,
#  в том числе для отрицательных индексов.
# Пример:

# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]


num = int(input('Введите число k: '))
fib = []
negafib = []

for i in range(num + 1):
    if i == 0:
        fib.append(0)
    elif i == 1:
        fib.append(1)
    else:
        fib.append(fib[i - 1] + fib[ - 2])
for i in range(num, 0, -1):
    negafib.append(((-1) ** (i + 1)) * fib[i])
print(f'k = {num} {negafib + fib}')



