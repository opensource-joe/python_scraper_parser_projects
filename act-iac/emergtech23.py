from bs4 import BeautifulSoup

# ---------------------

open_file = open('act-iac/speakers.html', 'r')
contents = open_file.read()

soup = BeautifulSoup(contents, 'html.parser')
cards = soup.find('div', {'class', 'SpeakersStyles__gridContainerGrouping___eiwPT grid__container___J52Tg'})

# print(cards)

# ---------------------

# keynote speaker

# TODO: image src from website

# img
# keynote_speaker_img = cards.findAll('img')
# for image in speaker_img:
#     print(image['src'])

# ---

# keynote speaker text values

keynote_speaker = cards.findAll('div')[4]
keynote_speaker2 = keynote_speaker.findAll('span')

keynote_speaker_list = []
for item in keynote_speaker2:
    keynote_speaker_list.append(item.text.strip())

# ---

# first name

keynote_first_name = []
for first in keynote_speaker_list[::5]:
    keynote_first_name.append(first)

# ---

# last name

keynote_last_name = []
for last in keynote_speaker_list[1::5]:
    keynote_last_name.append(last)

# ---

# title

keynote_title = []
for value_title in keynote_speaker_list[2::5]:
    keynote_title.append(value_title)

# ---

# agency

keynote_agency = []
for value_agency in keynote_speaker_list[3::5]:
    keynote_agency.append(value_agency)

# ---

# TODO: profile

# ---------------------

# speakers text values

# TODO: image src from url

# ---

# speaker text values

speaker = cards.findAll('div')[56]
speaker2 = speaker.findAll('span')

speaker_list = []
for item in speaker2:
    speaker_list.append(item.text.strip())

# ---

# first name

speaker_first_name = []
for first in speaker_list[::5]:
    speaker_first_name.append(first)

# last name

speaker_last_name = []
for last in speaker_list[1::5]:
    speaker_last_name.append(last)


# ---

# title

speaker_title = []
for value_title in speaker_list[2::5]:
    speaker_title.append(value_title)

# ---

# agency

speaker_agency = []
for value_agency in speaker_list[3::5]:
    speaker_agency.append(value_agency)

# ---

# TODO: profile

# ---------------------

# moderators text values

# TODO: image src from url

# ---

# moderators text values

moderators = cards.findAll('div')[500]
moderators2 = moderators.findAll('span')

moderators_list = []
for item in moderators2:
    moderators_list.append(item.text.strip())

# ---

# first name

moderator_first_name = []
for first in moderators_list[::5]:
    moderator_first_name.append(first)
    
# ---

# last name

moderator_last_name = []
for last in moderators_list[1::5]:
    moderator_last_name.append(last)

# ---

# title

moderator_title = []
for value_title in moderators_list[2::5]:
    moderator_title.append(value_title)

# ---

# agency

moderator_agency = []
for value_agency in moderators_list[3::5]:
    moderator_agency.append(value_agency)