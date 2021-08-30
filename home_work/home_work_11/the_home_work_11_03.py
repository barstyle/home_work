'''Создайте класс-наследник Person, который будет хранить данные абстрактного преподавателя.
Назовите его Professor.

У класса Student должны быть все параметры класса Person,
плюс дополнительный параметр - название курса, который читает преподаватель.

Кроме того, у класса Professor должен быть метод test_stugents, который получает на вход список студентов
и для каждого студента устанавливает случайную оценку от 0 до 10 с помощью метода set_test_score класса Student.

Переопределите метод __str__ таким образом, чтобы информация о преподавателе выводилась в
формате “Преподаватель: Семен Семенов читает курс ООП”

Создайте список из нескольких студентов.

Создайте объект-преподавателя. Сделайте так, чтобы преподаватель провел для студентов 2 теста.
После каждого из тестов распечатайте состояния студентов.'''
import random
from the_home_work_11_02 import Student


# Создайте класс-наследник Person - Назовите его Professor.
class Professor(Student):

    # плюс дополнительный параметр - название курса, который читает преподаватель.
    def __init__(self, first_name, last_name, group='ГР-01', course='ООП'):
        super().__init__(first_name, last_name, group)
        self.course = course

    # Переопределите метод __str__
    def __str__(self):
        return f'Преподаватель: {self.first_name} {self.last_name} читает курс {self.course}'

    # у класса Professor должен быть метод test_students
    def test_students(self, stud_list, n):
        for i in stud_list:
            for j in range(n):
                i.set_test_score(random.randint(1, 10))


# чтобы информация о преподавателе выводилась в формате “Преподаватель: Семен Семенов читает курс ООП”
teacher = Professor('Гвидо', 'Россум')
print(teacher)
print('-'*50)

# Создайте список из нескольких студентов.
name_list = [['Асума', 'Сарутоби'], ['Майто', 'Гай'], ['Хаширама', 'Сенджу'],
             ['Минато', 'Намиказе'], ['Шино', 'Абураме']]

student_list = [('student_0' + str(i)) for i in range(1, 6)]

# Сдаем документы в универ
for i in range(5):
    student_list[i] = Student(name_list[i][0], name_list[i][1])

# распечатывем зачетки до атесстации
for j in student_list:
    print(j)

print('-'*50)

# Сделайте так, чтобы преподаватель провел для студентов 2 теста.
teacher.test_students(student_list, 2)

# распечатывем зачетки после атесстации
for j in student_list:
    print(j)

print('-'*50)

# преподаватель провел для студентов еще 5 тестов.
teacher.test_students(student_list, 5)

# распечатывем зачетки после второй атесстации
for j in student_list:
    print(j)