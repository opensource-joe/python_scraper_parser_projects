# original scraper and parser for ACT-IAC events (can be deleted once new scraper and parser is running)

import requests
from bs4 import BeautifulSoup

# ---------------------

url = "https://www.actiac.org/upcoming-events"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
# find all events on the page by event card with div and class
cards = soup.find_all('div', class_='cards-item non-sticky views-row')
print(cards)

# count all events with cards on the page to manually check on webpage
# print(len(cards))

# ---------------------

# type of event - COI, Conference, FIE, Small Biz Alliance, Pro Dev
# <img alt="" src="/sites/default/files/community_of_interest.png">

# event_type = [event_type_value.find_all('img') for event_type_value in cards]
# print(event_type)

# jobs = cards[0].find('img')
# string_jobs = str(jobs)

# if string_jobs == '<img alt="" src="/sites/default/files/federal_insights_exchange2.png"/>':
#     print("Federal Insights Exchange (FIE)")
# elif string_jobs == '<img alt="" src="/sites/default/files/Small%20Business%20Alliance.png"/>':
#     print("Small Business Alliance")
# elif string_jobs == '<img alt="" src="/sites/default/files/community_of_interest.png"/>':
#     print("Community of Interest (COI)")
# elif string_jobs == '<img alt="" src="/sites/default/files/professional_development.png"/>':
#     print("Professional Development")
# elif string_jobs == '<img alt="" src="/sites/default/files/conferences_0.png"/>':
#     print("Conference")
# else:
#     print("Type of Event TBD")

# ---------------------

# event format - virtual, in-person, in-person and virtual, unknown, multi-day event
# <strong>Virtual Event</strong>

# event_format = [event_format_value.find('strong') for event_format_value in cards]
# print(event_format)    

# ---------------------

# event title - like "ACT-IAC Health COI February 2023"
# <h4>ACT-IAC Health COI February 2023</h4>

# event_title = [event_title_value.find('h4') for event_title_value in cards]
# print(event_title)

# ---------------------

# event date - like "Tuesday, February 21, 2023"
# <time datetime="00Z" class="datetime">Tuesday, February 21, 2023</time>

# event_date = [event_date_value.find('time') for event_date_value in cards]
# print(event_date)

# ---------------------

# event description
# <p>Join the ACT-IAC Health COI meeting to hear from...</p>

# event_description = [event_description_value.find('p') for event_description_value in cards]
# print(event_description)

# ---------------------

# Learn More button - link to event page
# <a href="/act-iac-event/act-iac-health-coi-february-2023">Learn More</a>

# event_more = [event_more_value.find('a') for event_more_value in cards]
# print(event_more)