# scraper and parser for ACT-IAC events

import requests
from bs4 import BeautifulSoup
import xlsxwriter

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

# event_more = [event_more_value.find('a') for event_more_value in cards]
# print(event_more)

# TODO: parse out URL, maybe alias to spreadsheet value (e.g., Link)

# ---------------------

# xlsxwriter output

workbook = xlsxwriter.Workbook('ACT-IAC_Events.xlsx')
worksheet = workbook.add_worksheet()

header = ['Event_Type', 'Event_Format', 'Event_Title', 'Event_Date', 'Description', 'Learn More']

worksheet.write_row('A1', header)
worksheet.write_column('A2', event_type)
worksheet.write_column('B2', event_format)
worksheet.write_column('C2', event_title)
worksheet.write_column('D2', event_date)
worksheet.write_column('E2', event_description)
# TODO: add event_more in 'F2'

workbook.close()