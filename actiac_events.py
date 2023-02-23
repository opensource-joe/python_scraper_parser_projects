# scraper and parser for ACT-IAC events

import requests
from bs4 import BeautifulSoup
import csv

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

# type of event - COI, Conference, FIE, Small Biz Alliance, Pro Dev
# <img alt="" src="/sites/default/files/community_of_interest.png">

for card in cards:
    event_type = card.find('img')
    # event_format = getattr(card.find('strong'), 'text', None)
    # print(event_type)
    # print(event_format)

# TODO: figure out how to iterate to only get image name and produce as text for excel

# ---------------------

# event format - virtual, in-person, in-person and virtual, unknown, multi-day event
# <strong>Virtual Event</strong>

# for card in cards:
    # event_format = getattr(card.find('strong'), 'text', None)
    # print(event_format)

event_format = [getattr(event.find('strong'), 'text', None) for event in cards]
# print(event_format)

# excel code

header = ['Event_Type', 'Event_Format', 'Event_Title', 'Event_Date', 'Description', 'Learn More']

with open('test1.csv', 'w') as test:
    events = csv.writer(test, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

    events.writerow(header)
    events.writerow(event_format)

test.close()