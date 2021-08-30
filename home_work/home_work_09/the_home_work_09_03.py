'''
В приложении к уроку задан файл lesson09_cats_of_ulthar.txt.
С помощью библиотеки re посчитайте сколько раз в нем встречается слово “кошка” в любой форме
'''
import re

filename = 'lesson09_cats_of_ulthar.txt'

with open(filename) as file:
    cat_word_list = []
    lines = file.read()
    for cat in lines.split():
        if re.search(r"\bкош.+\b", cat):
            cat_word_list.append(cat)
    print(len(cat_word_list), '- раз встречается в этом тексте слово "кошка" в любой форме.')


