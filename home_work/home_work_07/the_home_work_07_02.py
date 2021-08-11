'''
Вользите алгоритм пузырьковой сортировки из лекции.
Модифицируйте его так, чтобы сортировка производилась не по возрастанию, а по убыванию.
Отсортируйте список [19,2,31,45,6,11,121,27]
'''

def bubble_sort(arr):
    result = arr.copy()
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(result)-1):
            # Модифицируйте его так, чтобы сортировка производилась не по возрастанию, а по убыванию.
            if result[i] < result[i+1]:
                result[i], result[i+1] = result[i+1], result[i]
                swapped = True
    return result

array = [19, 2, 31, 45, 6, 11, 121, 27]

print(bubble_sort(array))