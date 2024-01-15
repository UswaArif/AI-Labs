import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Step 1: Pre-processing
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names=names)

# Remove null and duplicate values
dataset = dataset.dropna()
dataset = dataset.drop_duplicates()

# Step 2: Show Scatter Plot
plt.scatter(dataset['sepal-length'], dataset['petal-width'])
plt.xlabel('Sepal Length')
plt.ylabel('Petal Width')
plt.title('Scatter Plot of Sepal Length vs Petal Width')
plt.show()

# Step 3: Splitting Train-Test Data
X_train, X_test, y_train, y_test = train_test_split(dataset['sepal-length'], dataset['petal-width'], test_size=0.25, random_state=42)

# Step 4: Fit the Model on Training Dataset
def gradient_descent(X, y, learning_rate, epochs):
    m, b = 0, 0  # Initial values for slope and intercept
    n = float(len(X))  # Number of elements in X
    
    for _ in range(epochs):
        y_pred = m * X + b  # Predicted values
        cost = (1/n) * sum([val**2 for val in (y - y_pred)])  # Cost function
        
        # Partial derivatives w.r.t. m and b
        dm = -(2/n) * sum(X * (y - y_pred))
        db = -(2/n) * sum(y - y_pred)
        
        m -= learning_rate * dm  # Update slope
        b -= learning_rate * db  # Update intercept
    
    return m, b

learning_rate = 0.01
epochs = 1000
slope, intercept = gradient_descent(X_train, y_train, learning_rate, epochs)

# Step 5: Perform Binary Classification on Test Dataset
y_pred_test = slope * X_test + intercept
threshold = 1.0  # Set a threshold for binary classification
y_pred_class = np.where(y_pred_test > threshold, 1, 0)

# Step 6: Find Mean Square Error
mse = np.mean((y_pred_test - y_test)**2)

print(f'Mean Square Error: {mse}')
