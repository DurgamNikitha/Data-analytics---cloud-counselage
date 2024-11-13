# QUE.8)WHAT IS THE AVERAGE GPA FOR STUDENT FROM EACH CITY?

import pandas as pd
excel_file = 'DAD.xlsx'
df = pd.read_excel(excel_file)

# Group data by the "City" column
grouped_data = df.groupby('City')

# Replace 'Column_Name' with the name of the column you want to find the average of
column_name = 'CGPA'

# Calculate the average for each city
for city, city_group in grouped_data:
    city_average = city_group[column_name].mean()
    print(f'Average {column_name} in {city}: {city_average}')