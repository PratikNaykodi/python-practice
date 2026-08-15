# Q10: Plot a boxplot for English marks to check distribution and outliers.

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

# Create boxplot for English marks
plt.boxplot(df['English'])

# Add title and label
plt.title('Distribution of English Marks')
plt.ylabel('English Marks')

# Display boxplot
plt.show()