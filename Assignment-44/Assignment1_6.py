# Q6: Sort the DataFrame by 'Total' marks in descending order.

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

# Sort by Total in descending order
df = df.sort_values(by='Total', ascending=False)

# Display DataFrame
print(df)