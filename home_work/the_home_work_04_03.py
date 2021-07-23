'''
В приложении заданы словари с названиями, рейтингами и жанрами сериалов shows и ratings.
Напишите программу, которая рассчитывает средний рейтинг для сериалов с жанром “фантастика”.
'''
# импорт из сущетсвующей уже базы
from bd_for_hw_04 import shows, ratings

average_list = []

for x in shows.keys():
    if x in ratings.keys():
        if shows.setdefault(x) == 'фантастика':
            average_list.append(ratings.setdefault(x))
        print(average_list)

average_ratio = 0

for i in average_list:
    average_ratio = average_ratio + i

result = average_ratio/len(average_list)

print(result)