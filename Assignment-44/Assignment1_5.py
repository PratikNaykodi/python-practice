# Q5: Replace 'Pooja' with 'Puja' in the 'Name' column.

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

# Replace Pooja with Puja
df['Name'] = df['Name'].replace('Pooja', 'Puja')

# Display DataFrame
print(df)