# QUE.4) WHAT IS THE DISTRIBUTION OF STUDENTS EXPERIENCE WITH PYTHON PROGRAMMING?

import pandas as pd
import matplotlib.pyplot as plt

excel_file = 'DAD.xlsx'
data = pd.read_excel(excel_file)

python_experience = data['Experience with python (Months)']

# Calculate the frequency of each experience level
experience_counts = python_experience.value_counts().reset_index()

# Rename columns for clarity
experience_counts.columns = ['Experience_Level', 'Count']

# Sort the data by experience level (you may want to customize the sorting order)
experience_counts = experience_counts.sort_values(by='Experience_Level')

# Plot the distribution of students' Python experience levels
plt.figure(figsize=(10, 6))
plt.bar(experience_counts['Experience_Level'], experience_counts['Count'])
plt.xlabel('Python Experience Level')
plt.ylabel('Number of Students')
plt.title('Distribution of Students\' Python Experience Levels')
plt.xticks(rotation=45)  # Rotate x-axis labels for readability
plt.tight_layout()

# Show the plot
plt.show()