import time
import os

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},

]

directories = {
    '1': ["2207 876234", "11-2"],
    '2': ["10006"],
    '3': []
}

def write_log_path(path):
    def _write_log(old_function):

        def new_function(*args, **kwargs):
            time_stamp_start = time.strftime('%Y-%m-%d-%H_%M_%S')
            result = old_function(*args, **kwargs)
            log_info = f'время вызова: {time_stamp_start}, функция: {old_function.__name__}, ' \
                       f'для аргументов {args}, {kwargs} значение функции: {result}'
            # print(time_stamp_start, old_function.__name__, args, kwargs)
            path_write = os.path.join(os.getcwd(), path)
            with open(path_write, "a", encoding='utf-8') as file:
                file.write(log_info + "\n")
            return result
        return new_function
    return _write_log

@write_log_path('log_2.txt')
def people(catalog):
    '''
    Функция находит Имя и Фамилию человека по номеру документа.
    Переменная catalog - это список со словарями по шаблону:
    <название списка> = [{"type": "тип документа", "number": "номер", "name": "Имя Фамилия"}]
    '''
    doc_num = input("\nНайти человека по номеру документа\nВведите номер документа: ")
    count = 0
    for doc_list in catalog:
        if doc_list["number"] == doc_num:
            return f"\n>>> По номеру документа найден {doc_list['name']}"
            count = + 1
    if count == 0:
        return f">>>По номеру документа нет данных"


def shelf(shelf_list):
    '''
    Функция находит полку хранения документа по номеру документа.
    Переменная shelf_list - это словарь по шаблону:
    <название словаря> = {"номер полки": [список номеров документов]}
    '''
    doc_num = input("\nНайти номер полки с документом\nВведите номер документа: ")
    count = 0
    for number_shelf, numbers_list in shelf_list.items():
        if doc_num in numbers_list:
            return print(f">>> Документ с указанным номером находится на полке №{number_shelf}")
            count = + 1
    if count == 0:
        return print(">>>По номеру документа нет данных")


def doc_listing(catalog):
    '''
    Функция выводит список всех документов с указанием типа документа, номера
    и Имя Фамилии человека.
    Переменная catalog - это список со словарями по шаблону:
    <название списка> = [{"type": "тип документа", "number": "номер", "name": "Имя Фамилия"}]}
    '''
    lst_3 = ""
    for doc_list in documents:
        lst_1 = ""
        for doc_items in doc_list.values():
            lst = doc_items
            lst_1 += "\"" + lst + "\" "
        lst_3 += lst_1.replace("\"", "", 2) + "\n"
    return print(f"\n>>> Список документов:\n{lst_3}")


def add_document(catalog, shelf_list):
    '''
    Функция добавляет новый документ на указанную полку.
    Переменная catalog - это список со словарями по шаблону:
    <название списка> = [{"type": "тип документа", "number": "номер", "name": "Имя Фамилия"}]}
    Переменная shelf_list - это словарь по шаблону:
    <название словаря> = {"номер полки": [список номеров документов]}
    '''
    document_type = input("Введите название документа: ")
    document_number = input("Введите номер документа: ")
    document_owner = input("На чье имя документ: ")
    shelf_exist = True
    while shelf_exist:
        document_shelf = input("На какую полку положить, укажите номер: ")
        if document_shelf in shelf_list.keys():
            shelf_list[document_shelf].append(document_number)
            shelf_exist = False
        else:
            print("\nВы ввели номер несуществующей полки, попробуйте еще раз!\n")
            print(f"Доступны номера полок от 1 до {len(shelf_list.keys())}")
    dict_add = {"type": document_type, "number": document_number, "name": document_owner}
    catalog.append(dict_add)
    print(
        f"\n>>> Документ {document_type} с номером {document_number} на имя {document_owner} добавлен на полку {document_shelf}")




switch = True
while switch:
    print(
        '''
      - для просмотра списка документов введите букву "l"
      - для добавления нового документа введите букву "a"
      - найти человека по номеру документа введите букву "p"
      - узнать, где находится джокумент введите букву "s"
      - для выхода из программы введите букву "q"
      '''
    )
    command = input("Введите выбранную букву: ")
    if command == "p":
        people(documents)
    elif command == "s":
        shelf(directories)
    elif command == "l":
        doc_listing(documents)
    elif command == "a":
        add_document(documents, directories)
    elif command == "q":
        print("Программа закончила работу.")
        break
    else:
        print("Такой команды нет.\n")


