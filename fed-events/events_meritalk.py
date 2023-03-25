# scraper and parser for Meritalk Events

import requests
from bs4 import BeautifulSoup

# ---------------------

url = "https://www.meritalk.com/events/"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
cards = soup.find_all('div', {'class', 'wpb_wrapper'})[7]

# ---------------------

upcoming_title = cards.find_all('a')

upcoming_title_final = []
for item in upcoming_title[0::2]:
    upcoming_title_final.append(item.text)

# ---

# upcoming event date
upcoming_date = cards('div', {'class', 'event-date'})

upcoming_date_final = []
for item in upcoming_date:
    upcoming_date_final.append(item.text)
    
# ---

# upcoming event description
upcoming_description = cards('div', {'class', 'event-excerpt'})

upcoming_description_final = [getattr(event.find('p'), 'text', None) for event in upcoming_description]

# ---

# upcoming learn more

upcoming_url_final = []
for link in upcoming_title[0::2]:
    upcoming_url_final.append(link.get('href'))