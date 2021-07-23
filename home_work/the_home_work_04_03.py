'''
В приложении заданы словари с названиями, рейтингами и жанрами сериалов shows и ratings.
Напишите программу, которая рассчитывает средний рейтинг для сериалов с жанром “фантастика”.
'''
# импорт из сущетсвующей уже базы
from bd_for_hw_04 import shows, ratings

for x in shows.keys():
    if x in ratings:
        print(x, '-', shows.setdefault(x), '-', ratings.setdefault(x))