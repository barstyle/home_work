'''
В приложении к заданию находится рассказ “Кошки Ультара” Говарда Лавкрафта
(файл lesson05_cats_of_ulthar.txt). Напишите программу, которая:

- Открывает файл и считывает данные;
- Подсчитывает сколько раз в файле встречается слово “кошка” и выводит это число на экран; -
- Находит все строки, в которых встречается слово “кошка” и выводит эти строки на экран.
'''

filename = 'lesson05_cats_of_ulthar.txt'

with open(filename) as file:
    cat_word_list = []
    j = 0
    lines = file.read()
    new_lines = lines.replace('\n', '')
    line_list = new_lines.split('.')
    for line in line_list:
        for cat in line.split(' '):
            # если сделать if cat[0:3] == 'кош' - ,будет больше слов кошек
            if cat == 'кошка':
                j = j + 1
                cat_word_list.append(cat)
                print(str(j) + '-ая кошка -:', line, '\n')
    print(len(cat_word_list), '- раз встречается в этом тексте слово "кошка".')
file.close()

# на самом деле, кошка встречается чаще, но с другими склонениями
# кошке, кошку и даже кошачьи
