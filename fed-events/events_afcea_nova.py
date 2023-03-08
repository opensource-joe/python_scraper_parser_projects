# scraper and parser for ACT-IAC Events

from bs4 import BeautifulSoup

# ---------------------

open_file = open('fed-events/AFCEA-NOVA.html', 'r')
contents = open_file.read()

soup = BeautifulSoup(contents, 'html.parser')
cards = soup.find('div', {'class', 'field-items'})

# print(cards)

# ---------------------

# event title

upcoming_title = cards.find_all('a')

upcoming_title_final = []
for item in upcoming_title:
    upcoming_title_final.append(item.text.strip())

# ---

# event date

# TODO: find a way to split string of text to parse out date


# ---

# event learn more

upcoming_url = cards.find_all('a')

upcoming_url_final = []
for link in upcoming_url:
    upcoming_url_final.append(link.get('href'))