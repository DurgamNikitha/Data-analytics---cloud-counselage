#QUE.11)HOW DOES THE EXCEPETED SALARY VARY BASED ON FACTORS LIKE CGPA,FAMILY INCOME,EXPERIENCE WITH PYTHON?

import pandas as pd
df = pd.read_excel('DAD.xlsx')
print(df.head())

# Check data types and missing values
print(df.info())

# Summary statistics
print(df.describe())
import matplotlib.pyplot as plt

# Scatter plot between CGPA and Salary Expectations
plt.scatter(df['CGPA'], df['Expected salary (Lac)'])
plt.xlabel('CGPA')
plt.ylabel('Expected salary (Lac)')
plt.title('Relationship between CGPA and Expected salary (Lac)')
plt.show()

# Scatter plot between Family Income and Salary Expectations
plt.scatter(df['Family Income'], df['Expected salary (Lac)'])
plt.xlabel('Family Income')
plt.ylabel('Expected salary (Lac)')
plt.title('Relationship between Family Income and Expected salary (Lac)')
plt.show()

# Scatter plot between Experience with python (Months) and Salary Expectations
plt.scatter(df['Experience with python (Months)'], df['Expected salary (Lac)'])
plt.xlabel('Experience with python (Months)')
plt.ylabel('Expected salary (Lac)')
plt.title('Relationship between Experience with python (Months) and Expected salary (Lac)')
plt.show()
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Define the features (independent variables) and target (dependent variable)
X = df[['CGPA', 'Family Income', 'Experience with python (Months)']]
y = df['Expected salary (Lac)']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Fit the model to the training data
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
