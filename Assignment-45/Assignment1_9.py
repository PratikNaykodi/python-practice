# Q9: Rename 'Math' column to 'Mathematics'.

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

# Rename Math to Mathematics
df.rename(columns={'Math': 'Mathematics'}, inplace=True)

print(df)