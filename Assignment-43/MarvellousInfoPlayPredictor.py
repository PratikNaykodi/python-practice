# There is one data set of wether conditions.
# That dataset contains information as wether and we have to decides whether to play or
# not.
# Data set contains the target variable as Play which indicates whether to play or not.

# Consider below Marvellous Infosystems Play Predictor Dataset as


# According to above dataset there are two features as
# 1. Wether
# 2. Temperature

# We have two labels as
# 1.Yes
# 2.No

# There are three types of different entries under Wether as
# 1.Sunny
# 2. Overcast
# 3. Rainy

# There are three types of different entries under Temperature as
# 1.Hot
# 2. Cold
# 3. Mild

# Design machine learning application which follows below steps as

# Step 1:
# Get Data
# Load data from MarvellousInfosystems_PlayPredictor.csv file into python application.

# Step 2:
# Clean, Prepare and Manipulate data
# As we want to use the above data into machine learning application we have prepare
# that in the format which is accepted by the algorithms.
# As our dataset contains two features as Wether and Temperature. We have to replace
# each string field into numeric constants by using LabelEncoder from processing module
# of sklearn.

# Step 3:
# Train Data
# Now we want to train our data for that we have to select the Machine learning algorithm.
# For that we select K Nearest Neighbour algorithm.
# use fit method for training purpose. For training use whole dataset.

# Step 4:
# Test Data
# After successful training now we can test our trained data by passing some value of
# wether and temperature.
# As we are using KNN algorithm use value of K as 3.
# After providing the values check the result and display on screen.
# Result may be Yes or No.

# Step 5:
# Calculate Accuracy
# Write one function as CheckAccuracy() which calculate the accuracy of our algorithm.
# For calculating the accuracy divide the dataset into two equal parts as Training data and
# Testing data.
# Calculate Accuracy by changing value of K.

import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# ==========================================================
# Step 1: Get Data
# ==========================================================

# Read CSV from current path
df = pd.read_csv("MarvellousInfosystems_PlayPredictor.csv")

print("Dataset:")
print(df)

print("\nColumns:")
print(df.columns)


# ==========================================================
# Step 2: Clean, Prepare and Manipulate Data
# ==========================================================

# Create LabelEncoder
le_weather = LabelEncoder()
le_temperature = LabelEncoder()
le_play = LabelEncoder()

# Convert string values into numeric values
df["Wether"] = le_weather.fit_transform(df["Wether"])
df["Temperature"] = le_temperature.fit_transform(df["Temperature"])
df["Play"] = le_play.fit_transform(df["Play"])


print("\nAfter Label Encoding:")
print(df)


# Features
X = df[["Wether", "Temperature"]]

# Target
Y = df["Play"]


# ==========================================================
# Step 3: Train Data
# ==========================================================

# K = 3
model = KNeighborsClassifier(n_neighbors=3)

# Train using complete dataset
model.fit(X, Y)


# ==========================================================
# Step 4: Test Data
# ==========================================================

print("\nEnter Weather and Temperature")

weather = input("Enter Weather (Sunny/Overcast/Rainy): ")
temperature = input("Enter Temperature (Hot/Mild/Cold): ")


# Convert user input into numeric values
weather_encoded = le_weather.transform([weather])[0]
temperature_encoded = le_temperature.transform([temperature])[0]


# Create input data
new_data = [[weather_encoded, temperature_encoded]]


# Predict
prediction = model.predict(new_data)


# Convert numeric prediction back to Yes/No
result = le_play.inverse_transform(prediction)

print("\nPredicted Result:", result[0])


# ==========================================================
# Step 5: Calculate Accuracy
# ==========================================================

def CheckAccuracy(k):

    # Divide dataset into training and testing data
    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.5,
        random_state=42
    )

    # Create KNN model
    model = KNeighborsClassifier(n_neighbors=k)

    # Train model
    model.fit(X_train, Y_train)

    # Predict testing data
    Y_pred = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(Y_test, Y_pred)

    return accuracy


print("\nAccuracy Results:")

for k in [1, 3, 5, 7]:
    
    accuracy = CheckAccuracy(k)

    print(
        "K =", k,
        "Accuracy =", round(accuracy * 100, 2), "%"
    )