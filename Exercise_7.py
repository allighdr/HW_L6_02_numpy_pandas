import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('traffic_violations.csv')

# Prepare the Summary DataFrame for cities required for Exercise 7
city_summary = df.groupby('city').agg(
    total_violations=('plate_number', 'count'),
    avg_fine_amount=('fine_amount_irr', 'mean'),
    paid_percentage=('paid', lambda x: x.mean() * 100)
).reset_index()

# --- Answer for Exercise 7: Plotting Scatter Plot ---
print("\n--- Answer for Exercise 7: Plotting Scatter Plot ---")

fig, ax = plt.subplots(figsize=(12, 8))

# Scale down the marker sizes so they fit well on the plot
marker_sizes = city_summary['total_violations'] / 200

# Plotting the scatter plot
ax.scatter(
    x=city_summary['avg_fine_amount'], 
    y=city_summary['paid_percentage'], 
    s=marker_sizes, 
    color='darkorange', 
    alpha=0.6, 
    edgecolors='white',
    linewidth=1.5
)

# Adding annotations (city names) to each data point
for index, row in city_summary.iterrows():
    ax.annotate(
        row['city'], 
        (row['avg_fine_amount'], row['paid_percentage']),
        xytext=(0, 5), # Offset the text slightly above the point
        textcoords='offset points',
        ha='center', # Horizontally center the text
        fontsize=10,
        fontweight='bold'
    )

# Adding labels, title, and grid
ax.set_title('City Violations: Avg Fine vs. Paid Rate', fontsize=14, fontweight='bold')
ax.set_xlabel('Average Fine Amount (IRR)', fontsize=12)
ax.set_ylabel('Paid Percentage (%)', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('exercise_7_scatter.png')
print("Scatter plot created successfully and saved as 'exercise_7_scatter.png'.")