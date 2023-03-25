# scraper and parser for NextGov Events

import requests
from bs4 import BeautifulSoup

# ---------------------

url = "https://www.nextgov.com/events"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
cards = soup.find_all('div', {'class', 'river-items row'})[0]

# ---------------------

# upcoming event name
upcoming_title = cards.find_all('h1')

upcoming_title_final = []
for item in upcoming_title:
    upcoming_title_final.append(item.text.strip())

# ---

# # upcoming event date
upcoming_date = cards('p', {'class', 'river-item-dek'})

upcoming_date_final = []
for item in upcoming_date:
    upcoming_date_final.append(item.text)

# ---

# upcoming event location - if event digital, only date is provided in list and not a real location
upcoming_location = cards.find_all('p', {'class', 'river-item-label river-item-inset'})

upcoming_location_final = [getattr(event.find('span'), 'text', None) for event in upcoming_location]

# ---

# upcoming learn more
upcoming_url = cards.find_all('a', {'class': 'river-item-title-link hover-group-member'})

upcoming_url_final = []
for link in upcoming_url:
    upcoming_url_final.append(link.get('href'))