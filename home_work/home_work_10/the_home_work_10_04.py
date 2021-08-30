'''В приложении заданы словари сериалов shows и ratings.
С помощью dict comprehension сформируйте их этих двух словарей новый словарь,
содержащий полную информацию о сериалах. То есть ваш словарь должен выглядеть
примерно вот так: {'Секретные материалы': {'Жанр': 'фантастика', 'Рейтинг': 0.9}, … }'''

from bd_for_hw_10 import shows, ratings

full_dict_shows = {show: {'Жанр': shows[show], 'Рейтинг': ratings[show]} for show in shows}
print(full_dict_shows)