'''
В приложении к уроку задан список имен животных animals.
Модифицируйте алгоритм линейного поиска таким образом,
чтобы он находил все индексы указанного слова и возвращал список индексов.
Например, для слова ‘жираф’ функция должна вернуть список [10, 12, 13, 16, 17, 19, 24, 26, 31, 38, 41]
Вызовите получившуюся функцию для всех уникальных имен животных.
'''

from animals import animals


# функция для поиска индекса в списке
def search_index(animal):
    an_list = list()
    for i in range(len(animals)):
        if animals[i] == animal:
            an_list.append(i)
    return an_list


# создаем множество с уникальными именами животных
animals_set = set()
for name in animals:
    animals_set.add(name)

# вызовите получившуюся функцию для всех уникальных имен животных
for nik in animals_set:
    print(nik, '-', search_index(nik))