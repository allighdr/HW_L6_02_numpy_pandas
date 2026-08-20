import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Number of rows set to 1 million as requested
n_rows = 1000000

print(
    'Generating 1,000,000 records with high variety. Please wait a moment...'
)

# 1. Generate random datetime values distributed across multiple years
start_ts = pd.to_datetime('2024-01-01').timestamp()
end_ts = pd.to_datetime('2026-12-31').timestamp()
random_timestamps = np.random.uniform(start_ts, end_ts, n_rows)
dates = pd.to_datetime(random_timestamps, unit='s')

# 2. Generate diverse plate numbers to reduce repetition
rand_l1 = np.random.choice(
    ['AB', 'CD', 'EF', 'GH', 'XY', 'IR', 'ZZ', 'LK', 'MN', 'PR', 'QW', 'ST'],
    n_rows,
)
rand_nums = np.random.randint(100, 999, n_rows)
rand_l2 = np.random.choice(
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M'], n_rows
)
rand_nums2 = np.random.randint(10, 99, n_rows)

plate_numbers = [
    f'{l1}-{num}-{l2}{num2}'
    for l1, num, l2, num2 in zip(rand_l1, rand_nums, rand_l2, rand_nums2)
]

# Convert to pandas Series and make ~30% of them lowercase to test requirement 4 properly
plate_series = pd.Series(plate_numbers)
lower_mask = np.random.rand(n_rows) < 0.3
plate_series[lower_mask] = plate_series[lower_mask].str.lower()

# 3. Expanded categories for cities, vehicle types, and violations
cities_list = [
    'Tehran',
    'Isfahan',
    'Shiraz',
    'Tabriz',
    'Mashhad',
    'Karaj',
    'Ahvaz',
    'Qom',
    'Kermanshah',
    'Rasht',
]
cities = np.random.choice(cities_list, size=n_rows)

vehicle_types_list = [
    'Car',
    'SUV',
    'Truck',
    'Motorcycle',
    'Van',
    'Bus',
    'Taxi',
    'Trailer',
]
vehicle_types = np.random.choice(vehicle_types_list, size=n_rows)

violation_types_list = [
    'Speeding',
    'Illegal Parking',
    'Red Light',
    'No Entry',
    'Wrong Way',
    'Unsafe Lane Change',
]
violation_types = np.random.choice(violation_types_list, size=n_rows)

# 4. Fines and payment status
fine_amounts = np.random.choice(
    [500000, 1000000, 1500000, 2000000, 2500000, 3000000, 4000000, 5000000],
    size=n_rows,
)
paid_status = np.random.choice([True, False], size=n_rows, p=[0.65, 0.35])

# 5. Speeds
speed_limits = np.random.choice([50, 60, 80, 90, 100, 110, 120], size=n_rows)
measured_speeds = speed_limits + np.random.randint(-5, 60, size=n_rows)

# Create the final DataFrame
df = pd.DataFrame({
    'violation_datetime': dates,
    'plate_number': plate_series,
    'speed_limit_kmh': speed_limits,
    'measured_speed_kmh': measured_speeds,
    'city': cities,
    'vehicle_type': vehicle_types,
    'violation_type': violation_types,
    'fine_amount_irr': fine_amounts,
    'paid': paid_status,
})

# Save to CSV (This will create a file of around 80-100 MB)
df.to_csv('traffic_violations.csv', index=False)
print("Successfully generated 1,000,000 records in 'traffic_violations.csv'!")