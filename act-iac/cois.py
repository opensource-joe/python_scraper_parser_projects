# scraper and parser for ACT-IAC Community of Interest groups

import requests
from bs4 import BeautifulSoup
import xlsxwriter

# ---------------------

url = "https://www.actiac.org/communities-interest-coi"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
cards = soup.find_all('div', {'class': 'views-row'})[0]
post_cards = cards.find_all('div', {'class', 'views-row'})

# ---------------------

# COI title, only need text, href controls accordion effect
# <a href="/groups/acquisition-community-interest" hreflang="en">Acquisition Community of Interest</a>

coi_title = [getattr(title.find('a'), 'text', None) for title in post_cards]

# ---------------------

# COI description
# <p>The Acquisition COI is focused on increasing engagement and facilitating the sharing of best practices between the government and industry to improve the federal acquisition process.</p>

coi_description = [getattr(title.find('p'), 'text', None) for title in post_cards]

# ---------------------
# Link to COI page, need to be logged in to ACT-IAC site
# <a href="/groups/acquisition-community-interest" hreflang="en">&gt; Proceed to COI page (ACT-IAC Members Only)</a>

post_cards_link = cards.find_all('div', {'class', 'views-row'})[0]
post_cards_link_p = cards.find_all('div', {'class', 'views-field views-field-view-node'})

coi_link = [link_value.find_all('a') for link_value in post_cards_link_p]
flat_coi_list = [item for sublist in coi_link for item in sublist]

coi_link_2 = []
for link in flat_coi_list:
    coi_link_2.append(f"https://www.actiac.org{link.get('href')} (members only)")

# ---------------------

# xlsxwriter output

workbook = xlsxwriter.Workbook('excel_docs/ACT-IAC_COIs-02.27.23.xlsx')
worksheet2 = workbook.add_worksheet('COIs')

header = ['COI_Title', 'Description', 'COI_Page']

worksheet2.write_row('A1', header)
worksheet2.write_column('A2', coi_title)
worksheet2.write_column('B2', coi_description)
worksheet2.write_column('C2', coi_link_2)

workbook.close()

# move to one py file for clean output