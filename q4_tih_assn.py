import pandas as pd

# Load dataset
df_sales = pd.read_csv('sales.csv')

# Ensure the date column is parsed correctly as a datetime object
df_sales['date'] = pd.to_datetime(df_sales['date'])

# Task 1: Extract month number and full month name from the date column
df_sales['month'] = df_sales['date'].dt.month
df_sales['month_name'] = df_sales['date'].dt.strftime('%B')

# Task 2: Compute average weekly sales for each month
# (We also aggregate total sales to provide complete visibility)
monthly_stats = df_sales.groupby(['month', 'month_name'])['weekly_sales'].agg(
    average_sales='mean',
    total_sales='sum'
).reset_index()

# Sort by average sales in descending order to easily evaluate performance shifts
monthly_stats_sorted = monthly_stats.sort_values(by='average_sales', ascending=False)

print("--- MONTHLY SALES TREND ANALYSIS ---")
print(monthly_stats_sorted.round(2).to_string(index=False))

# Task 3: Determine the highest and lowest sales months
highest_month = monthly_stats_sorted.iloc[0]
lowest_month = monthly_stats_sorted.iloc[-1]

print("\n--- SEASONAL EXTREMES ---")
print(f"Highest Sales Month: {highest_month['month_name']} (Average Weekly Sales: ${highest_month['average_sales']:,.2f})")
print(f"Lowest Sales Month:  {lowest_month['month_name']} (Average Weekly Sales: ${lowest_month['average_sales']:,.2f})")