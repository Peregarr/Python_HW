# 1 Напишите программу, которая принимает на вход вещественное число
#  и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11


from decimal import Decimal


num = Decimal(input("Введите вещественное число:"))

while int(num) != num:
        num *= 10
sum = 0
while num > 0:
        dig = num - num % 10
        sum = sum + (num - dig)
        num = num // 10
print(sum)