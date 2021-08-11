'''
Напишите программу, которая находит в текущей папке все файлы типа *.dat,
поочередно считывает и выводит на экран их содержимое.
'''

import os
import pickle


# находим файл
for file in os.listdir():
    if file.endswith('.dat'):
        print(file)
        # читаем содержимое
        with open(file, 'rb') as rf:
            content = pickle.load(rf)
            for i in content:
                print(i, '-', content[i])
        print()