#QUE.16)FIND THE NUMBER OF STUDENTS WHO ATTENDED THE EVENTS RELATED TO DATA SCIENCE?

import pandas as pd
df = pd.read_excel('DAD.xlsx')

# Filter rows related to data science events
data_science_events = df[df['Events'].str.contains('Data Visualization using Power BI', case=False)]
# Assuming the student information is in a column named 'Email ID'.
unique_students = data_science_events['Email ID'].nunique()
print(f'Total number of students who attended data science events: {unique_students}')
