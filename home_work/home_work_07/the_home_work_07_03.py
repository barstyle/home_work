'''
В приложении задана функция сортировки выбором, которая сортирует список и возвращаем время,
затраченное на сортировку.

Исследуйте, как увеличение размера сортируемого списка влияет на скорость сортировки.

Возьмите вот такие размеры списка: 1 000, 2 000, 5 000, 10 000

Напишите цикл, в котором перебираются размеры списков. Для каждого размера:
- Генерируется список нужной длины, заполненный случайными целыми числами;
- Полученный список сортируется функцией selection_sort;
- Печатается размер списка и время сортировки.

Какой вывод вы можете сделать по результатам работы программы? Добавьте вывод в комментарий к программе.
'''
import random, time


# функция из приложения
def selection_sort(input_list):
    start_time = time.time() # время старта функции
    for i in range(len(input_list)):
        min_i = i
        for j in range(i + 1, len(input_list)):
            if input_list[min_i] > input_list[j]: min_i = j
        input_list[i], input_list[min_i] = input_list[min_i], input_list[i]
    return time.time() - start_time # время выполнения в секундах

# Генерируется список нужной длины, заполненный случайными целыми числами;
def as_list(n):
    asist = [x for x in range(n)]
    random.shuffle(asist)
    return asist


# - Печатается размер списка и время сортировки.
for i in [1000, 2000, 5000, 10000]:
    print(f'размер списка равен - {i}, время сортировки равно - {selection_sort(as_list(i))}')

"""
Вывод:
- Размер увеличения объема списка не прямо пропорционален увеличению времени на его обработку.
Объем списка может увеличится в два раза, а время на его сортировку в 4 раза. 
- При небольших списках - можно не заметить, что алгоритм выбран ресурсо-затратный.
- Выбирая алгоритм для обработки данных, нужно опираться на результаты тестов.
- надо учить мехмат?
"""