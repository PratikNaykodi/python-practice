# Q7: Create a bar plot of student names vs total marks.

import pandas as pd
import matplotlib.pyplot as plt

# Create data
data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate Total marks
df['Total'] = df['Math'] + df['Science'] + df['English']

# Create bar plot
plt.bar(df['Name'], df['Total'])

# Add title and labels
plt.title('Student Names vs Total Marks')
plt.xlabel('Student Name')
plt.ylabel('Total Marks')

# Display plot
plt.show()