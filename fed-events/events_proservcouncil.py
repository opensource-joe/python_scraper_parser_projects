# scraper and parser for PSC Events

import requests
from bs4 import BeautifulSoup

# ---------------------

url = "https://www.pscouncil.org/psc/Events"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
cards = soup.find('div', {'class', 'col-primary'})

# only provides first 15 of 39 events planned for the year
# need to check that old ones drop off and list updates each run
# first event is 5/14 - 2023 Strategic Planning Forum

# ---------------------

# event title
upcoming_title = cards.find_all('div', {'class', 'EventTitle'})

upcoming_title_final = []
for item in upcoming_title:
    upcoming_title_final.append(item.text)

# ---

# event date
upcoming_date = cards.find_all('div', {'class', 'EventDate'})

upcoming_date_final = []
for item in upcoming_date:
    upcoming_date_final.append(item.text)

# ---

# location
upcoming_location = cards.find_all('div', {'class', 'EventAdd2'})

upcoming_location_final = []
for item in upcoming_location:
    upcoming_location_final.append(item.text)


# ---

# learn more

upcoming_url = cards.find_all('div', {'class', 'EventButton'})

upcoming_url_inter = [link.find_all('a') for link in upcoming_url]
flat_upcoming_url = [item for sublist in upcoming_url_inter for item in sublist]

upcoming_url_final = []
for link in flat_upcoming_url:
    upcoming_url_final.append(f"https://pscouncil.org" + link.get('href'))