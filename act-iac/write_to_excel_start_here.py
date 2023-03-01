import xlsxwriter
import events
import cois
# import projects

# ---------------------

workbook = xlsxwriter.Workbook('act-iac/ACT-IAC_Events-03.01.23.xlsx')

# ---------------------

# report content for Events

worksheet1 = workbook.add_worksheet('Events_Calendar')

header1 = ['Event_Type', 'Event_Format', 'Event_Title', 'Event_Date', 'Description', 'Learn More']

worksheet1.write_row('A1', header1)
worksheet1.write_column('A2', events.event_type)
worksheet1.write_column('B2', events.event_format)
worksheet1.write_column('C2', events.event_title)
worksheet1.write_column('D2', events.event_date)
worksheet1.write_column('E2', events.event_description)
worksheet1.write_column('F2', events.event_more_2)

# ---------------------

# report content for COIs

worksheet2 = workbook.add_worksheet('COIs')

header2 = ['COI_Title', 'Description', 'COI_Page']

worksheet2.write_row('A1', header2)
worksheet2.write_column('A2', cois.coi_title)
worksheet2.write_column('B2', cois.coi_description)
worksheet2.write_column('C2', cois.coi_link_2)

# ---------------------

# report content for Projects

# worksheet3 = workbook.add_worksheet('Projects')

# header3 = ['Project_Title']

# worksheet3.write_row('A1', header3)
# worksheet3.write_column('A2', [tbd])

# ---------------------

workbook.close()