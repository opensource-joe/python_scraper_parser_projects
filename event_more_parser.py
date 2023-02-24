# scraper and parser for ACT-IAC events

import requests
from bs4 import BeautifulSoup

# ---------------------

url = "https://www.actiac.org/upcoming-events"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
# find all events on the page by event card with div and class
cards = soup.find_all('div', class_='cards-item non-sticky views-row')
# print(cards)

# count all events with cards on the page to manually check on webpage
# print(len(cards))

# ---------------------

# Learn More button - link to event page
# <a href="/act-iac-event/act-iac-health-coi-february-2023">Learn More</a>

event_more = [event_type_value.find_all('a') for event_type_value in cards]
print(event_more)

flat_list = [item for sublist in event_more for item in sublist]
print(flat_list)

event_more = []
for link in flat_list:
    event_more.append(f"https://www.actiac.org{link.get('href')}")