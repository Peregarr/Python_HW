
# Задайте список из нескольких чисел. Напишите программу,
#  которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


list = [2, 3, 5, 9, 3]

sum = 0
n = 0
for i in list:
    if n % 2 != 0:
        sum = list[n] + sum
    n += 1
print(sum)
