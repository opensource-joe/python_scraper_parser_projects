# test scraper

import requests
from bs4 import BeautifulSoup

# create connection to URL for scraping
url = "https://www.actiac.org/upcoming-events"
response = requests.get(url)

# begin scraping w/ BeautifulSoup
soup = BeautifulSoup(response.content)
print(soup)