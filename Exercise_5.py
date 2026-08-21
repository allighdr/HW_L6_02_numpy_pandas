import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset and prepare the datetime index
df = pd.read_csv('traffic_violations.csv')
df['violation_datetime'] = pd.to_datetime(df['violation_datetime'])
df_time_indexed = df.set_index('violation_datetime')

# Calculate monthly counts (using 'ME' for Month-End frequency)
monthly_counts = df_time_indexed.resample('ME').size()

# --- Answer for Exercise 5: Create a figure with 3 subplots and plot the first one ---
print("\n--- Answer for Exercise 5: Plotting Monthly Violations ---")

# Create a figure containing 3 subplots (3 rows, 1 column)
# Using a larger figsize to ensure all 3 subplots will have enough space
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(12, 18))

# 1. Line chart of violations over time (monthly) on the first subplot (axes[0])
monthly_counts.plot(kind='line', ax=axes[0], color='dodgerblue', marker='o', linewidth=2)

# 2. Add Title
axes[0].set_title('Number of Traffic Violations Over Time (Monthly)', fontsize=14, fontweight='bold')

# 3. Add Axis Labels
axes[0].set_xlabel('Date', fontsize=12)
axes[0].set_ylabel('Total Violations', fontsize=12)

# 4. Enable Grid
axes[0].grid(True, linestyle='--', alpha=0.7)

# 5. Add Annotation on the month with the highest violations
max_month = monthly_counts.idxmax()
max_value = monthly_counts.max()

# The annotation points to (max_month, max_value) and places the text slightly above it
axes[0].annotate(
    f'Highest: {max_value}', 
    xy=(max_month, max_value), 
    xytext=(max_month, max_value + (max_value * 0.05)), # Offset text vertically
    arrowprops=dict(facecolor='red', shrink=0.05, width=2, headwidth=8),
    fontsize=11,
    color='red',
    ha='center' # Horizontal alignment
)

print("Subplot 1 (Monthly Violations Line Chart) created successfully with all requested elements.")
print("The other 2 subplots are created and ready for the next exercises.")

# Adjust layout so subplots do not overlap
plt.tight_layout()

# Save the figure to a file (Recommended for scripting environments)
plt.savefig('exercise_5_plot.png')
print("Plot saved as 'exercise_5_plot.png'.")

# Uncomment the line below if you want to display the plot in an interactive window
# plt.show()