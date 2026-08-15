# Q4: Display students who scored more than 85 in Science.

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

# Display students who scored more than 85 in Science
result = df[df['Science'] > 85]

print("Students who scored more than 85 in Science:")
print(result)