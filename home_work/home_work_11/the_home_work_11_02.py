'''Создайте класс-наследник Person, который будет хранить данные абстрактного студента.
Назовите его Student. У класса Student должны быть все параметры класса Person,
плюс два дополнительных параметра:
- Номер группы
- Список оценок по тестам
Также у класса Student должен быть дополнительный метод set_test_score,
получающий на вход оценку по тесту и добавляющий ее в список оценок студента.
Переопределите метод __str__ таким образом, чтобы информация о студенте
выводилась в формате “Студент: Иван Иванов, группа ГР-01, оценки [5, 0]”
Создайте несколько объектов класса Student,
распечатайте их параметры с помощью print.'''
import random
from the_home_work_11_01 import Person


class Student(Person):

    def __init__(self, first_name, last_name, group='ГР-01'):
        super().__init__(first_name, last_name)
        self.rate = []
        self.group = group

    def set_test_score(self, rate):
        self.rate.append(rate)

    def __str__(self):
        return f'Студент: {self.first_name} {self.last_name}, группа {self.group}, оценки {self.rate}'

if __name__ == '__main__':
    one_pers = Student('Асума', 'Сарутоби')
    two_pers = Student('Майто', 'Гай')

    for i in range(2):
        one_pers.set_test_score(random.randint(1, 10))
        two_pers.set_test_score(random.randint(1, 10))

    print(one_pers, '\n' + str(two_pers))