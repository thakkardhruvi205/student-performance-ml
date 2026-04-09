import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("housing.csv")

# Features & Target
X = data[['sqft_living', 'bedrooms', 'bathrooms']]
y = data['price']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

print("Sample Predictions:", predictions[:5])

import seaborn as sns
import matplotlib.pyplot as plt

sns.scatterplot(x='sqft_living', y='price', data=data)
plt.title("Area vs Price")
plt.show()