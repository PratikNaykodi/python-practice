# Q9: Create a DataFrame with missing values and fill them with column mean.

# data2 = {
# 'Name': ['Amit', 'Sagar', 'Pooja'],
# 'Math': [np.nan, 76, 88],
# 'Science': [91, np.nan, 85]
# }

import pandas as pd
import numpy as np

# Create data with missing values
data2 = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [np.nan, 76, 88],
    'Science': [91, np.nan, 85]
}

# Create DataFrame
df = pd.DataFrame(data2)

print("Before filling missing values:")
print(df)

# Fill missing values with column mean
df['Math'] = df['Math'].fillna(df['Math'].mean())
df['Science'] = df['Science'].fillna(df['Science'].mean())

print("\nAfter filling missing values:")
print(df)