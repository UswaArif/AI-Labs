import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load and Preprocess the dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
df = pd.read_csv(url, header = None, names = column_names)

# Remove null and duplicate values
df = df.dropna()
df = df.drop_duplicates()

# Step 2: Show scatter plot of the dataset
plt.scatter(df['sepal_length'], df['sepal_width'])
plt.title('Scatter Plot of Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.show()

# Step 3: Split the dataset into training and testing (75% - 25%)
train_size = int(0.75 * len(df))
train_data = df[:train_size]
test_data = df[train_size:]

# Step 4: Implement Linear Regression Model
def linear_regression_fit(X, y, learning_rate = 0.01, epochs = 1000):
    m, b = 0, 0  # initial values for slope and intercept
    n = len(X)

    for epoch in range(epochs):
        y_pred = m * X + b
        mse = np.mean((y_pred - y)**2)
        gradient_m = (-2/n) * np.sum(X * (y - y_pred))
        gradient_b = (-2/n) * np.sum(y - y_pred)
        m = m - learning_rate * gradient_m
        b = b - learning_rate * gradient_b

    return m, b

# Step 5: Fit the model on training dataset
X_train = train_data['sepal_length'].values
y_train = train_data['sepal_width'].values

m, b = linear_regression_fit(X_train, y_train)

# Step 6: Perform binary classification on the test dataset
X_test = test_data['sepal_length'].values
y_test = test_data['sepal_width'].values
y_pred = m * X_test + b

# Step 7: Find mean square error
mse = np.mean((y_pred - y_test)**2)
print(f"Mean Squared Error: {mse}")
