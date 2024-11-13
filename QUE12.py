#QUE.12) WHICH EVENT TEND TO ATTRACT MORE STUDENTS FROM SPECIFIC FIELDS OF STUDY?
 
import pandas as pd

file_path = 'DAD.xlsx'
df = pd.read_excel(file_path)

column_name = 'Events' 

# Find the most common values in the specified column
most_common_values = df[column_name].value_counts()

# Print the top N most common values (adjust 'N' as needed)
N = 20  # Change this to the desired number of top values to display
print(f"Top {N} most common values in the '{column_name}' column:")
print(most_common_values.head(N))



