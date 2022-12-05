# 3) Задайте последовательность чисел. Напишите программу,
#  которая выведет список неповторяющихся элементов исходной последовательности.
# Пример:
# 1 1 2 3 4 4 5 6 7 7 8 --->> 2 3 5 6 8


numbers = list(map(int, input('Введите числа: ').split()))

del_duplicate_nums = [i for i in numbers if numbers.count(i) == 1]
print(del_duplicate_nums)
