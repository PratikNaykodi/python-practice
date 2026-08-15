# Q7: Export the final DataFrame to a CSV file.

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

# Calculate Total
df['Total'] = df['Math'] + df['Science'] + df['English']

# Create Status
df['Status'] = df['Total'].apply(
    lambda total: 'Pass' if total >= 250 else 'Fail'
)

# Export DataFrame to CSV
df.to_csv('student_marks_final.csv', index=False)

print("DataFrame exported successfully.")