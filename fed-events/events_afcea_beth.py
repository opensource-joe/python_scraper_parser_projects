# scraper and parser for AFCEA Bethesda Events
# manual update to number of list items for title

import requests
from bs4 import BeautifulSoup

# ---------------------

url = "https://bethesda.afceachapters.org/events/"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
cards = soup.find('div', {'class', 'tribe-events-calendar-list'})

# ---------------------

# event title

upcoming_title = cards.find_all('a')

upcoming_title_final = []
for item in upcoming_title[1::3]:
    upcoming_title_final.append(item.text.strip())

# ---

# event date

upcoming_date = cards.find_all('span', {'class', 'tribe-event-date-start'})

upcoming_date_final = []
for item in upcoming_date:
    upcoming_date_final.append(item.text)

# ---

# event learn more

upcoming_url = cards.find_all('div', {'class', 'iron-tribe-event-link'})

upcoming_url_inter = [link.find_all('a') for link in upcoming_url]
flat_upcoming_url = [item for sublist in upcoming_url_inter for item in sublist]

upcoming_url_final = []
for link in flat_upcoming_url:
    upcoming_url_final.append(link.get('href'))