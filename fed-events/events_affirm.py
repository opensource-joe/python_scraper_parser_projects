# scraper and parser for AFFIRM Events
# manual update to number of list items for title

import requests
from bs4 import BeautifulSoup

# ---------------------

url = "https://members.affirm.org/event-calendar"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
cards = soup.find('div', {'class', 'row gz-cards gz-events-cards'})

# ---------------------------------------------

# event title

upcoming_title = cards.find_all('a')

upcoming_title_final = []
for item in upcoming_title[1::3]:
    upcoming_title_final.append(item.text.strip())

# ---

# event date

# ['WED', 'TUE']
event_week_day = cards.find_all('span', {'class', 'gz-card-wkday'})
event_week_day_final = []
for week_day in event_week_day:
    event_week_day_final.append(week_day.text)

# ['19', '25']
event_day = cards.find_all('span', {'class', 'gz-start-dy'})
event_day_final = []
for day in event_day:
    event_day_final.append(day.text)

# ['April', 'May']
event_month = cards.find_all('span', {'class', 'gz-start-dt'})
event_month_final = []
for month in event_month:
    event_month_final.append(month.text)

date_combined = []
for wk_day, month, num_day in zip(event_week_day_final, event_month_final, event_day_final):
    date_combined.append([wk_day.title(), month, num_day])

upcoming_date_final = [''.join(l) for l in date_combined]

# ---

# description

event_description = cards.find_all('p')

upcoming_description_final = []
for item in event_description:
    upcoming_description_final.append(item.text.strip())
    
# ---

# learn more

upcoming_url = cards.find_all('div', {'class', 'card-footer'})

upcoming_url_inter = [link.find_all('a') for link in upcoming_url]
flat_upcoming_url = [item for sublist in upcoming_url_inter for item in sublist]

upcoming_url_final = []
for link in flat_upcoming_url:
    upcoming_url_final.append(link.get('href'))