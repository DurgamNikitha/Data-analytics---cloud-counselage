#QUE.15)WHICH PROMOTION CHANNEL BRINGS IN MORE STUDENT PARTICIPATIONS FOR THE EVENT?

import pandas as pd
import matplotlib.pyplot as plt

file_path = 'DAD.xlsx'
df = pd.read_excel(file_path)

channel_participation = df.groupby('Events')['Quantity'].sum().reset_index()

# Sort the channels by total participants in descending order
channel_participation = channel_participation.sort_values(by='Quantity', ascending=False)

# Create a bar chart to visualize the data
plt.figure(figsize=(10, 6))
plt.bar(channel_participation['Events'], channel_participation['Quantity'])
plt.xlabel('Events')
plt.ylabel('Total Student Participants')
plt.title('Student Participation by Events')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability

# Show the chart
plt.tight_layout()
plt.show()

# Get the Events with the highest participation
most_participated_channel = channel_participation.iloc[0]['Events']
print(f"The Events that brings in the most student participation is: {most_participated_channel}")
