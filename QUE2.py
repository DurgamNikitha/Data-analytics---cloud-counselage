# QUE.2) WHAT IS THE AVERAGE GPA OF THE STUDENT?

import pandas as pd

excel_file = 'DAD.xlsx'
df = pd.read_excel(excel_file)

# Replace 'Column_Name' with the name of the column you want to find the average of
column_name = 'CGPA'
average = df[column_name].mean()

print(f'The average of {column_name} is: {average}')