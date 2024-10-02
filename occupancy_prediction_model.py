import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load data
data = pd.read_csv('data/historical_booking_data.csv')

# Preprocess data
X = data.drop('occupancy_rate', axis=1)
y = data['occupancy_rate']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'models/occupancy_prediction_model.pkl')
