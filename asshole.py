import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("SAT__College_Board__2010_School_Level_Results_20240506.csv")

selected_cols = ['School Name', 'Critical Reading Mean', 'Mathematics Mean', 'Writing Mean']
df_selected = df[selected_cols]

# Calculate the total score
df_selected['Total Score'] = df_selected['Critical Reading Mean'] + df_selected['Mathematics Mean'] + df_selected['Writing Mean']

# Get the top 15 rows based on the total score
df_top15 = df_selected.nlargest(15, 'Total Score')

# Create a bar chart for the top 15 schools
plt.figure(figsize=(12, 8))
plt.bar(df_top15['School Name'], df_top15['Critical Reading Mean'], color='skyblue', label='Critical Reading')
plt.bar(df_top15['School Name'], df_top15['Mathematics Mean'], bottom=df_top15['Critical Reading Mean'], color='orange', label='Mathematics')
plt.bar(df_top15['School Name'], df_top15['Writing Mean'], bottom=df_top15['Critical Reading Mean']+df_top15['Mathematics Mean'], color='green', label='Writing')

plt.title('Top 15 Schools by Total SAT Score')
plt.xlabel('School Name')
plt.ylabel('Score')
plt.legend()
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save the chart as a JPG file
plt.savefig('top15_sat_scores.jpg', format='jpg', dpi=100)