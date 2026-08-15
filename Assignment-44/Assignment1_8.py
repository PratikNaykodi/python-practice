# Q8: Plot a line chart of marks for 'Amit' across all subjects.

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

# Get Amit's marks
amit = df[df['Name'] == 'Amit'].iloc[0]

# Subjects
subjects = ['Math', 'Science', 'English']

# Marks
marks = [amit['Math'], amit['Science'], amit['English']]

# Create line chart
plt.plot(subjects, marks, marker='o')

# Add title and labels
plt.title("Amit's Marks Across Subjects")
plt.xlabel("Subjects")
plt.ylabel("Marks")

# Display chart
plt.show()