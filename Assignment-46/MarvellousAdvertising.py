# Q1: Dataset contains multiple records about the customers who invest in multiple advertisement
# options.
# Depends on that sales feature indicates the the increased amount in there sales

# This data set contains 4 features as
# TV
# Radio
# Television

# Depends on the above three features Sales feature indicates the increased sale amount.

# We have to design Machine Learning application which uses Classification technique.

# Design machine learning application which follows below steps as

# Step 1:
# Get Data
# Load data from MarvellousAdvertising.csv file into python application.

# Step 2:
# Clean, Prepare and Manipulate data
# As we want to use the above data into machine learning application we have prepare
# that in the format which is accepted by the algorithms.

# Step 3:
# Train Data
# Now we want to train our data for that we have to select the Machine learning algorithm.
# For that we select Linear Regression algorithm from sykit learn library.
# For training purpose divide the dataset into half part.
# Use train method to train our dataset.

# Step 4:
# Test the data
# Test data by passing the remaining half part of the data set.

# Step 5:
# Display predicted values of Linear regression algorithms as well as expected values
# which are provided by the data set.

# Advertising Dataset - Linear Regression


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Step 1: Get Data
# Load data from MarvellousAdvertising.csv
df = pd.read_csv("MarvellousAdvertising.csv")

print("Dataset:")
print(df)

# Step 2: Clean, Prepare and Manipulate Data

# Features (Independent Variables)
X = df[['TV', 'radio', 'newspaper']]

# Target (Dependent Variable)
Y = df['sales']

print("\nFeatures:")
print(X)

print("\nTarget:")
print(Y)

# Step 3: Train Data

# Divide dataset into two parts:
# 50% Training Data
# 50% Testing Data

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.5,
    random_state=42
)

print("\nTraining Data:")
print(X_train)

print("\nTesting Data:")
print(X_test)

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, Y_train)

# Step 4: Test the Data

# Predict Sales using testing data
Y_pred = model.predict(X_test)

# Step 5: Display Predicted and Expected Values

print("\nPredicted Sales vs Expected Sales")
print("----------------------------------")

for predicted, expected in zip(Y_pred, Y_test):
    print(
        "Predicted Sales : {:.2f} | Expected Sales : {:.2f}".format(
            predicted,
            expected
        )
    )