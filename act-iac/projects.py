# scraper and parser for ACT-IAC Projects

import requests
from bs4 import BeautifulSoup

# ---------------------

url = "https://www.actiac.org/recent-projects-and-activities-0"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
cards = soup.find_all('div', {'class': 'view-content row'})[0]

# ---------------------

# find card title for seeking volunteers

cards_lev2 = cards.find_all('div', {'class', 'views-row'})[0]

# seek_cards = cards_lev2.find_all('span', {'field-content'})
# seek_cards = [getattr(title.find('span'), 'text', None) for title in cards_lev2]

for card in cards_lev2:
    print(card)


# find card title for in progress


# ---------------------

# COI title, only need text, href controls accordion effect
# <a href="/groups/acquisition-community-interest" hreflang="en">Acquisition Community of Interest</a>

# coi_title = [getattr(title.find('a'), 'text', None) for title in post_cards]
