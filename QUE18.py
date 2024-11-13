#QUE.18)HOW MANY STUDENTS KNOW ABOUT THE EVENT FROM THEIR COLLEGES?WHICH OF THESE TOP 5 COLLEGES?

import pandas as pd
data = pd.read_excel('DAD.xlsx')

# Assuming your Excel file has a column named 'College Name' for college information
college_counts = data['College Name'].value_counts().reset_index()

college_counts.columns = ['College Name', 'Events']

# Sort the data by the number of students (in descending order)
college_counts = college_counts.sort_values(by='Events', ascending=False)

# Select the top 5 colleges
top_5_colleges = college_counts.head(5)

# Print the result
print("Top 5 Colleges with the Most Students:")
print(top_5_colleges)