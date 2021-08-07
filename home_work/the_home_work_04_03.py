'''
В приложении заданы словари с названиями, рейтингами и жанрами сериалов shows и ratings.
Напишите программу, которая рассчитывает средний рейтинг для сериалов с жанром “фантастика”.
'''

# импорт из сущетсвующей уже базы
from bd_for_hw_04 import shows, ratings


# создаем функцию которая считает средний рейтинг по жанру
def is_which_ratio(genre):
    # список для хранения рейтингов
    average_list = []

    # заполняем список рейтингами конкретного жанра
    for x in shows.keys():
        if x in ratings.keys():
            if shows.setdefault(x) == genre:
                average_list.append(ratings.setdefault(x))

    # создаем переменную с нулевым значением, чтоб посчитать сумму ретинга
    average_ratio = 0

    # в этом цикле считаем сумму рейтингов
    for i in average_list:
        average_ratio = average_ratio + i

    # вычисляем среднее значение
    result = average_ratio / len(average_list)

    # закрепялем результат с пояснительной бригадой для красоты
    return ('{}{}{}{}'.format('Среднее занчение ретинга фильмов жанра - ', genre,
                             ' - ', round(result, 2)))

print(is_which_ratio('фантастика'))
# print(is_which_ratio('криминал'))
# print(is_which_ratio('драма'))
# print(is_which_ratio('фэнтази'))