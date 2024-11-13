# QUE.6) HOW DOES THE CGPA VARY AMONG DIFFERENT COLLEGES? (Show top 5 results only)

import pandas as pd
import matplotlib.pyplot as plt

excel_file = 'DAD.xlsx'
data = pd.read_excel(excel_file)

# Assuming your dataset has columns 'College' and 'CGPA', select these columns
college_cgpa_data = data[['College Name', 'CGPA']]

# Group the data by 'College' and calculate the mean CGPA for each college
college_avg_cgpa = college_cgpa_data.groupby('College Name')['CGPA'].mean().reset_index()

# Sort the colleges by average CGPA in descending order and select the top 5
top_five_colleges = college_avg_cgpa.sort_values(by='CGPA', ascending=False).head(5)

# Plot a bar chart to visualize the variation in CGPA among the top 5 colleges
plt.figure(figsize=(10, 6))
plt.bar(top_five_colleges['College Name'], top_five_colleges['CGPA'])
plt.xlabel('College Name')
plt.ylabel('Average CGPA')
plt.title('Average CGPA Among Top 5 Colleges')
plt.xticks(rotation=45)  # Rotate x-axis labels for readability
plt.tight_layout()

# Show the plot
plt.show()