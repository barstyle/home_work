'''
В приложении заданы 4 словаря с названиями и жанрами сериалов,
которые нравятся Ане, Оле, Насте и Свете. Напишите функцию,
которая получает на вход два словаря и возвращает пересечение жанров.
Например, Ане и Свете обеим нравятся фантастика и драма.
С помощью функции найдите общие жанры для:
- Ани и Насти
- Оли и Светы
- Светы и Ани
'''
# импортируем словари
from bd_for_hw_04 import shows, ratings, sveta, nastya, olya, anya


def conjoint(name_01, name_02):
    likes_genre = set()
    for genre in name_01.values():
        if genre in name_02.values():
            likes_genre.add(genre)
    if len(likes_genre) > 0:




print(conjoint(anya, nastya))
print()
print(conjoint(olya, sveta))
print()
print(conjoint(sveta, anya))