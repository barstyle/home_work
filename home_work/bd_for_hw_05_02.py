'''
В приложении заданы словари с названиями, рейтингами и жанрами сериалов shows и ratings.

Напишите программу, которая состоит из двух функций:

- Первая функция получает на вход словарь shows и название жанра.
Функция должна вернуть все названия сериалов для заданного жанра;

- Вторая функция получает на вход словарь ratings и список названий сериалов.
Функция должна вернуть средний рейтинг для сериалов из входного списка.
Создайте модуль, содержащий эти функции.

Импортируйте модуль в свою программу и с помощью этих двух функций исследуйте
средний рейтинг для жанров “драма” и “криминал”.
'''

from bd_for_hw_04 import shows, ratings

# Возвращает названия сериалов для заданного жанра
def shows_select(genre):
    shows_list = []
    for text in shows.keys():
        if genre == shows.setdefault(text):
            shows_list.append(text)
    return shows_list

# тут мы запускади проверочик - как работают функции
# print(shows_select('драма'))
# print(shows_select('криминал'))
# print(shows_select('фэнтази'))
# print(shows_select('фантастика'))

# должна вернуть средний рейтинг для сериалов из входного списка.
def ratio_average(shows_set):
    average_ratio = 0
    for i in shows_set:
        average_ratio = average_ratio + ratings.setdefault(i)
    return average_ratio / len(shows_set)

# тут тоже проверки были
# print()
# text = shows_select('фантастика')
# print(ratio_average(text))

# все закомментировали, что бы не результаты не импортироались