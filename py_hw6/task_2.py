# Дана последовательность чисел.
#  Получить список уникальных элементов заданной последовательности,
#  список повторяемых и убрать дубликаты из заданной последовательности.

# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]


lst_init = [11, 2, 3, 5, 11, 5, 3, 10]

lst1 = []
lst2 = []

for i in set(lst_init):
    if lst_init.count(i) > 1:
        lst2.append(i)
    else:
        lst1.append(i)
print(f'Исходный список {lst_init}')
print(f'Уникальные элементы {lst1}')
print(f'Повторяемые {lst2}')
print(f'Список без повторений {list(set(lst_init))}')

