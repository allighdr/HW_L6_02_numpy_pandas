import pandas as pd

# --- Question 1: Load the dataset using Pandas ---
print("--- Answer for Question 1: Load dataset ---")
df = pd.read_csv('traffic_violations.csv')
print("Dataset loaded successfully. First 3 rows:")
print(df.head(3))

# --- Question 2: Convert violation_datetime to datetime type ---
print("\n--- Answer for Question 2: Convert violation_datetime to datetime ---")
df['violation_datetime'] = pd.to_datetime(df['violation_datetime'])
print("Data type of violation_datetime:", df['violation_datetime'].dtype)

# --- Question 3: Create three new columns (Year, Month, Hour) ---
print("\n--- Answer for Question 3: Create Year, Month, and Hour columns ---")
df['Year'] = df['violation_datetime'].dt.year
df['Month'] = df['violation_datetime'].dt.month
df['Hour'] = df['violation_datetime'].dt.hour
print("New columns (Year, Month, Hour) created. Sample data:")
print(df[['violation_datetime', 'Year', 'Month', 'Hour']].head(3))

# --- Question 4: Standardize plate_number to uppercase ---
print("\n--- Answer for Question 4: Standardize plate_number to uppercase ---")
df['plate_number'] = df['plate_number'].str.upper()
print("Plate numbers standardized to uppercase. Sample data:")
print(df['plate_number'].head(3))

# --- Question 5: Create speed_over_limit column ---
print("\n--- Answer for Question 5: Create speed_over_limit column ---")
df['speed_over_limit'] = df['measured_speed_kmh'] - df['speed_limit_kmh']
print("speed_over_limit column created. Sample data:")
print(df[['measured_speed_kmh', 'speed_limit_kmh', 'speed_over_limit']].head(3))