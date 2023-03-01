# scraper and parser for ACT-IAC Projects

import requests
from bs4 import BeautifulSoup

# ---------------------

url = "https://www.actiac.org/recent-projects-and-activities-0"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
cards = soup.find_all('div', {'class': 'view-content row'})[0]

# ---------------------

# Seeking Volunteers

cards_lev2 = cards.find_all('div', {'class', 'views-row'})[0]
cards_lev3 = cards_lev2.find_all('div', {'class', 'views-row'})

# header
accord_group_seek = [cards_lev2.find('h3').text]

# card title
card_title = [getattr(title.find('span'), 'text', None) for title in cards_lev3]

# click to learn more

cards_link = cards_lev2.find_all('a')

card_link_prep = []
for a in cards_link:
    if 'https' in str(a):
        card_link_prep.append("invalid_link")
    else:
        card_link_prep.append(a)

card_link_final = []
for link in card_link_prep:
    if link != "invalid_link":
        card_link_final.append(f"https://www.actiac.org" + link.get('href'))

# ---------------------

# In Progress

# bumping up variable to 10th to capture all In Progress cards
cards_lev10 = cards.find_all('div', {'class', 'views-row'})[4]
cards_lev11 = cards_lev10.find_all('div', {'class', 'views-row'})

# header

accord_group_prog = [cards_lev10.find('h3').text]

# card title

card_title_prog = [getattr(title.find('span'), 'text', None) for title in cards_lev11]

# click to learn more

cards_link_prog = cards_lev10.find_all('a')

card_link_prep_prog = []
for a in cards_link_prog:
    if 'https' in str(a):
        card_link_prep_prog.append("invalid_link")
    else:
        card_link_prep_prog.append(a)

card_link_prog_final = []
for link in card_link_prep_prog:
    if link != "invalid_link":
        card_link_prog_final.append(f"https://www.actiac.org" + link.get('href'))