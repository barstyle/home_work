'''
В приложении к уроку задан словарь cериалов shows.
Напишите программу, которая считает средний рейтинг сериалов в словаре.
Используйте try except.
В процессе обработки вам встретятся исключения нескольких типов - обработайте каждый
тип исключений отдельным блоком except.
'''
# импортируем словарь
from the_home_work_06_shows import shows

genre = set()
ratio = set()
for i in shows.values():
    x = [j for j in i.keys()]
    genre.add(x[0])
    ratio.add(x[1])

print(genre, ratio)

aver_rait = []

for i in shows.values():
    for j in i.keys():
        for k in ratio:
            if k == j:
                aver_rait.append(round(float(i.setdefault(k)), 2))

aver = 0
for i in aver_rait:
    aver = aver + i

result = aver / len(aver_rait)

print(round(result, 2))