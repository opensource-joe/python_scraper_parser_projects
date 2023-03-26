# scraper and parser for ATARC Events

import requests
from bs4 import BeautifulSoup

# ---------------------

url = "https://atarc.org/events/"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
cards = soup.find('div', {'class', 'tribe-events-calendar-list'})

# ---------------------------------------------

# event title

upcoming_title = cards.find_all('a')

upcoming_title_final = []
for item in upcoming_title:
    upcoming_title_final.append(item.text.strip())

# ---

# event date & time

upcoming_date = cards.find_all('span', {'class', 'tribe-event-date-start'})

upcoming_date_final = []
for item in upcoming_date:
    upcoming_date_final.append(item.text)

# ---

# location

upcoming_location = cards.find_all('span', {'class', 'tribe-events-calendar-list__event-venue-title tribe-common-b2--bold'})

upcoming_location_final = []
for item in upcoming_location:
    upcoming_location_final.append(item.text.strip())

# ---

# description

event_description = cards.find_all('p')

# print(event_description)

upcoming_description_final = []
for item in event_description:
    upcoming_description_final.append(item.text.strip())

# ---

# learn more

upcoming_url = cards.find_all('a')

upcoming_url_final = []
for link in upcoming_url:
    upcoming_url_final.append(link.get('href'))