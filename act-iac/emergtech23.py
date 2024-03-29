import xlsxwriter
from bs4 import BeautifulSoup

# ---------------------

workbook = xlsxwriter.Workbook('act-iac/EmergingTech_2023.xlsx')
worksheet1 = workbook.add_worksheet('Speakers')

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
moderator = cards.findAll('div')[391]
moderator2 = moderator.findAll('span')

moderator_list = []
for item in moderator2:
    moderator_list.append(item.text.strip())

# govt cochair 
govt = cards.findAll('div')[500]
govt2 = govt.findAll('span')

govt_cochair_list = []
for item in govt2:
    govt_cochair_list.append(item.text.strip())

# industry cochair 
industry = cards.findAll('div')[530]
industry2 = industry.findAll('span')

industry_cochair_list = []
for item in industry2:
    industry_cochair_list.append(item.text.strip())

# advisor 
advisor = cards.findAll('div')[550]
advisor2 = advisor.findAll('span')

advisor_cochair_list = []
for item in advisor2:
    advisor_cochair_list.append(item.text.strip())

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
moderator_first_name = []
for first in moderator_list[::5]:
    moderator_first_name.append(first)

# govt cochair 
govt_first_name = []
for first in govt_cochair_list[::5]:
    govt_first_name.append(first)

# industry cochair 
industry_first_name = []
for first in industry_cochair_list[::5]:
    industry_first_name.append(first)

# advisor
advisor_first_name = []
for first in advisor_cochair_list[::5]:
    advisor_first_name.append(first)

# ---- last name ----
# keynote 
keynote_last_name = []
for last in keynote_speaker_list[1::5]:
    keynote_last_name.append(last)
    
# speaker 
speaker_last_name = []
for last in speaker_list[1::5]:
    speaker_last_name.append(last)
    
# moderator 
moderator_last_name = []
for last in moderator_list[1::5]:
    moderator_last_name.append(last)

# govt cochair 
govt_last_name = []
for last in govt_cochair_list[1::5]:
    govt_last_name.append(last)
    
# industry cochair 
industry_last_name = []
for last in industry_cochair_list[1::5]:
    industry_last_name.append(last)

# advisor
advisor_last_name = []
for last in advisor_cochair_list[1::5]:
    advisor_last_name.append(last)

# ---- title ----
# keynote 
keynote_title = []
for value_title in keynote_speaker_list[2::5]:
    keynote_title.append(value_title)
    
# speaker 
speaker_title = []
for value_title in speaker_list[2::5]:
    speaker_title.append(value_title)
    
# moderator 
moderator_title = []
for value_title in moderator_list[2::5]:
    moderator_title.append(value_title)

# govt cochair 
govt_title = []
for value_title in govt_cochair_list[2::5]:
    govt_title.append(value_title)
    
# industry cochair 
industry_title = []
for value_title in industry_cochair_list[2::5]:
    industry_title.append(value_title)

# advisor
advisor_title = []
for value_title in advisor_cochair_list[2::5]:
    advisor_title.append(value_title)

# ---- organization ----
# keynote 
keynote_agency = []
for value_agency in keynote_speaker_list[3::5]:
    keynote_agency.append(value_agency)
    
# speaker 
speaker_agency = []
for value_agency in speaker_list[3::5]:
    speaker_agency.append(value_agency)
    
# moderator 
moderator_agency = []
for value_agency in moderator_list[3::5]:
    moderator_agency.append(value_agency)

# govt cochair 
govt_agency = []
for value_agency in govt_cochair_list[3::5]:
    govt_agency.append(value_agency)
    
# industry cochair 
industry_agency = []
for value_agency in industry_cochair_list[3::5]:
    industry_agency.append(value_agency)

# advisor
advisor_agency = []
for value_agency in advisor_cochair_list[3::5]:
    advisor_agency.append(value_agency)

# ---------------------

header1 = ['First_Name', 'Last_Name', 'Title', 'Organization']
bold = workbook.add_format({'bold': True})

worksheet1.write_row('A1', header1, bold)

worksheet1.write_column('A2', keynote_first_name)
worksheet1.write_column('A7', speaker_first_name)
worksheet1.write_column('A43', moderator_first_name)
worksheet1.write_column('A54', govt_first_name)
worksheet1.write_column('A56', industry_first_name)
worksheet1.write_column('A58', advisor_first_name)

worksheet1.write_column('B2', keynote_last_name)
worksheet1.write_column('B7', speaker_last_name)
worksheet1.write_column('B43', moderator_last_name)
worksheet1.write_column('B54', govt_last_name)
worksheet1.write_column('B56', industry_last_name)
worksheet1.write_column('B58', advisor_last_name)

worksheet1.write_column('C2', keynote_title)
worksheet1.write_column('C7', speaker_title)
worksheet1.write_column('C43', moderator_title)
worksheet1.write_column('C54', govt_title)
worksheet1.write_column('C56', industry_title)
worksheet1.write_column('C58', advisor_title)

worksheet1.write_column('D2', keynote_agency)
worksheet1.write_column('D7', speaker_agency)
worksheet1.write_column('D43', moderator_agency)
worksheet1.write_column('D54', govt_agency)
worksheet1.write_column('D56', industry_agency)
worksheet1.write_column('D58', advisor_agency)

workbook.close()