import xlsxwriter
import events
import cois
import projects

# ---------------------

workbook = xlsxwriter.Workbook('act-iac/ACT-IAC_Events-03.25.23.xlsx')

# ---------------------

# formatting

bold = workbook.add_format({'bold': True})

# ---------------------

# report content for Events

worksheet1 = workbook.add_worksheet('Events Calendar')

header1 = ['Event Type', 'Event Format', 'Event Title', 'Event Date', 'Description', 'Learn More']

worksheet1.write_row('A1', header1, bold)
worksheet1.write_column('A2', events.event_type)
worksheet1.write_column('B2', events.event_format)
worksheet1.write_column('C2', events.event_title)
worksheet1.write_column('D2', events.event_date)
worksheet1.write_column('E2', events.event_description)
worksheet1.write_column('F2', events.event_more_2)

# ---------------------

# report content for COIs

worksheet2 = workbook.add_worksheet('COIs')

header2 = ['COI Title', 'Description', 'COI Page']

worksheet2.write_row('A1', header2, bold)
worksheet2.write_column('A2', cois.coi_title)
worksheet2.write_column('B2', cois.coi_description)
worksheet2.write_column('C2', cois.coi_link_2)

# ---------------------

# report content for Projects

worksheet3 = workbook.add_worksheet('Projects')

worksheet3.write_row('A1', projects.accord_group_seek, bold)
header3_1 = ('Project Title', 'Learn More')

worksheet3.write_row('A3', header3_1, bold)
worksheet3.write_column('A4', projects.card_title)
worksheet3.write_column('B4', projects.card_link_final)

worksheet3.write_row('A10', projects.accord_group_prog, bold)
header3_2 = ('Project Title', 'Learn More')

worksheet3.write_row('A11', header3_2, bold)
worksheet3.write_column('A12', projects.card_title_prog)
worksheet3.write_column('B12', projects.card_link_prog_final)

# ---------------------

workbook.close()