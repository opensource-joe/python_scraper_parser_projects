# scraper and parser for ACT-IAC Projects

import requests
from bs4 import BeautifulSoup

# ---------------------

url = "https://www.actiac.org/recent-projects-and-activities-0"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
# cards = soup.find_all('div', {'class': 'views-row'})[0]
# post_cards = cards.find_all('div', {'class', 'views-row'})




# ---------------------

# COI title, only need text, href controls accordion effect
# <a href="/groups/acquisition-community-interest" hreflang="en">Acquisition Community of Interest</a>

# coi_title = [getattr(title.find('a'), 'text', None) for title in post_cards]
