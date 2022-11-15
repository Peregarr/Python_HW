# 4 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#  Входные и выходные данные хранятся в отдельных текстовых файлах.



with open('py_hw5/file_1.txt', 'r') as data:
    text = data.read()
# text = 'aaaaaaaaaabbbbbbbbbbbbccccc222222==========='
print(f'исходные данные: {text}')

count = 1
new_text = ''

for i in range(len(text)-1):
    if text[i] == text[i + 1]:
        count += 1
        if count == 9:
            new_text = new_text + str(count) + text[i]
            count = 1
    elif text[i] != text[i + 1]:
        new_text = new_text + str(count) + text[i]
        count = 1
if count > 1 or text[len(text) - 2] != text[-1]:
    new_text = new_text + str(count) + text[-1]



with open('py_hw5/file_2.txt', 'w') as data:
    data.write(new_text)

with open('py_hw5/file_2.txt', 'r') as data:
    file_2 = data.read()
print(f'Сжатый файл: {file_2}')

txt = ''.join(file_2)

num = ''
in_text = ''

for i in range(0, len(txt), 2):
    num = txt[i]
    in_text = in_text + txt[i + 1] * int(num)
print(f'Восстановленные данные: {in_text}')

