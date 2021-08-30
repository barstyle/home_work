'''
Спомощью re и BeautifulSoup исследуйте страницу Википедии,
посвященную премии “Небьюла” (https://ru.wikipedia.org/wiki/Небьюла).
Соберите все ссылки на этой странице.
Отфильтруйте только те, которые не ведут на страницы Википедии.
'''
import re
import requests
from bs4 import BeautifulSoup

# С помощью библиотек requests прочитайте содержимое страницы
r = requests.get('https://ru.wikipedia.org/wiki/Небьюла')
content = r.text

# С помощью библиотек bs4 прочитайте содержимое страницы
soup = BeautifulSoup(content, 'html.parser')

# находим все ссылки с нужным классом
links = soup.find_all('a', "external text")
# Перебираем их
for i in links:
    # ссылки, которые ведут на вики не печатаем
    if re.search(r"\bwiki.+\b", str(i)):
        pass
    # печатаем только ссылки, которые ведут на внешние страницы
    else:
        print(i.text, '-', i.get('href'))