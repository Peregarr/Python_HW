
# Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент,
#  второй и предпоследний и т.д.
#  Пример:

# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]


list = [2, 3, 4, 5, 6]
lst = []
pow = 0
n = 0
j = 0
while n < len(list) / 2:
    pow = list[n] * list[j-1]
    n += 1
    j -= 1
    lst.append(pow)
print(lst)


