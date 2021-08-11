'''
В предыдущий пример добавьте любой другой алгоритм сортировки.
Сравните время его работы с selection_sort. Напишите выводы.
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

print('Выборочная сортировка:')
# - Печатается размер списка и время сортировки.
for i in [1000, 2000, 5000, 10000]:
    print(f'размер списка - {i}, время сортировки - {selection_sort(as_list(i))} сек.')


def bubble_sort(arr):
    start_time = time.time()
    result = arr.copy()
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(result)-1):
            if result[i] > result[i+1]:
                result[i], result[i+1] = result[i+1], result[i]
                swapped = True
    return time.time() - start_time


print('\nПузырьковая сортировка:')

# - Печатается размер списка и время сортировки.
for i in [1000, 2000, 5000, 10000]:
    print(f'размер списка - {i}, время сортировки - {bubble_sort(as_list(i))} сек.')


def dea_sort(array):
    start_time = time.time()
    sorted(array)
    return time.time() - start_time


print('\nСортировка из коробки:')

# - Печатается размер списка и время сортировки.
for i in [1000, 2000, 5000, 10000]:
    print(f'размер списка - {i}, время сортировки - {dea_sort(as_list(i))} сек.')

'''
Выводы:
- Сортировка из коробки в данном кейсе самая быстрая, возможно потому заточена на такую)
- Пузырьковая уступает выборочной
- 
'''