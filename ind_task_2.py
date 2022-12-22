class Notebook:

    def __init__(self):
        self.note = {}

    def add_note(self, key, val):
        self.note[key] = val
        return 'Контакт создан'

    def del_note(self, x):
        if x in self.note:
            del self.note[x]
            return f'{x} удален'
        return 'Контакт не найден'

    def find(self, x):
        for x in self.note:
            note = ' '.join(self.note[x])
            return f'Найден контакт: {x} {note}'
        return "Контакт не найден"

    def info(self):
        return self.note.items()

    def sort_by_surname(self):
        return sorted(self.note.items())

    def sort_by_date(self):
        return sorted(self.note.items(), key=lambda val: val[1][0][::-1])


print('\nЗаписная книжка')
print('''Выберите действие:
 1 - Добавить запись
 2 - Найти запись
 3 - Удалить запись
 4 - Посмотреть все записи
 5 - Отсортировать записи
 0 - Выход''')

book = Notebook()

while True:
    print("\nВведите номер действия")
    command = input()
    if command == '1':
        surname = input("Фамилия: ")
        date = input("Дата рождения: ")
        number = input("Номер телефона: ")
        print(book.add_note(surname, [date, number]))

    elif command == '2':
        print("Введите:\n1 - для поиска записи по фамилии\n2 - для поиска записи по номеру телефона")
        variant = input()
        if variant == '1':
            name = input("Введите фамилию контакта ->  ")
            print(book.find(name))
        elif variant == '2':
            number = input("Введите номер телефона контакта ->  ")
            print(book.find(number))

    elif command == '3':
        name = input("Введите фамилию контакта, которого хотите удалить ->  ")
        print(book.del_note(name))

    elif command == '4':
        for name, data in book.info():
            data = ' '.join(data)
            print(name, data)

    elif command == '5':
        print("Введите:\n1 - для сортировки записей по фамилии\n2 - для сортировки записи по дате рождения")
        variant = input()
        if variant == '1':
            for name, data in book.sort_by_surname():
                data = ' '.join(data)
                print(name, data)
        elif variant == '2':
            for name, data in book.sort_by_date():
                data = ' '.join(data)
                print(name, data)

    elif command == '0':
        break

    else:
        print('Неизвестное действие')
