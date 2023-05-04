from bs4 import BeautifulSoup

# ---------------------

open_file = open('act-iac/speakers.html', 'r')
contents = open_file.read()

soup = BeautifulSoup(contents, 'html.parser')
cards = soup.find('div', {'class', 'SpeakersStyles__gridContainerGrouping___eiwPT grid__container___J52Tg'})

# ---- data source ----
# keynote 
keynote_speaker = cards.findAll('div')[4]
keynote_speaker2 = keynote_speaker.findAll('span')

keynote_speaker_list = []
for item in keynote_speaker2:
    keynote_speaker_list.append(item.text.strip())

# speaker 
speaker = cards.findAll('div')[56]
speaker2 = speaker.findAll('span')

speaker_list = []
for item in speaker2:
    speaker_list.append(item.text.strip())

# moderator 
# TODO

# govt cochair 
govt = cards.findAll('div')[500]
govt2 = govt.findAll('span')

govt_cochair_list = []
for item in govt2:
    govt_cochair_list.append(item.text.strip())

# industry cochair 
# TODO

# advisor 
# TODO

# ---- first name ----
# keynote 
keynote_first_name = []
for first in keynote_speaker_list[::5]:
    keynote_first_name.append(first)

# speaker 
speaker_first_name = []
for first in speaker_list[::5]:
    speaker_first_name.append(first)

# moderator 

# govt cochair 
govt_first_name = []
for first in govt_cochair_list[::5]:
    govt_first_name.append(first)

# industry cochair 

# advisor cochair 

# ---- last name ----
# keynote 

# speaker 

# moderator 

# govt cochair 

# industry cochair 

# advisor cochair 

# ---- title ----
# keynote 

# speaker 

# moderator 

# govt cochair 

# industry cochair 

# advisor cochair 

# ---- organization ----
# keynote 

# speaker 

# moderator 

# govt cochair 

# industry cochair 

# advisor cochair 


# ---------------------

# TODO: img src from website

# img
# keynote_speaker_img = cards.findAll('img')
# for image in speaker_img:
#     print(image['src'])

# TODO: profile info