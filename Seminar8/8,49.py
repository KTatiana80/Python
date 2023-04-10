# Создать телефонный справочник с возможностью импорта и
# экспорта данных в формате .txt. Фамилия, имя, отчество,
# номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для
# поиска определенной записи(Например имя или фамилию человека)

# Использование функций. Ваша программа не должна быть линейной

import os

def add_person():
    last_name = input('Введите фамилию: ')
    name = input('Введите имя: ')
    surname = input('Введите отчество: ')
    phone = input('Введите номер телефона: ')
    data = open(
        'C:\\Users\\Танюшка\\Desktop\\python\\Seminar8\\Phonebook1.txt', 'a', encoding='utf-8')
    data.writelines([last_name, ' ', name, ' ', surname, ' ', phone, '\n'])
    data.close()


def print_data():
    with open('C:\\Users\\Танюшка\\Desktop\\python\\Seminar8\\Phonebook1.txt', 'r', encoding='utf-8') as data:
        print(data.read())


def search():
    search_name = input('Введите данные: ')
    with open('C:\\Users\\Танюшка\\Desktop\\python\\Seminar8\\Phonebook1.txt', 'r', encoding='utf-8') as data:
        for line in data:
            if search_name in line:
                print(line)


def load_data():
    with open('C:\\Users\\Танюшка\\Desktop\\python\\Seminar8\\Phonebook1.txt', 'r+', encoding="utf-8") as data:
        text_data = data.read().splitlines()
        path = input("Укажите путь к импортируемому файлу: ")
        with open(path, 'r', encoding="utf-8") as data_2:
            for line in data_2:
                if line not in text_data:
                    data.write(line)


def del_person():
    del_name = input('Введите данные контакта, который хотите изменить: ')
    with open('C:\\Users\\Танюшка\\Desktop\\python\\Seminar8\\Phonebook1.txt', 'r', encoding='utf-8') as data:
        d = data.readlines()
        for i_line in range(len(d)):
            if del_name in d[i_line]:
                del d[i_line]
    with open('C:\\Users\\Танюшка\\Desktop\\python\\Seminar8\\Phonebook1.txt', 'w', encoding='utf-8') as data:
        for line in d:
            data.write(line)


def change_person():
    change_name = input('Введите данные контакта, который хотите изменить: ')
    last_name = input('Введите новую фамилию: ')
    name = input('Введите новое имя: ')
    surname = input('Введите новое отчество: ')
    phone = input('Введите новый номер телефона: ')

    with open('C:\\Users\\Танюшка\\Desktop\\python\\Seminar8\\Phonebook1.txt', 'r', encoding='utf-8') as data:
        d = data.readlines()
    for i_line in range(len(d)):
        if change_name in d[i_line]:
            d[i_line] = last_name + ' ' + name + ' ' + surname + ' ' + phone
    
    with open('C:\\Users\\Танюшка\\Desktop\\python\\Seminar8\\Phonebook1.txt', 'w', encoding='utf-8') as data:
        for line in d:
            data.write(line)


def ui():
    print('''1 - добавить контакт
2 - поиск
3 - импорт данных
4 - вывод в консоль
5 - удалить контакт
6 - изменить контакт
7 - выход''')
    user_input = input('Выберите нужный вариант: ')
    while user_input != '7':
        if user_input == '1':
            add_person()
        elif user_input == '2':
            search()
        elif user_input == '3':
            load_data()
        elif user_input == '4':
            print_data()
        elif user_input == '5':
            del_person()
        elif user_input == '6':
            change_person()
        elif user_input == '7':
            print_data()
        else:
            print('вы ввели не корректный вариант, попробуйте еще раз. ')
        print('''1 - добавить контакт
2 - поиск
3 - импорт данных
4 - вывод в консоль
5 - удалить контакт
6 - изменить контакт
7 - выход''')
        user_input = input('введите нужный вариант: ')


def main():
    ui()


if __name__ == "__main__":
    main()
