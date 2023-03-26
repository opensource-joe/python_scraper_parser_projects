# Process instructions

Process instructions to run parsers and generate events spreadsheets.

## ACT-IAC parser

1. Preview ACT-IAC [website](https://www.actiac.org/) for [events](https://www.actiac.org/upcoming-events), [COIs](https://www.actiac.org/communities-interest-coi), and [projects](https://www.actiac.org/recent-projects-and-activities-0) for content updates and overall structure
2. Review code files for familiarity
3. write_to_excel.py
    - Update the Excel file output date - "act-iac/ACT-IAC_Events-03.26.23.xlsx"
    - Run the py file in terminal - fn + control + F5 (on a Mac)
4. Compare Excel file output to corresponding webpages

## Fed Events parser

1. Preview various federal association websites
2. Save local HTML for AFCEA Nova and AFCEA DC
3. Review code files for familiarity, pay special attention to files with list delimiters as the lists will change (e.g., [1::3])
    - events_afcea_beth.py
    - events_afcea_dc.py
    - events_affirm.py
3. write_to_excel.py
    - Update the Excel file output date - "fed-events/Fed_Events-03.26.23.xlsx"
    - Run the py file in terminal - fn + control + F5 (on a Mac)
4. Compare Excel file output to corresponding webpages

**When finished, push all updates to GitHub*