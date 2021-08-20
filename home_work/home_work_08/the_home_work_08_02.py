'''
На этой же странице, с помощью equests и bs4 найдите и обработайте раздел тегов:
Сформируйте словарь, в котором ключами будут имена тегов, а значениями - количества игр,
относящихся к этим тегам. Например: {‘Indie’: 2355, … }
Обратите внимание, что теги можно найти вот по такому bs-запросу:
.find_all('div', class_ = 'tag_count_button')
'''

import requests
from bs4 import BeautifulSoup

# С помощью библиотек requests прочитайте содержимое страницы
r = requests.get('https://store.steampowered.com/genre/Free%20to%20Play/')
content = r.text

# С помощью библиотек bs4 прочитайте содержимое страницы
soup = BeautifulSoup(content, 'html.parser')

# создаем словарь - пока пустой
narrow_by_tag = dict()

# находим все тэги
narrow_tag = soup.find_all(class_='tag_count_button')
# Перебираем все разделы с этим тегом
for i in narrow_tag:
    # добавляем в словарь
    narrow_by_tag[i.find(class_='tag_name').text] = i.find(class_='tag_count tab_filter_control_count').text

# выводим словарь на экран
for i in narrow_by_tag:
    print(i, '-', narrow_by_tag[i])