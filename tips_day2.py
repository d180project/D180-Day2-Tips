# --------------------------------------------------------
# Day 2 Challenge - Restaurant Tips Analysis
# Author: R (180-Day Challenge)
# --------------------------------------------------------

import pandas as pd  # Pandas identity format

# Step 1: Load dataset
df = pd.read_csv("tips_day2.csv")

# Step 2: Preview data
print("👀 First 5 rows of the dataset:")
print(df.head())   # first 5 rows
print("-" * 50)

# Step 3: Basic statistics (summary)
# Store results in a dictionary

summary = {}

# --- 'Total_Bill' column ---
summary['Total_Bill_Mean']   = df['Total_Bill'].mean()    # average
summary['Total_Bill_Median'] = df['Total_Bill'].median()  # middle value
summary['Total_Bill_Mode']   = df['Total_Bill'].mode()[0] # most common

summary['Total_Bill_Min']    = df['Total_Bill'].min()     # smallest
summary['Total_Bill_Max']    = df['Total_Bill'].max()     # largest
summary['Total_Bill_Std']    = df['Total_Bill'].std()     # spread

# --- 'Tip' column ---
summary['Tip_Mean']   = df['Tip'].mean()
summary['Tip_Median'] = df['Tip'].median()
summary['Tip_Mode']   = df['Tip'].mode()[0]

# Step 4: Group and count
# Records per day
day_counts = df['Day'].value_counts()

# Records by gender
sex_counts = df['Sex'].value_counts()

# Step 5: Save to CSV
summary_df = pd.DataFrame([summary])  # wrap dict in DataFrame
summary_df.to_csv("tips_day2_summary.csv", index=False)

day_counts.to_csv("tips_day2_day_counts.csv")
sex_counts.to_csv("tips_day2_sex_counts.csv")

# Step 6: Notify user
print("\n✅ Done! Results saved as:")
print("  - tips_day2_summary.csv (summary)")
print("  - tips_day2_day_counts.csv (day counts)")
print("  - tips_day2_sex_counts.csv (gender counts)")