import xlsxwriter
import events_fedscoop

# ---------------------

workbook = xlsxwriter.Workbook('fed-events/Fed_Events-03.02.23.xlsx')

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
# worksheet1.write_column('B3', events_fedscoop.upcoming_date)
# worksheet1.write_column('C3', events_fedscoop.upcoming_location)
# worksheet1.write_column('D3', events_fedscoop.upcoming_url_final)

# ---------------------

# report content for next gov't org

# worksheet2 = workbook.add_worksheet('COIs')

# header2 = ['COI Title', 'Description', 'COI Page']

# worksheet2.write_row('A1', header2, bold)
# worksheet2.write_column('A2', cois.coi_title)
# worksheet2.write_column('B2', cois.coi_description)
# worksheet2.write_column('C2', cois.coi_link_2)

# ---------------------

workbook.close()