# Q4: Plot a pie chart of subject marks for 'Sagar'.

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

# Get Sagar's marks
sagar = df[df['Name'] == 'Sagar'].iloc[0]

# Subject names
subjects = ['Math', 'Science', 'English']

# Sagar's marks
marks = [sagar['Math'], sagar['Science'], sagar['English']]

# Create pie chart
plt.pie(
    marks,
    labels=subjects,
    autopct='%1.1f%%'
)

plt.title("Sagar's Marks Distribution")

# Display chart
plt.show()