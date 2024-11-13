# QUE.3)WHAT IS THE DISTRIBUTION OF STUDENTS ACROSS DIFFERENT GRADUATION YEARS?

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel('DAD.xlsx')

# Assuming your Excel file has a column named 'Year of Graduation' for graduation years
graduation_years = data['Year of Graduation']

# Calculate the frequency of each graduation year
year_counts = graduation_years.value_counts().reset_index()

# Rename columns for clarity
year_counts.columns = ['Year of Graduation', 'Count']

# Sort the data by graduation year
year_counts = year_counts.sort_values(by='Year of Graduation')

# Plot the distribution of students across different graduation years
plt.figure(figsize=(10, 6))
plt.bar(year_counts['Year of Graduation'], year_counts['Count'])
plt.xlabel('Year of Graduation')
plt.ylabel('Number of Students')
plt.title('Distribution of Students Across Graduation Years')
plt.xticks(rotation=45)  # Rotate x-axis labels for readability
plt.tight_layout()

# Show the plot
plt.show()