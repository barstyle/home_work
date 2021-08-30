'''С помощью filter и регулярных выражений выберите из списка animals только тех животных,
у которых название начинается с букв “к” или “л”.
Проделайте то же самое с помощью list comprehension и регулярных выражений.
Напечатайте результаты.'''
import re
from bd_for_hw_10 import animals

# С помощью filter и регулярных выражений выберите из списка animals только тех животных,
# у которых название начинается с букв “к” или “л”.
filter_animals = list(filter(lambda word: re.search('^к.+|^л.+', word), animals))
print(filter_animals)

# Проделайте то же самое с помощью list comprehension и регулярных выражений.
filter_animals_list = [word for word in animals if re.search('^к.+|^л.+', word)]
print(filter_animals_list)