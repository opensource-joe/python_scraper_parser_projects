import xlsxwriter
import events_fedscoop
import events_govexec
import events_nextgov
import events_meritalk
# import events_proservcouncil
import events_afcea_beth
import events_afcea_nova

# ---------------------

workbook = xlsxwriter.Workbook('fed-events/Fed_Events-03.25.23.xlsx')

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
worksheet4.write_column('C2', events_meritalk.upcoming_description_final)
worksheet4.write_column('D2', events_meritalk.upcoming_url_final)

# ---------------------

# report content Professional Services Council events

# worksheet5 = workbook.add_worksheet('ProServCouncil')

# header5 = ['Event Name', 'Event Date', 'Location', 'Learn More']

# worksheet5.write_row('A1', header5, bold)
# worksheet5.write_column('A2', events_proservcouncil.upcoming_title_final)
# worksheet5.write_column('B2', events_proservcouncil.upcoming_date_final)
# worksheet5.write_column('C2', events_proservcouncil.upcoming_location_final)
# worksheet5.write_column('D2', events_proservcouncil.upcoming_url_final)

# ---------------------

# report content Professional Services Council events

worksheet6 = workbook.add_worksheet('AFCEA')

header6 = ['Event Name', 'Event Date', 'Learn More']

worksheet6.write('A1', 'AFCEA Bethesda', bold)
worksheet6.write('A8', 'AFCEA Northern VA', bold)

# Bethesda
worksheet6.write_row('A3', header6, bold)
worksheet6.write_column('A4', events_afcea_beth.upcoming_title_final)
worksheet6.write_column('B4', events_afcea_beth.upcoming_date_final)
worksheet6.write_column('C4', events_afcea_beth.upcoming_url_final)

# NoVA
worksheet6.write_row('A10', header6, bold)
worksheet6.write_column('A11', events_afcea_nova.upcoming_title_final)
worksheet6.write_column('B11', events_afcea_nova.dates)
worksheet6.write_column('C11', events_afcea_nova.upcoming_url_final)

# ---------------------

workbook.close()