# scraper and parser for ACT-IAC events

import requests
from bs4 import BeautifulSoup
# csv

url = "https://www.actiac.org/upcoming-events"
response = requests.get(url)

soup = BeautifulSoup(response.content, features='html.parser')

# find all events on the page by event card with div and class
css_class_card = soup.findAll('div', class_='cards-item non-sticky views-row')
# print(css_class_card)

# TODO: use class closest to text element to make sure it pulls correct text (e.g., div class="cards-description" then "p")

# count all events with cards on the page to manually check on webpage
# print(len(css_class_card))

# parse content bits for csv export

# type of event - COI, Conference, FIE, Small Biz Alliance, Pro Dev
# <img alt="" src="/sites/default/files/community_of_interest.png">

# event_type = css_class_card[0].find('span', class_='field_content', html_='img')
# event_type = css_class_card[0].find('img')
# print(event_type)
# TODO: get event_type from URL, format as needed for excel file
# TODO: loop for all cards

# event format - virtual, in-person, in-person and virtual, unknown, multi-day event
# <strong>Virtual Event</strong>

event_format = css_class_card[0].find('strong')
event_text_only = event_format.text
print(event_text_only)
# TODO: loop for all cards

# event title - like "ACT-IAC Health COI February 2023"
# <h4>ACT-IAC Health COI February 2023</h4>

event_title = css_class_card[0].find('h4')
event_title_only = event_title.text
print(event_title_only)
# TODO: loop for all cards

# event date - like "Tuesday, February 21, 2023"
# <time datetime="00Z" class="datetime">Tuesday, February 21, 2023</time>

event_date = css_class_card[0].find('time')
event_date_only = event_date.text
print(event_date_only)
# TODO: loop for all cards

# event description
# <p>Join the ACT-IAC Health COI meeting to hear from...</p>

event_description = css_class_card[0].find('p')
event_description_only = event_description.text
print(event_description_only)
# TODO: loop for all cards

# Learn More button - link to event page
# <a href="/act-iac-event/act-iac-health-coi-february-2023">Learn More</a>

event_more = css_class_card[0].find('a')
print(event_more)
# event_more_only = event_more.text
# print(event_more_only)
# TODO: determine how to strip URLs from an href
# TODO: loop for all cards

# TODO: write to csv, format text as needed