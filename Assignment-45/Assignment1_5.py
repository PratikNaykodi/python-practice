# Q5: Add a new column 'Status' where students with total >= 250 are 'Pass', else 'Fail'.

import pandas as pd

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

# Add Status column
df['Status'] = df['Total'].apply(
    lambda total: 'Pass' if total >= 250 else 'Fail'
)

print(df)