"""
Homework Assignment. Python Core. Module 10
For a description of the task, please refer to the README.md file
"""

from collections import UserDict


class Field:
    """
    Базовий клас для полів запису.
    Буде батьківським для всіх полів, у ньому реалізується логіка загальна для всіх полів
    """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """
    Клас для зберігання імені контакту.
    Обов'язкове поле.
    """
    
    # реалізація класу

    pass


class Phone(Field):
    """
    Клас для зберігання номера телефону.
    Має валідацію формату (10 цифр).
    Необов'язкове поле з телефоном та таких один запис Record може містити декілька.
    """
    
    # реалізація класу
                # Реалізовано валідацію номера телефону (має бути 10 цифр)
    pass


class Record:
    """
    Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
    Відповідає за логіку додавання/видалення/редагування необов'язкових полів та зберігання обов'язкового поля Name
    """
    
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    
    # Додавання телефонів
    def add_phone(self, x):
        self.x = x
        pass

    # Видалення телефонів
    def remove_phone(self, a):
        self.a = a
        pass

    # Редагування телефонів
    def edit_phone(self, s, d):
        self.s = s
        self.d = d
        pass

    # Пошук телефону
    def find_phone(self, y):
        self.y = y
        pass

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    """
    Клас для зберігання та управління записами.
    Успадковується від UserDict, та містить логіку пошуку за записами до цього класу
    """

    # Додавання записів
    def add_record(self, f):
        self.f = f
        pass

    # Пошук записів за іменем
    def find(self, g):
        # self.book.find("Jane")
        self.g = g
        pass

    # Видалення записів за іменем
    def delete(self, j):
        # self.book.delete("Jane")
        self.j = j
        pass



if __name__ == "__main__":
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")