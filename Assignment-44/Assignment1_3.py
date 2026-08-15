# Q3: Add a new column 'Total' to the DataFrame as the sum of all subject marks.

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

# Add Total column
df['Total'] = df['Math'] + df['Science'] + df['English']

# Display DataFrame
print(df)