# Q8: Plot a histogram of math marks.
import pandas as pd
import matplotlib.pyplot as plt

# Create data
data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create histogram of Math marks
plt.hist(df['Math'], bins=5)

# Add title and labels
plt.title('Distribution of Math Marks')
plt.xlabel('Math Marks')
plt.ylabel('Number of Students')

# Display histogram
plt.show()