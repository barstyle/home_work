'''Создайте класс Person, хранящий базовые данные о каком-нибудь человеке.
У класса должно быть два параметра:
- Фамилия
- Имя
И два метода:
- Конструктор __init__
- Метод __str__ для вывода объектов на печать. Определите метод __str__ таким образом,
чтобы при печати объекта выводились имя и фамилия. Например “Иван Иванов”.
Создайте и распечатайте с помощью print два объекта класса Person с любыми именами и фамилиями.'''


class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


if __name__ == '__main__':

    one_player = Person('Хидэаки', 'Анно')
    two_player = Person('Масаси', 'Кисимото')

    print(one_player)
    print(two_player)