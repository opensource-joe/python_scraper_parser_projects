# test scraper

import requests
from bs4 import BeautifulSoup

# create connection to URL for scraping
url = "https://www.actiac.org/upcoming-events"
response = requests.get(url)

# begin scraping w/ BeautifulSoup
soup = BeautifulSoup(response.content, features='html.parser')
# print(soup)

# identify elements by ID
# results_id = soup.find(id='main')
# print(results_id)

# identify content by class name
results_class = soup.findAll('div', class_='cards-item non-sticky views-row')
print(results_class)

# how many class='field-content'
print(len(results_class))