import xlsxwriter
import events_fedscoop
import events_govexec
import events_nextgov
import events_meritalk

# ---------------------

workbook = xlsxwriter.Workbook('fed-events/Fed_Events-03.03.23.xlsx')

# ---------------------

# formatting

bold = workbook.add_format({'bold': True})

# ---------------------

# report content for FedScoop events

worksheet1 = workbook.add_worksheet('FedScoop')

header1 = ['Event Name', 'Event Date', 'Location', 'Learn More']

worksheet1.write_row('A1', header1, bold)
worksheet1.write_column('A2', events_fedscoop.featured_title)
worksheet1.write_column('B2', events_fedscoop.featured_date)
worksheet1.write_column('C2', events_fedscoop.featured_location)
worksheet1.write_column('D2', events_fedscoop.featured_url_final)

worksheet1.write_column('A3', events_fedscoop.upcoming_title_final)
worksheet1.write_column('B3', events_fedscoop.upcoming_date_final)
worksheet1.write_column('C3', events_fedscoop.upcoming_location_final)
worksheet1.write_column('D3', events_fedscoop.upcoming_url_final)

# ---------------------

# report content Gov Exec events

worksheet2 = workbook.add_worksheet('Gov Exec')

header2 = ['Event Name', 'Event Date', 'Location', 'Learn More']

worksheet2.write_row('A1', header2, bold)
worksheet2.write_column('A2', events_govexec.featured_title)
worksheet2.write_column('B2', events_govexec.featured_date)
worksheet2.write_column('C2', events_govexec.featured_location)
worksheet2.write_column('D2', events_govexec.featured_url_final)

worksheet2.write_column('A3', events_govexec.upcoming_title_final)
worksheet2.write_column('B3', events_govexec.upcoming_date_final)
worksheet2.write_column('C3', events_govexec.upcoming_location_final)
worksheet2.write_column('D3', events_govexec.upcoming_url_final)

# ---------------------

# report content Nextgov events

worksheet3 = workbook.add_worksheet('Nextgov')

header3 = ['Event Name', 'Event Date', 'Location', 'Learn More']

worksheet3.write_row('A1', header3, bold)
worksheet3.write_column('A2', events_nextgov.upcoming_title_final)
worksheet3.write_column('B2', events_nextgov.upcoming_date_final)
worksheet3.write_column('C2', events_nextgov.upcoming_location_final)
worksheet3.write_column('D2', events_nextgov.upcoming_url_final)

# ---------------------

# report content Meritalk events

worksheet4 = workbook.add_worksheet('Meritalk')

header4 = ['Event Name', 'Event Date', 'Description', 'Learn More']

worksheet4.write_row('A1', header4, bold)
worksheet4.write_column('A2', events_meritalk.upcoming_title_final)
worksheet4.write_column('B2', events_meritalk.upcoming_date_final)
worksheet4.write_column('C2', events_meritalk.upcoming_location_final)
worksheet4.write_column('D2', events_meritalk.upcoming_url_final)

# ---------------------

workbook.close()