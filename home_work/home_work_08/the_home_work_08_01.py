'''
С помощью библиотек requests и bs4 прочитайте содержимое страницы
бесплатных игр на сайте Steam (https://store.steampowered.com/genre/Free%20to%20Play/)

Получите все ссылки (тег <a href = ‘...’>), для каждой ссылки получите текст ссылки и url.
Сформируйте словарь, состоящий только из тех ссылок,
у которых в тексте встречается фраза “Free To Play”.

Выведите словарь на экран.
'''

import requests
from bs4 import BeautifulSoup

# С помощью библиотек requests прочитайте содержимое страницы
r = requests.get('https://store.steampowered.com/genre/Free%20to%20Play/')
content = r.text

# С помощью библиотек bs4 прочитайте содержимое страницы
soup = BeautifulSoup(content, 'html.parser')

# создаем словарь - пока пустой
free_to_play_dict = dict()

# находим все ссылки
tag_free_to_play = soup.find_all('a')
# Перебираем все разделы с тегом "а"
for i in tag_free_to_play:
    # и где встречается нужный нам текст
    if 'Free To Play' in i.text:
        # добавляем в словарь
        free_to_play_dict[i.find(class_='tab_item_name').text] = i.get('href')

# выводим словарь на экран
for i in free_to_play_dict:
    print(i, '-', free_to_play_dict[i])