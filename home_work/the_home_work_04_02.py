'''
Ане нравятся сериалы “Секретные материалы”, “Карточный домик” и “Рик и Морти”.
На новой работе у Ани появилось три новых подруги - Оля, Настя и Света.
С помощью множеств (set) найдите, с кем из них у Ани больше всего общих любимых сериалов
'''

# Импортируем необходимые словари для выполнения задачи
from bd_for_hw_04 import anya, olya, nastya, sveta


# Созадем функцию для создания множества (списка сериалов)
def like_show(name):
    likes_show = set()
    for show in name:
        likes_show.add(show)
    return likes_show


# Функиця для кол-ва сравнений во множествах
def diff(name_01, name_02):
    result = like_show(name_01).intersection(like_show(name_02))
    return len(result)


# Сравниваем кол-во совпадений
if diff(anya, olya) > diff(anya, nastya) and diff(anya, olya) > diff(anya, sveta):
    print('У Ани и Оли больше совпадений')
elif diff(anya, nastya) > diff(anya, olya) and diff(anya, nastya) > diff(anya, sveta):
    print('У Ани и Насти больше совпадений')
else:
    print('У Ани и Светы больше совпадений')