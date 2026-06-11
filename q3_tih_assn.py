import pandas as pd

# Load dataset
df_sales = pd.read_csv('sales.csv')

# =========================================================================
# Task 1 & 2: Overall Holiday vs. Non-Holiday Impact
# =========================================================================
overall_stats = df_sales.groupby('is_holiday')['weekly_sales'].mean().reset_index()

non_holiday_avg = overall_stats[overall_stats['is_holiday'] == 0]['weekly_sales'].values[0]
holiday_avg = overall_stats[overall_stats['is_holiday'] == 1]['weekly_sales'].values[0]

# Calculate percentage increase
pct_change = ((holiday_avg - non_holiday_avg) / non_holiday_avg) * 100

print("=== OVERALL HOLIDAY IMPACT ON SALES ===")
print(f"Average Weekly Sales (Regular Weeks): ${non_holiday_avg:,.2f}")
print(f"Average Weekly Sales (Holiday Weeks): ${holiday_avg:,.2f}")
print(f"Percentage Revenue Shift on Holidays: +{pct_change:.2f}%\n")


# =========================================================================
# Task 3: Departmental Deep Dive (Who benefits most?)
# =========================================================================
# Unstack regular vs holiday averages by department
dept_holiday_stats = df_sales.groupby(['department', 'is_holiday'])['weekly_sales'].mean().unstack()
dept_holiday_stats.columns = ['regular_weeks_avg', 'holiday_weeks_avg']

# Calculate the exact percentage increase per department
dept_holiday_stats['pct_increase'] = (
    (dept_holiday_stats['holiday_weeks_avg'] - dept_holiday_stats['regular_weeks_avg']) 
    / dept_holiday_stats['regular_weeks_avg']
) * 100

# Extract top performing departments
top_beneficiaries = dept_holiday_stats.sort_values(by='pct_increase', ascending=False).head(5)

print("=== TOP 5 DEPARTMENTS BENEFITING MOST FROM HOLIDAYS ===")
print(top_beneficiaries.round(2))