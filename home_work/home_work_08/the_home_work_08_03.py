'''
На этой же странице найдите и обработайте таблицу игр:
Используйте функцию Inspect Element в вашем браузере,
чтобы понять, какие теги и классы вам нужно обрабатывать.
Составьте и распечатайте словарь игр и их тегов. Например,
{'Incremental Epic Breakers': ['2D Platformer', ', Puzzle Platformer', ', Idler', ', Destruction'], … }
'''

import requests
from bs4 import BeautifulSoup

# С помощью библиотек requests прочитайте содержимое страницы
r = requests.get('https://store.steampowered.com/genre/Free%20to%20Play/')
content = r.text

# С помощью библиотек bs4 прочитайте содержимое страницы
soup = BeautifulSoup(content, 'html.parser')

# создаем словарь - пока пустой
tab_item_dict = dict()

# находим все из блока
app_item = soup.find_all(class_='tab_item')

# Перебираем все разделы с тегом "tab_item"
for i in app_item:
    tag_list = list()
    for j in i.find_all(class_='top_tag'):
        if j.text[0:2] == ', ':
            tag_list.append(j.text[2:])
        else:
            tag_list.append(j.text)
    tab_item_dict[i.find(class_='tab_item_name').text] = tag_list

# выводим словарь на экран
for i in tab_item_dict:
    print(i, '-', tab_item_dict[i])