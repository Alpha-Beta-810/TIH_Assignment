import pandas as pd

# Load dataset
df_sales = pd.read_csv('sales.csv')

# Step 1: Calculate the company's gross overall revenue across all stores and departments
total_network_revenue = df_sales['weekly_sales'].sum()

# Step 2: Group by store_id and department and sum up total sales
combination_sales = df_sales.groupby(['store_id', 'department'])['weekly_sales'].sum().reset_index()
combination_sales.rename(columns={'weekly_sales': 'total_combination_revenue'}, inplace=True)

# Step 3: Compute percentage contribution to the overall company revenue
combination_sales['percentage_contribution'] = (combination_sales['total_combination_revenue'] / total_network_revenue) * 100

# Rank the combinations from highest to lowest revenue generators
ranked_combinations = combination_sales.sort_values(by='total_combination_revenue', ascending=False).reset_index(drop=True)

# Separate top 5 and bottom 5 performers
top_5_units = ranked_combinations.head(5)
bottom_5_units = ranked_combinations.tail(5)

print(f"Grand Overall Revenue (All Stores & Depts): ${total_network_revenue:,.2f}\n")

print("--- TOP 5 REVENUE CONTRIBUTING COMBINATIONS ---")
print(top_5_units.round({'total_combination_revenue': 2, 'percentage_contribution': 4}).to_string(index=False))

print("\n--- BOTTOM 5 REVENUE CONTRIBUTING COMBINATIONS ---")
print(bottom_5_units.round({'total_combination_revenue': 2, 'percentage_contribution': 4}).to_string(index=False))