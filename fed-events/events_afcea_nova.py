# scraper and parser for AFCEA Nova Events
# need to use updated HTML page b/c webpage is dynamic

import re
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

# event date - using regex w/ import re

pattern = "\d{2}[/-]\d{2}[/-]\d{4}"
dates = re.findall(pattern, contents)

# ---

# event learn more

upcoming_url = cards.find_all('a')

upcoming_url_final = []
for link in upcoming_url:
    upcoming_url_final.append(link.get('href'))