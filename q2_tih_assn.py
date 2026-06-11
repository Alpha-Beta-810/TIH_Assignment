import pandas as pd

# Load dataset
df_sales = pd.read_csv('sales.csv')

# Compute baseline metrics per department
dept_stats = df_sales.groupby('department')['weekly_sales'].agg(['mean', 'std']).reset_index()
dept_stats.rename(columns={'std': 'standard_deviation'}, inplace=True)

# Compute Coefficient of Variation (CV)
dept_stats['coefficient_of_variation'] = dept_stats['standard_deviation'] / dept_stats['mean']


# =========================================================================
# LENS 1: Absolute Volatility (Using Standard Deviation Alone)
# =========================================================================
stable_by_sd = dept_stats.sort_values(by='standard_deviation', ascending=True).head(5)
volatile_by_sd = dept_stats.sort_values(by='standard_deviation', ascending=False).head(5)

print("=== METHOD 1: ABSOLUTE VOLATILITY (STANDARD DEVIATION) ===")
print("\nTop 5 Highly Stable Departments (Lowest Raw Dollar Variance):")
print(stable_by_sd[['department', 'standard_deviation', 'mean']].round(2).to_string(index=False))

print("\nTop 5 Highly Volatile Departments (Highest Raw Dollar Variance):")
print(volatile_by_sd[['department', 'standard_deviation', 'mean']].round(2).to_string(index=False))
print("\n" + "="*60 + "\n")


# =========================================================================
# LENS 2: Relative Volatility (Using Coefficient of Variation Alone)
# =========================================================================
stable_by_cv = dept_stats.sort_values(by='coefficient_of_variation', ascending=True).head(5)
volatile_by_cv = dept_stats.sort_values(by='coefficient_of_variation', ascending=False).head(5)

print("=== METHOD 2: RELATIVE VOLATILITY (COEFFICIENT OF VARIATION) ===")
print("\nTop 5 Highly Stable Departments (Lowest Proportional Variance):")
print(stable_by_cv[['department', 'coefficient_of_variation', 'standard_deviation', 'mean']].round({'mean': 2, 'standard_deviation': 2, 'coefficient_of_variation': 4}).to_string(index=False))

print("\nTop 5 Highly Volatile Departments (Highest Proportional Variance):")
print(volatile_by_cv[['department', 'coefficient_of_variation', 'standard_deviation', 'mean']].round({'mean': 2, 'standard_deviation': 2, 'coefficient_of_variation': 4}).to_string(index=False))