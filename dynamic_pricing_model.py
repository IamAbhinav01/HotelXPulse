import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load data
data = pd.read_csv('data/market_trends.csv')

# Preprocess data
X = data.drop('price', axis=1)
y = data['price']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, 'models/dynamic_pricing_model.pkl')
