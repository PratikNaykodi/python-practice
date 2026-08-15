# Q3: Group students by gender and calculate average marks.

import pandas as pd

# Create data
data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82],
    'Gender': ['Male', 'Male', 'Female']
}

# Create DataFrame
df = pd.DataFrame(data)

# Group by Gender and calculate average marks
result = df.groupby('Gender')[['Math', 'Science', 'English']].mean()

print("Average Marks by Gender:")
print(result)