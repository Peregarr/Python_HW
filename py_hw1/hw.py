# 1 Напишите программу, которая принимает на вход цифру,
#  обозначающую день недели, и проверяет,
#  является ли этот день выходным.

# num = int(input('введите день недели: '))
# if num > 7 or num < 1:
#     print('такого дня недели не существует')
# elif num < 6:
#     print('Не выходной день')
# else:
#     print('Выходной день')



# 2 Напишите программу
#  для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
#  для всех значений предикат.

# for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 print(not (x or y or z) == (not x and not y and not z))
#                 print(x, y, z)


# 3 Напишите программу, которая принимает на вход координаты точки (X и Y),
#  причем X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
#  в которой находится эта точка (или на какой оси она находится).

# x = int(input('Введите число X не равное 0:'))
# y = int(input('Введите число Y не равное 0:'))


# if x == 0 and y == 0:
#     print('числа X, Y равны нулю, повторите ввод;)')
# elif x > 0 and y > 0:
#     print(f'Координаты точки находятся в плоскости 1 ')
# elif x < 0 and y > 0:
#     print(f'Координаты точки находятся в плоскости 2 ')
# elif x < 0 and y < 0:
#     print(f'Координаты точки находятся в плоскости 3 ')
# elif x > 0 and y < 0:
#     print(f'Координаты точки находятся в плоскости 4 ')


# 4 Напишите программу, которая по заданному номеру четверти,
#  показывает диапазон возможных координат точек в этой четверти (x и y).

# quarter = int(input('Введите номер четверти из 4х: '))

# if quarter == 1:
#     print('x > 0, y > 0')
# elif quarter == 2:
#     print('x < 0, y > 0')
# elif quarter == 3:
#     print('x < 0, y < 0')
# elif quarter == 4:
#     print('x > 0, y < 0')
# else:
#     print('Введите правильное значение, от 1 до 4')


# 5 Напишите программу,
#  которая принимает на вход координаты двух точек
#  и находит расстояние между ними в 2D пространстве.

# import math

# xa = float(input('Введите координату точки А по оси Х: '))
# ya = float(input('Введите координату точки А по оси Y: '))
# xb = float(input('Введите координату точки B по оси Х: '))
# yb = float(input('Введите координату точки B по оси Y: '))

# distance = round(math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2), 2)
# print(distance)