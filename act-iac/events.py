# scraper and parser for ACT-IAC Events

import requests
from bs4 import BeautifulSoup

# ---------------------

url = "https://www.actiac.org/upcoming-events"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
cards = soup.find_all('div', class_='cards-item non-sticky views-row')

# count all events with cards on the page to manually check on webpage
# print(len(cards))

# ---------------------

# type of event - COI, Conference, FIE, Small Biz Alliance, Pro Dev
# <img alt="" src="/sites/default/files/community_of_interest.png">

# loop for finding all 'img' tags within the cards class noted above
event_type = [event_type_value.find_all('img') for event_type_value in cards]

# flatten the list of lists created by above event_type loop
flat_list = [item for sublist in event_type for item in sublist]

# creating new list with output values from iterations
event_type = []
for item in flat_list:
    if str(item) == '<img alt="" src="/sites/default/files/federal_insights_exchange2.png"/>':
        event_type.append("Federal Insights Exchange")
    elif str(item) == '<img alt="" src="/sites/default/files/Small%20Business%20Alliance.png"/>':
        event_type.append("Small Business Alliance")
    elif str(item) == '<img alt="" src="/sites/default/files/community_of_interest.png"/>':
        event_type.append("Community of Interest (COI)")
    elif str(item) == '<img alt="" src="/sites/default/files/professional_development.png"/>':
        event_type.append("Professional Development")
    elif str(item) == '<img alt="" src="/sites/default/files/conferences_0.png"/>':
        event_type.append("Conference")
    else:
        event_type.append("Type of Event TBD")

# ---------------------

# event format - virtual, in-person, in-person and virtual, unknown, multi-day event
# <strong>Virtual Event</strong>

event_format = [getattr(event.find('strong'), 'text', None) for event in cards]

# ---------------------

# event title - like "ACT-IAC Health COI February 2023"
# <h4>ACT-IAC Health COI February 2023</h4>

event_title = [getattr(event.find('h4'), 'text', None) for event in cards]

# ---------------------

# event date - like "Tuesday, February 21, 2023"
# <time datetime="00Z" class="datetime">Tuesday, February 21, 2023</time>

event_date = [getattr(event.find('time'), 'text', None) for event in cards]

# ---------------------

# event description
# <p>Join the ACT-IAC Health COI meeting to hear from...</p>

event_description = [getattr(event.find('p'), 'text', None) for event in cards]

# ---------------------

# Learn More button - link to event page
# <a href="/act-iac-event/act-iac-health-coi-february-2023">Learn More</a>

event_more = []
for card in cards:
    if card.find('a') == None:
        event_more.append('TBD')
    else: 
        event_more.append(card.find('a'))

event_more_2 = []
for link in event_more:
    if link == "TBD":
        event_more_2.append("TBD")
    else:
        event_more_2.append(f"https://www.actiac.org" + link.get('href'))