from sklearn.linear_model import LinearRegression

# Training data
# Study hours
X = [[1], [2], [3], [4], [5], [6], [7], [8]]

# Marks obtained
y = [35, 40, 50, 55, 65, 70, 80, 90]

# Create ML model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Get input from user
hours = float(input("Enter study hours: "))

# Predict marks
prediction = model.predict([[hours]])

print("Predicted Marks:", round(prediction[0], 2))
