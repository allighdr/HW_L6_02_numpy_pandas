import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('traffic_violations.csv')

# Prepare the required column for Exercise 6
df['speed_over_limit'] = df['measured_speed_kmh'] - df['speed_limit_kmh']

# --- Answer for Exercise 6: Plotting Histogram ---
print("\n--- Answer for Exercise 6: Plotting Histogram ---")

fig, ax = plt.subplots(figsize=(10, 6))

# Plotting the histogram
# bins=30: appropriate number of bins
# color: custom color (purple)
# label: required for the legend
ax.hist(
    df['speed_over_limit'], 
    bins=30, 
    color='purple', 
    edgecolor='black', 
    alpha=0.7, 
    label='Speed Over Limit'
)

# Adding labels, title, and legend
ax.set_title('Distribution of Speed Over Limit', fontsize=14, fontweight='bold')
ax.set_xlabel('Speed Over Limit (km/h)', fontsize=12)
ax.set_ylabel('Frequency (Number of Violations)', fontsize=12)

# Enable legend
ax.legend() 

plt.tight_layout()
plt.savefig('exercise_6_histogram.png')
print("Histogram created successfully and saved as 'exercise_6_histogram.png'.")