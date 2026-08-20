import pandas as pd

# Load the dataset and convert the datetime column to a proper pandas datetime object
df = pd.read_csv('traffic_violations.csv')
df['violation_datetime'] = pd.to_datetime(df['violation_datetime'])

# --- Part 1: Calculate the number of violations monthly ---
print("\n--- Answer for Part 1: Monthly Violations Count ---")

# Setting the datetime column as the DataFrame index for time-series operations
df_time_indexed = df.set_index('violation_datetime')

# Resampling the data by Month ('ME' stands for Month-End frequency) and getting the size of each group
monthly_counts = df_time_indexed.resample('ME').size()

# Optional: Format the index to display only Year-Month for better readability
monthly_counts.index = monthly_counts.index.strftime('%Y-%m')

print("Monthly violations count (Showing first 5 months):")
print(monthly_counts.head())


# --- Part 2: Calculate the number of violations by hour of the day ---
print("\n--- Answer for Part 2: Violations Count by Hour ---")

# Using the .dt accessor to extract the hour from the datetime column and grouping by it
hourly_counts = df.groupby(df['violation_datetime'].dt.hour).size()

# Renaming the index axis for clarity
hourly_counts.index.name = 'Hour of Day'

print("Violations count per hour:")
print(hourly_counts)


# --- Part 3: Determine the hour with the most violations ---
print("\n--- Answer for Part 3: Hour with Maximum Violations ---")

# idxmax() returns the index (the hour) corresponding to the maximum value in the series
peak_hour = hourly_counts.idxmax()
peak_violations = hourly_counts.max()

print(f"The most violations occur at hour {peak_hour}:00, with a total of {peak_violations} violations.")