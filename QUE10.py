#QUE.10) HOW MANY STUDENTS FROM VARIOUS CITIES?

import pandas as pd
import matplotlib.pyplot as plt

file_path = 'DAD.xlsx'
df = pd.read_excel(file_path)

# Assuming your Excel file has a 'City' column and a 'First Name' column, you can count the number of students who solved through data analysis per city
city_data = df.groupby('City')['First Name'].sum().reset_index()

# Create a bar chart
plt.figure(figsize=(10,4))
plt.bar(city_data['City'], city_data['First Name'])
plt.xlabel('City')
plt.ylabel('Number of Students First Name Through Data Analysis')
plt.title('Students First Name Through Data Analysis by City')
plt.xticks(rotation=100, ha='right')  # Rotate x-axis labels for better readability

# Display the chart
plt.tight_layout()
plt.show()