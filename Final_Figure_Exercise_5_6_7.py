import pandas as pd
import matplotlib.pyplot as plt

# --- 1. Load Data and Prepare Required Columns ---
print("--- Loading data and preparing for the dashboard ---")
df = pd.read_csv('traffic_violations.csv')

# Prep for Ex 5: Datetime indexing & monthly counts
df['violation_datetime'] = pd.to_datetime(df['violation_datetime'])
df_time_indexed = df.set_index('violation_datetime')
monthly_counts = df_time_indexed.resample('ME').size()

# Prep for Ex 6: Speed over limit
df['speed_over_limit'] = df['measured_speed_kmh'] - df['speed_limit_kmh']

# Prep for Ex 7: City Summary
city_summary = df.groupby('city').agg(
    total_violations=('plate_number', 'count'),
    avg_fine_amount=('fine_amount_irr', 'mean'),
    paid_percentage=('paid', lambda x: x.mean() * 100)
).reset_index()


# --- 2. Create the Figure with 3 Subplots (Requested in Exercise 5) ---
print("\n--- Creating the Figure with 3 Subplots (Exercises 5, 6, and 7) ---")
# 3 rows, 1 column. High figsize to fit all nicely.
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(12, 18))


# =========================================================
# Subplot 1 (axes[0]): Line Chart (Exercise 5)
# =========================================================
monthly_counts.plot(kind='line', ax=axes[0], color='dodgerblue', marker='o', linewidth=2)
axes[0].set_title('Number of Traffic Violations Over Time (Monthly)', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Date', fontsize=12)
axes[0].set_ylabel('Total Violations', fontsize=12)
axes[0].grid(True, linestyle='--', alpha=0.7)

# Annotation for the highest month
max_month = monthly_counts.idxmax()
max_value = monthly_counts.max()
axes[0].annotate(
    f'Highest: {max_value}', 
    xy=(max_month, max_value), 
    xytext=(max_month, max_value + (max_value * 0.05)), 
    arrowprops=dict(facecolor='red', shrink=0.05, width=2, headwidth=8),
    fontsize=11, color='red', ha='center'
)


# =========================================================
# Subplot 2 (axes[1]): Histogram (Exercise 6)
# =========================================================
axes[1].hist(
    df['speed_over_limit'], 
    bins=30, 
    color='purple', 
    edgecolor='black', 
    alpha=0.7, 
    label='Speed Over Limit'
)
axes[1].set_title('Distribution of Speed Over Limit', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Speed Over Limit (km/h)', fontsize=12)
axes[1].set_ylabel('Frequency (Number of Violations)', fontsize=12)
axes[1].legend()


# =========================================================
# Subplot 3 (axes[2]): Scatter Plot (Exercise 7)
# =========================================================
marker_sizes = city_summary['total_violations'] / 200
axes[2].scatter(
    x=city_summary['avg_fine_amount'], 
    y=city_summary['paid_percentage'], 
    s=marker_sizes, 
    color='darkorange', 
    alpha=0.6, 
    edgecolors='white',
    linewidth=1.5
)

# City names annotations
for index, row in city_summary.iterrows():
    axes[2].annotate(
        row['city'], 
        (row['avg_fine_amount'], row['paid_percentage']),
        xytext=(0, 5), textcoords='offset points',
        ha='center', fontsize=10, fontweight='bold'
    )

axes[2].set_title('City Violations: Avg Fine vs. Paid Rate (Bubble Size = Total Violations)', fontsize=14, fontweight='bold')
axes[2].set_xlabel('Average Fine Amount (IRR)', fontsize=12)
axes[2].set_ylabel('Paid Percentage (%)', fontsize=12)
axes[2].grid(True, linestyle='--', alpha=0.5)

# --- 3. Finalize and Save ---
plt.tight_layout() # Prevents overlap between subplots
plt.savefig('FFinal_Figure_Exercise_5_6_7.png')
print("Dashboard containing all 3 subplots created and saved successfully as 'Final_Dashboard_Ex5_6_7.png'.")