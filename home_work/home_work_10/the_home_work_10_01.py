'''В приложении к уроку дан список имен животных animals.
С помощью map трансформируйте его в список, в котором лежат длины строк имен животных.
Например animals = ['питон', 'питон', … ] трансформируется в [5, 5, …].
Проделайте эту же операцию с помощью list comprehension.
Напечатайте результаты.'''

from bd_for_hw_10 import animals

# С помощью map трансформируйте его в список
result_map = list(map(len, animals))
print(result_map)

# Проделайте эту же операцию с помощью list comprehension
result_list = [len(i) for i in animals]
print(result_list)