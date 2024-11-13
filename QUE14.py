#QUE.14) HOW MANY STUDENTS ARE GRADUATING BY THE END OF 2024?

import pandas as pd
data = pd.read_excel('DAD.xlsx')

graduation_dates = data['Year of Graduation']

graduation_dates = pd.to_datetime(graduation_dates, errors='coerce')

# Define the end date for 2024
end_of_2024 = pd.to_datetime('2024')

# Filter the data for students graduating by the end of 2024
graduating_by_2024 = data[graduation_dates <= end_of_2024]

# Count the number of students meeting the criteria
num_students_graduating_by_2024 = len(graduating_by_2024)

# Print the result
print(f"Number of students graduating by the end of 2024: {num_students_graduating_by_2024}")
