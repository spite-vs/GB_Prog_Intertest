import csv
import os.path
from datetime import datetime


def err():
    print('\n -- Открой глаза шире и нажимай на клавиши с умом --')


def end():
    print('\n -- Возвращайся, я буду ждать --')


def title():
    return input('Название произведения:\n')


def body_note():
    return input('Погнали:\n')


def index():
    if not os.path.isfile('notes.csv'):
        return 1
    else:
        with open('notes.csv', 'r', encoding='utf-8', newline='') as pb:
            reader = csv.DictReader(pb, delimiter=';')
            var = list(reader)
            return int(var[-1]["№"])+1


def wrt(dt):
    headers = ['№', 'Title', 'Body_note', 'Date_time']
    with open('notes.csv', 'w', encoding='utf-8', newline='') as pb:
        writer = csv.DictWriter(pb, fieldnames=headers, delimiter=';')
        writer.writeheader()
        writer.writerows(dt)


def input_data():
    buffer = f'{index()};{title()};{body_note()};{str(datetime.now()).split(".")[0]}\n'
    if not os.path.isfile('notes.csv'):
        with open('notes.csv', 'a', encoding='utf-8', newline='') as pb:
            pb.write('№;Title;Body_note;Date_time\n')
            pb.write(buffer)
    else:
        with open('notes.csv', 'a', encoding='utf-8', newline='') as pb:
            pb.write(buffer)
    print('\n -- Схоронил, будь спокоен --')


def print_data():
    with open('notes.csv', 'r', encoding='utf-8', newline='') as pb:
        reader = csv.DictReader(pb, delimiter=';')
        var = list(reader)
        com = input('\nОтсортировать по дате? (Y/N)(Д/Н)')
    while com not in 'yYnNдДнН':
        err()
        com = input(
            '\nОтсортировать по дате? (Y/N)(Д/Н)')
    if com in 'nNнН':
        print()
        for i in var:
            print(
                f'{i["№"]:>3}. {i["Title"]} ({i["Date_time"]})')
        print()
    else:
        for i in sorted(var, key=lambda x: datetime.strptime(x['Date_time'], '%Y-%m-%d %H:%M:%S')):
            print(
                f'{i["№"]:>3}. {i["Title"]} ({i["Date_time"]})')
        print()
    num = input('Под каким номером надо что-то перечитать: ')
    while not num.isdigit() or int(num) < 1 or int(num) > len(var):
        err()
        num = input('Под каким номером надо что-то перечитать: ')
    num = int(num)
    print(
        f'\n{var[num-1]["Title"]}: \n\t{var[num-1]["Body_note"]}')


def put_data():
    with open('notes.csv', 'r', encoding='utf-8', newline='') as pb:
        reader = csv.DictReader(pb, delimiter=';')
        var = list(reader)
        print()
        for i in var:
            print(
                f'{i["№"]:>3}. {i["Title"]} ({i["Date_time"]})')
        print()
    number = input('\nКакую заметку вздумалось поменять: ')
    while not number.isdigit() or int(number) < 1 or int(number) > len(var):
        err()
        number = input('\nКакую заметку вздумалось поменять: ')
    number = int(number)
    key_data = {'2': 'Title', '3': 'Body_note'}
    key_operation = {'2': title, '3': body_note}
    print(
        f'\n{var[number-1]["Title"]}: \n\t{var[number-1]["Body_note"]}')
    print('\nЧто переписываем?\n\n1. Всё\n2. Заголовок\n3. Заметку\n4. Стой! Я передумал')
    com = input("Введите номер операции: ")
    while not com.isdigit() or int(com) < 1 or int(com) > 4:
        err()
        print(
            '\nЧто переписываем?\n\n1. Всё\n2. Заголовок\n3. Заметку\n4. Стой! Я передумал')
        com = input("Введите номер операции: ")
    if com == '4':
        end()
    elif com == '1':
        for i in key_data:
            var[number-1][key_data[i]] = key_operation[i]()
            var[number-1]['Date_time'] = str(datetime.now()).split(".")[0]
        wrt(var)
        print('\n -- Переписал --')
    else:
        var[number-1][key_data[com]] = key_operation[com]()
        var[number-1]['Date_time'] = str(datetime.now()).split(".")[0]
        wrt(var)
        print('\n -- Переписал --')


def delete_data():
    with open('notes.csv', 'r', encoding='utf-8', newline='') as pb:
        reader = csv.DictReader(pb, delimiter=';')
        var = list(reader)
        print()
        for i in var:
            print(
                f'{i["№"]:>3}. {i["Title"]} ({i["Date_time"]})')
        print()
    number = input('От чего решил избавиться: ')
    while not number.isdigit() or int(number) < 1 or int(number) > len(var):
        err()
        number = input('От чего решил избавиться: ')
    number = int(number)
    print(
        f'\n{var[number-1]["Title"]}: \n\t{var[number-1]["Body_note"]}')
    com = input('\nУверен, что это оно? (Y/N)(Д/Н)')
    while com not in 'yYnNдДнН':
        err()
        com = input(
            '\nУверен, что это оно? (Y/N)(Д/Н): ')
    if com in 'nNнН':
        end()
    else:
        del var[number-1]
        for i in range(number-1, len(var)):
            if i == 0:
                var[0]['№'] = 1
                continue
            var[i]['№'] = int(var[i-1]['№'])+1
        wrt(var)
        print('\n -- Выкинул и забыл :( --')


def choise():
    command = ''
    operation = {'1': input_data, '2': delete_data, '3': put_data,
                 '4': print_data, '5': end}
    while command != '5':
        print('\nХотите сохранить свои фантазии в файле csv? Я к Вашим услугам:\n1. Излить душу\n2. Уничтожить воспоминание\n3. Изменить прошлое\n4. Поностальгировать\n5. Закончить сеанс самотерапии')
        command = input("Введите номер операции: ")
        operation.get(command, err)()


choise()
