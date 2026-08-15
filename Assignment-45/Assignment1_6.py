# Q6: Count how many students passed.
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

# Count passed students
passed_count = (df['Status'] == 'Pass').sum()

print("Number of students passed:", passed_count)