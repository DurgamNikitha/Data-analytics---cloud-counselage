#QUE13.)DO STUDENTS IN LEADERSHIP POSITION DURING THEIR COLLEGE YEARS TEND TO HAVE HIGHER CGPAS OR BETTER EXCEPETED SALARY?

import pandas as pd
import numpy as ny
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'DAD.xlsx'
df = pd.read_excel(file_path)

# Calculate the average GPA for students with and without leadership positions
avg_gpa_with_leadership = df[df['Leadership- skills'] == 1]['CGPA'].mean()
avg_gpa_without_leadership = df[df['Leadership- skills'] == 0]['CGPA'].mean()

# Calculate the average expected salary for students with and without leadership positions
avg_salary_with_leadership = df[df['Leadership- skills'] == 1]['Year of Graduation'].mean()
avg_salary_without_leadership = df[df['Leadership- skills'] == 0]['Year of Graduation'].mean()

# Example bar chart for GPAs:
plt.figure(figsize=(10, 6))
sns.barplot(x=['With Leadership', 'Without Leadership'], y=[avg_gpa_with_leadership, avg_gpa_without_leadership])
plt.xlabel('Leadership- skills')
plt.ylabel('Average GPA')
plt.title('Average GPA by Leadership- skills')
plt.show()

# Example bar chart for expected salaries:
plt.figure(figsize=(10, 6))
sns.barplot(x=['With Leadership', 'Without Leadership'], y=[avg_salary_with_leadership, avg_salary_without_leadership])
plt.xlabel('Leadership- skills)')
plt.ylabel('Average Expected Salary')
plt.title('Average Expected Salary by Leadership- skills')
plt.show()
