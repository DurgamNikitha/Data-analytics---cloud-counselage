#QUE.7) ARE THERE ANY OUTLIERS IN THE QUANTITY(number of courses completed) ATTRIBUTR?

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

excel_file = 'DAD.xlsx'
data = pd.read_excel(excel_file)


# Assuming your dataset has a column named 'Quantity' for the number of courses completed
quantity_data = data['Quantity']

# Create a box plot to visualize the distribution of the 'Quantity' attribute
plt.figure(figsize=(6, 4))
plt.boxplot(quantity_data, vert=False)
plt.xlabel('Quantity')
plt.title('Box Plot of Quantity (Number of Courses Completed)')
plt.show()

# Calculate the Interquartile Range (IQR)
Q1 = quantity_data.quantile(0.25)
Q3 = quantity_data.quantile(0.75)
IQR = Q3 - Q1

# Define the lower and upper bounds to identify outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identify outliers
outliers = quantity_data[(quantity_data < lower_bound) | (quantity_data > upper_bound)]

# Display the outliers
print("Outliers in the 'Quantity' attribute:")
print(outliers)