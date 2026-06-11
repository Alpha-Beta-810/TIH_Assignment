import pandas as pd

# Load the dataset
df_sales = pd.read_csv('sales.csv')

# Aggregate total sales per store to establish rankings
store_sales = df_sales.groupby('store_id')['weekly_sales'].sum().reset_index()
store_sales.rename(columns={'weekly_sales': 'total_sales'}, inplace=True)

# Rank stores by total revenue (highest to lowest)
ranked_stores = store_sales.sort_values(by='total_sales', ascending=False).reset_index(drop=True)
ranked_stores['rank'] = ranked_stores.index + 1

# Extract the cohort boundary targets (top 5 and bottom 5 stores)
top_5_stores = ranked_stores.head(5)
bottom_5_stores = ranked_stores.tail(5)

# ==========================================================
# OP 1: Rank stores by total revenue (Top 5 & Bottom 5)
# ==========================================================
print("--- OP 1: Ranked Stores by Total Revenue ---")
print("Top 5 Stores:")
print(top_5_stores.to_string(index=False))
print("\nBottom 5 Stores:")
print(bottom_5_stores.to_string(index=False))
print("\n")

# ==========================================================
# OP 2: Compare average sales per department within cohorts
# ==========================================================
# Build the ordered target store list maintaining revenue rank order
ordered_store_ids = pd.concat([top_5_stores, bottom_5_stores])['store_id'].tolist()

# Filter master transactional data for these specific cohorts
cohort_transactions = df_sales[df_sales['store_id'].isin(ordered_store_ids)]

# Compute chronological mean sales per department
dept_averages = cohort_transactions.groupby(['store_id', 'department'])['weekly_sales'].mean().reset_index()
dept_averages.rename(columns={'weekly_sales': 'average_weekly_sales'}, inplace=True)

# Pivot flat data into a cross-operational matrix
pivoted_comparison = dept_averages.pivot(
    index='department', 
    columns='store_id', 
    values='average_weekly_sales'
).fillna(0.0)

# Explicitly sort columns based on the total revenue rank sequence
pivoted_comparison_ranked = pivoted_comparison.reindex(columns=ordered_store_ids)

# Filter down to a core sample of departments (e.g., 1 to 5) for cleaner reporting
target_departments = [1, 2, 3, 4, 5]
filtered_pivot = pivoted_comparison_ranked.loc[target_departments]

print("--- OP 2: Departmental Average Weekly Sales Comparison (Ranked Columns) ---")
print(filtered_pivot.round(2))