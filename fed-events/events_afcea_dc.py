# scraper and parser for AFCEA DC Events
# need to use updated HTML page b/c webpage is dynamic
# manual update to number of list items for title, date, and upcoming_url

from bs4 import BeautifulSoup

# ---------------------

open_file = open('fed-events/AFCEA-DC.html', 'r')
contents = open_file.read()

soup = BeautifulSoup(contents, 'html.parser')
cards = soup.find('div', {'class', 'field-item even'})

# print(cards)

# ---------------------

# event title

upcoming_title = cards.find_all('span')

upcoming_title_final = []
for item in upcoming_title[0:3]:
    upcoming_title_final.append(item.text.strip())

# ---

# event date

upcoming_date = cards.find_all('h4')

upcoming_date_final = []
for item in upcoming_date[0:5:2]:
    upcoming_date_final.append(item.text.strip())

# ---

# event learn more

upcoming_url = cards.find_all('a')

upcoming_url_inter = []
for link in upcoming_url:
    upcoming_url_inter.append(link.get('href'))

upcoming_url_final = upcoming_url_inter[1:3]