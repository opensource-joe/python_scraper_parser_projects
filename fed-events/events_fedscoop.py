# scraper and parser for FedScoop Events

import requests
from bs4 import BeautifulSoup

# ---------------------

url = "https://fedscoop.com/attend/"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
cards = soup.find_all('div', class_='events-page')[0]

# ---------------------

# featured event
# <section class="featured-event"></section>

cards_featured = cards.find_all('section', {'class', 'featured-event'})[0]

# ---

# featured event title
# <h2 class="featured-event__title">Cybersecurity Modernization Summit</h2>

featured_title = [cards_featured.find('h2').text]

# ---

# featured event date
# <p class="featured-event__date">Mar 2, 2023</p>

featured_date = [cards_featured.find('p', {'class', 'featured-event__date'}).text]

# ---

# featured event location
# <p class="featured-event__location">Virtual</p>

featured_location = [cards_featured.find('p', {'class', 'featured-event__location'}).text]

# ---

# learn more - register
# <a href="https://cybersecuritymodsummit.upgather.com/" target="_blank" class="featured-event__link button button-primary">Register</a>

featured_url = cards_featured.find_all('a')

featured_url_final = []
for link in featured_url:
    featured_url_final.append(link.get('href'))

# ---------------------

# upcoming events
# <section class="events-page_feed"></section>

cards_upcoming = cards.find_all('section', {'class', 'events-page__feed'})[0]

# ---

# event card title
# <a href="https://upgather.com/it-mod-talks-2" class="event-card__link" target="">IT Mod Talks</a>

upcoming_title = cards_upcoming.find_all('h3')

upcoming_title_final = []
for item in upcoming_title:
    upcoming_title_final.append(item.text.strip())

# ---

# event card date
# <p class="event-card__date">Mar 15, 2023</p>

upcoming_date = cards_upcoming.find_all('p', {'event-card__date'})

upcoming_date_final = []
for item in upcoming_date:
    upcoming_date_final.append(item.text)
    
# ---

# event card location
# <p class="event-card__location">Ritz-Carlton, Pentagon City</p>

upcoming_location = cards_upcoming.find_all('p', {'event-card__location'})

upcoming_location_final = []
for item in upcoming_location:
    upcoming_location_final.append(item.text)

# ---

# learn more - register (located w/ title)
# <p class="event-card__location">Ritz-Carlton, Pentagon City</p>

upcoming_url = cards_upcoming.find_all('a')
# print(upcoming_url)

upcoming_url_final = []
for link in upcoming_url:
    upcoming_url_final.append(link.get('href'))