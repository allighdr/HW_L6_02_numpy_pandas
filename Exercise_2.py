import pandas as pd

# Load the dataset and prepare the required column from Exercise 1
# This ensures the script runs independently without the NameError
df = pd.read_csv('traffic_violations.csv')
df['speed_over_limit'] = df['measured_speed_kmh'] - df['speed_limit_kmh']

# --- Question 1: Summary DataFrame for each city ---
print("\n--- Answer for Question 1: Summary DataFrame for each city ---")
city_summary = df.groupby('city').agg(
    total_violations=('plate_number', 'count'),
    avg_fine_amount=('fine_amount_irr', 'mean'),
    paid_percentage=('paid', lambda x: x.mean() * 100)
).reset_index()

print("City summary created successfully. First 5 rows:")
print(city_summary.head())

# --- Question 2: Summary DataFrame for each vehicle_type ---
print("\n--- Answer for Question 2: Summary DataFrame for each vehicle_type ---")
vehicle_summary = df.groupby('vehicle_type').agg(
    total_violations=('plate_number', 'count'),
    avg_speed_over_limit=('speed_over_limit', 'mean')
).reset_index()

print("Vehicle type summary created successfully:")
print(vehicle_summary)