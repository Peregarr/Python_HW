# Напишите программу вычисления арифметического выражения заданного строкой.
#  Используйте операции +,-,/,*. приоритет операций стандартный.
# Пример:

# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;

# Добавьте возможность использования скобок, меняющих приоритет операций.
# Пример:

# 1+2*3 => 7;
# (1+2)*3 => 9;


################################# первая попытка
# text = '2+3'

# operators = '+-*/'

# # print(operators[1])
# for i in range(0, len(text)):
#     if text[i] == operators[0] or operators[1] or operators[2] or operators[3]:
#         op = text[i+1]
#         if op == text[i+1]:
#             num1 = int(text[2])
#             num2 = int(text[0])
#             print(num1 + num2)
#             break
##################################


text = '(2+2)*3'
txt = text

def Get_expression(text):
    expression = Convert_to_list(text)
    while '(' in expression:
        expression = Brackets(expression, 0, len(expression))
    expression = Mult_div(expression, 0, len(expression))
    expression = Sum_sub(expression, 0, len(expression))
    return expression


def Convert_to_list(text):
    expression = []
    operators = '+-*/()'
    num = ''
    for i in text:
        if i in (operators):
            if num != '':
                expression.append(int(num))
                num = ''
            expression.append(i)
        else:
            num += i
    if num != '':
        expression.append(int(num))
    return expression


def Brackets(expression, start, end):
    i = start
    # count = 0
    while i < end:
        if expression[i] == '(':
            start = i
        if expression[i] == ')':
            end = i
            expression.pop(end)
            expression.pop(start)
            expression = Mult_div(expression, start, end - 2)
            expression = Sum_sub(expression, start, end - 2)
            return expression
        i += 1


def Mult_div(expression, start, end):
    i = start
    while i < end:
        if expression[i] == '*':
            expression[i - 1] *= expression[i + 1]
            expression.pop(i)
            expression.pop(i)
            end -= 2
            i -= 1
        elif expression[i] == '/':
            expression[i - 1] /= expression[i + 1]
            expression.pop(i)
            expression.pop(i)
            end -= 2
            i -= 1
        i += 1
    return expression


def Sum_sub(expression, start, end):
    i = start
    while i < end:
        if expression[i] == '+':
            expression[i - 1] += expression[i + 1]
            expression.pop(i)
            expression.pop(i)
            end -= 2
        elif expression[i] == '-':
            expression[i - 1] -= expression[i + 1]
            expression.pop(i)
            expression.pop(i)
            end -= 2
        i += 1
    return expression

# t = type(Get_expression(text))
print(f'{txt} =', Get_expression(text))


