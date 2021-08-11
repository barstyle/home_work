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
import pickle


# Используйте set для получения уникального набора жанров.
genre_set = set()
for x in shows.values():
    try:
        genre_set.add(x['Жанр'])
    except KeyError:
        genre_set.add(x['Genre'])

# Создаем функцию которая делает из списка на верху)
def genre_count_ratio(genre):
    ratio_list = []
    genre_shows_dict = dict()
    data_file_name = genre + '.dat'
    for show in shows.keys():
        try:
            if shows[show]['Genre'] == genre:
                ratio_list.append(float(shows[show]['Rating']))
                # Создает словарь, содержащий только фильмы заданного жанра + рейтинг
                genre_shows_dict.update({show: shows[show]['Rating']})
        except KeyError:
            if shows[show]['Жанр'] == genre:
                ratio_list.append(float(shows[show]['Рейтинг']))
                # Создает словарь, содержащий только фильмы заданного жанра + рейтинг
                genre_shows_dict.update({show: shows[show]['Рейтинг']})

    # Сохраняет словарь в pickle-формате в файл с именем ИМЯ ЖАНРА.dat
    data = genre_shows_dict
    file = open(data_file_name, 'wb')
    pickle.dump(data, file)
    file.close()

    # Это вообще законно?
    aver_ratio = round(reduce(lambda x, y: x + y, ratio_list)/len(ratio_list), 2)

    return f'В жанре {genre} - {len(ratio_list)} сериала, их средний рейтинг {aver_ratio}'


# Вызовите функцию в цикле для всех уникальных жанров.
for i in genre_set:
    print(genre_count_ratio(i))