# Q2: Create a gender column and perform one-hot encoding.
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

print("Original DataFrame:")
print(df)

# One-hot encoding of Gender
df = pd.get_dummies(df, columns=['Gender'])

print("\nAfter One-Hot Encoding:")
print(df)