'''
В свободное от работы время Вася очень любит смотреть сериалы.
Васе не нравится фэнтази и он принципиально не смотрит фильмы с рейтингом ниже 0.85.

Напишите рекомендательную систему, которая:
- Берет данные о сериалах из словарей shows и ratings;
- Выбирает случайный сериал и проверяет подходит ли он Васе;
- Предлагает Васе посмотреть подходящий сериал и, если Вася не согласен,
то выбирает следующий.

Используйте while, continue, break.
'''
# импортируем билиотеку великого рандома
import random

# импортируем словари
from bd_for_hw_04 import shows, ratings

# создаем пустой список, в котором будем хранить сериалы подхлдящие для Васи
shows_for_vasya = []

# генерируем этот список
for film in shows:
    if shows.setdefault(film) != 'фэнтази' and ratings.setdefault(film) > 0.85:
        shows_for_vasya.append(film)

# функция подбирает случайный сериал подходящий Васе
def is_what_show():
    i = random.randint(0, len(shows_for_vasya)-1)
    show = shows_for_vasya[i]
    return show

will = True

while will:
    show = is_what_show()
    print('Хотите посмотреть - {}?'
          '\nЕго рейтинг - {}'.format(show, ratings.setdefault(show)))
    click = input('Если хотите продолжить подборку, нажмите - "Y"'
                  '\nЕсли хотите остановть подборку, нажмите любую дргую кнопку: ')
    if click.lower() == 'y':
        print('')
        continue
    else:
        break