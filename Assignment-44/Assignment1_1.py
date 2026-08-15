# Q1: Create a DataFrame for student marks and print basic information like shape, columns, and
# data types.

# data = {
# 'Name': ['Amit', 'Sagar', 'Pooja'],
# 'Math': [85, 90, 78],
# 'Science': [92, 88, 80],
# 'English': [75, 85, 82]
# }
# Note : Consider the same dataset for this as well as next assignment.

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

# Display DataFrame
print("Student Marks Data:")
print(df)

# Display shape
print("\nShape of DataFrame:")
print(df.shape)

# Display columns
print("\nColumns:")
print(df.columns)

# Display data types
print("\nData Types:")
print(df.dtypes)