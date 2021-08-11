'''
Напишите функцию, которая:
- Принимает на вход название жанра;
- Рассчитывает и выводит на экран название жанра, число сериалов и среднюю оценку;
- Создает словарь, содержащий только фильмы заданного жанра;
- Сохраняет словарь в pickle-формате в файл с именем ИМЯ ЖАНРА.dat

Вызовите функцию в цикле для всех уникальных жанров.
Используйте set для получения уникального набора жанров.
'''


# импортируем словарь и библиотеки
from the_home_work_06_shows import shows
from functools import reduce
import os, pickle


# Создаем функцию для создания множества (списка сериалов)
def like_show(name):
    likes_show = set()
    for show in name:
        likes_show.add(show)
    return likes_show


# Используйте set для получения уникального набора жанров.
genre_set = set()
for x in shows.values():
    try:
        genre_set.add(x['Жанр'])
    except KeyError:
        genre_set.add(x['Genre'])


def genre_ratio(genre):
    ratio_list = []
    for i in shows.values():
        try:
            if i['Genre'] == genre:
                ratio_list.append(float(i['Rating']))
        except KeyError:
            if i['Жанр'] == genre:
                ratio_list.append(float(i['Рейтинг']))
    aver_ratio = round(reduce(lambda x, y: x + y, ratio_list)/len(ratio_list), 2)
    return f'В жанре {genre} - {len(ratio_list)} сериала, их средний рейтинг {aver_ratio}'


# Вызовите функцию в цикле для всех уникальных жанров.
for i in genre_set:
    print(genre_ratio(i))

print()



def genre_count_ratio(genre):
    ratio_list = []
    genre_shows_dict = dict()
    for show in shows.keys():
        try:
            if shows[show]['Genre'] == genre:
                ratio_list.append(float(shows[show]['Rating']))
                genre_shows_dict.update({show: shows[show]['Rating']})
        except KeyError:
            if shows[show]['Жанр'] == genre:
                ratio_list.append(float(shows[show]['Рейтинг']))
                genre_shows_dict.update({show: shows[show]['Рейтинг']})
    aver_ratio = round(reduce(lambda x, y: x + y, ratio_list)/len(ratio_list), 2)
    print(genre_shows_dict)
    return f'В жанре {genre} - {len(ratio_list)} сериала, их средний рейтинг {aver_ratio}'


# Вызовите функцию в цикле для всех уникальных жанров.
for i in genre_set:
    print(genre_count_ratio(i))