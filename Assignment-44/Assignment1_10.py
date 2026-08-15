# Q10: Drop the 'English' column from original DataFrame.

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

print("Original DataFrame:")
print(df)

# Drop English column
df = df.drop('English', axis=1)

print("\nDataFrame after dropping English:")
print(df)