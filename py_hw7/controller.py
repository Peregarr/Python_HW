from import_data import import_data
from export_data import export_data
from print_data import print_data
from search_data import search_data

def hello():
    print("Телефонный справочник")

def input_info():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    date_of_birth = input("Введите дату рождения: ")
    phone_number = input("Введите номер контакта: ")
    category = input("Введите категорию контакта: ")
    return [last_name, first_name, middle_name, date_of_birth, phone_number, category]

def choice_sep():
    sep = input("Введите разделитель: ")
    if sep == "":
        sep = None
    return sep

def choice_action():
    print("Возможные действия:\n\
    1 - импорт;\n\
    2 - экспорт;\n\
    3 - поиск контакта.")
    action = input("Введите номер действия: ")
    if action == '1':
        sep = choice_sep()
        import_data(input_info(), sep)
    elif action == '2':
        data = export_data()
        print_data(data)
    elif action == '3':
        word = input("Введите данные для поиска: ")
        data = export_data()
        item = search_data(word, data)
        if item != None:
            print("Фамилия".center(20), "Имя".center(20), "Отчество".center(20), "Дата рождения".center(20), "Телефон".center(15), "Категория".center(30))
            print("-"*130)
            print(item[0].center(20), item[1].center(20), item[2].center(20), item[3].center(20), item[4].center(15), item[5].center(30))
        else:
            print("Данные не обнаружены")
    else:
        print('Выберите действие из предложенных')
        exit