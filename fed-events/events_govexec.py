# scraper and parser for GovExec Events

import requests
from bs4 import BeautifulSoup

# ---------------------

url = "https://www.govexec.com/events/"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
cards = soup.find_all('div', {'class', 'l-right-rail-side-companion lander-event-container'})[0]

# ---------------------

# featured event
featured_card = cards.find('div', {'class', 'l-spacing-3rem-up'})

# ---

# featured event name
featured_title = [featured_card.find('h1').text.strip()]

# ---

# featured event date
featured_date = [featured_card.find('p', {'class', 'feature-story-description'}).text]

# ---

# featured event location
featured_location = [featured_card.find('span').text]

# ---

# featured learn more
featured_url = [featured_card.find('h1', {'class', 'feature-story-hed'})][0]

featured_url_final = []
for link in featured_url.find_all('a', href=True):
    featured_url_final.append(link['href'])
    
# ---------------------

# upcoming event
upcoming_card = cards.find('div', {'class', 'river-items row'})

# ---

# upcoming event name
upcoming_title = upcoming_card.find_all('h1')

upcoming_title_final = []
for item in upcoming_title:
    upcoming_title_final.append(item.text.strip())

# ---

# upcoming event date
upcoming_date = upcoming_card.find_all('p', {'class', 'river-item-dek'})

upcoming_date_final = []
for item in upcoming_date:
    upcoming_date_final.append(item.text)

# ---

# upcoming event location - if event digital, only date is provided in list and not a real location
upcoming_location = upcoming_card.find_all('p', {'class', 'river-item-label river-item-inset'})

upcoming_location_final = [getattr(event.find('span'), 'text', None) for event in upcoming_location]

# ---

# upcoming learn more
upcoming_url = upcoming_card.find_all('a', {'class': 'river-item-title-link hover-group-member'})

upcoming_url_final = []
for link in upcoming_url:
    upcoming_url_final.append(link.get('href'))