import pandas as pd

# Load the dataset to ensure the script runs independently
df = pd.read_csv('traffic_violations.csv')

# --- Part 1: Create a Pivot Table and Normalize it ---
print("\n--- Answer for Part 1: Create and Normalize Pivot Table ---")

# Create the pivot table
# We use 'plate_number' to count the occurrences, and set aggfunc='count'
pivot_counts = df.pivot_table(
    values='plate_number', 
    index='city', 
    columns='violation_type', 
    aggfunc='count'
)

# Normalize the table so that the sum of each row is 100%
# .div() divides each element by the row sum (axis=1 specifies row-wise summation for division along axis=0)
pivot_normalized = pivot_counts.div(pivot_counts.sum(axis=1), axis=0) * 100

print("Normalized Pivot Table (Rows sum to 100%):")
print(pivot_normalized.round(2).head()) # Rounded to 2 decimal places for better readability


# --- Part 2: Find the violation type with the highest share per city ---
print("\n--- Answer for Part 2: Highest Violation Type Share per City ---")

# .idxmax(axis=1) returns the column name with the maximum value for each row
highest_violation_share = pivot_normalized.idxmax(axis=1).reset_index()
highest_violation_share.columns = ['city', 'most_frequent_violation']

print("The violation type with the highest share in each city:")
print(highest_violation_share)