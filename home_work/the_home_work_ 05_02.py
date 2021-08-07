'''
Создайте модуль, [bd_for_hw_05_02] содержащий эти функции.
Импортируйте модуль в свою программу и с
помощью этих двух функций исследуйте средний
рейтинг для жанров “драма” и “криминал”.
'''

from bd_for_hw_05_02 import shows_select, ratio_average

def is_average_ratio(genre):
    result = ratio_average(shows_select(genre))
    return ('{}{}{}{}'.format('Среднее занчение ретинга фильмов жанра - ', genre,
                              ' - ', round(result, 2)))

print(is_average_ratio('фантастика'))
print(is_average_ratio('драма'))
