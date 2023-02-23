# scratch file for working with code

jobs = cards[0].find('img')
string_jobs = str(jobs)

if string_jobs == '<img alt="" src="/sites/default/files/federal_insights_exchange2.png"/>':
    print("Federal Insights Exchange (FIE)")
elif string_jobs == '<img alt="" src="/sites/default/files/Small%20Business%20Alliance.png"/>':
    print("Small Business Alliance")
elif string_jobs == '<img alt="" src="/sites/default/files/community_of_interest.png"/>':
    print("Community of Interest (COI)")
elif string_jobs == '<img alt="" src="/sites/default/files/professional_development.png"/>':
    print("Professional Development")
elif string_jobs == '<img alt="" src="/sites/default/files/conferences_0.png"/>':
    print("Conference")
else:
    print("Type of Event TBD")
