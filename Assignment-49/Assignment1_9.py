# Q9: Write a Python program using scikit-learn to generate a classification report for the following data:

# actual = [1,1,1,1,0,0,0,0]
# predicted = [1,1,0,1,0,1,0,0]

# Display the complete classification report including precision, recall, F1-score, and support.

from sklearn.metrics import classification_report

# Actual values
actual = [1, 1, 1, 1, 0, 0, 0, 0]

# Predicted values
predicted = [1, 1, 0, 1, 0, 1, 0, 0]

# Generate classification report
report = classification_report(actual, predicted)

# Display report
print("Classification Report:")
print(report)