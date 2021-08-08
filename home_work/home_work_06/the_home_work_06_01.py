'''
В приложении к уроку задан словарь cериалов shows.
Напишите программу, которая считает средний рейтинг сериалов в словаре.
Используйте try except.
В процессе обработки вам встретятся исключения нескольких типов - обработайте каждый
тип исключений отдельным блоком except.
'''


# импортируем словарь aver_rait.append(round(float(i.setdefault(k)), 2))
from the_home_work_06_shows import shows

# создаем пустые множества, т.к. мы заметили, что не все ключи одинаковы
genre = set()
ratio = set()

# заполняем множества значениями ключей
for i in shows.values():
    x = [j for j in i.keys()]
    # массив жанр нам пока не понадобится, но вдруг в будущем нужен будет
    genre.add(x[0])
    ratio.add(x[1])

# проверяем все ли мы правильно заполнили
# print(genre, ratio)

# создаем пустой список, где будем хранить значения (рейтинг)
aver_rait = []

# заполняем наш пустой список, используя массив ratio, так мы подберем все значения
for i in shows.values():
    for j in i.keys():
        for k in ratio:
            if k == j:
                # используем трай, вдруг не получиться
                try:
                    aver_rait.append(round(i.setdefault(k)), 2)
                # если бы мы сразу использовали float, то получилось бы, но не было expect
                except TypeError:
                    aver_rait.append(round(float(i.setdefault(k)), 2))

# считаем среднее значения
aver = 0
for i in aver_rait:
    aver = aver + i
result = aver / len(aver_rait)

# выводим на экран
print(round(result, 2))