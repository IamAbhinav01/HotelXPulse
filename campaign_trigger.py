import pandas as pd
import joblib

# Load models
occupancy_model = joblib.load('models/occupancy_prediction_model.pkl')

# Load data
data = pd.read_csv('data/historical_booking_data.csv')

# Predict occupancy
predicted_occupancy = occupancy_model.predict(data)

# Trigger campaign if occupancy is low
if predicted_occupancy.mean() < 50:  # Example threshold
    print("Triggering marketing campaign...")
    # Add code to trigger campaign
