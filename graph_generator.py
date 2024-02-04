import matplotlib.pyplot as plt
import pandas

df = pandas.read_csv('dit-cost-of-living/costs-growth.csv')

# Data
years = df['Year'].to_numpy()
salary_values = df['Salary'].to_numpy()
inflation_values = df['CPI'].to_numpy()
ahpra_values = df['AHPRA'].to_numpy()
rent_values = df['Rent'].to_numpy()

# Plots
plt.plot(years, salary_values, marker='o', label="DiT Wages", color="#e84118")
plt.plot(years, inflation_values, marker='o', label="Inflation", color="#0097e6")
plt.plot(years, ahpra_values, marker='o', label='AHPRA Fees', color="#44bd32")
plt.plot(years, rent_values, marker='o', label="Perth Rent", color="#5f27cd")

# Set font to Rockwell
plt.rcParams['font.family'] = 'Rockwell'
plt.rcParams['font.weight'] = 'bold'
# plt.rcParams['font.size'] = 'large'

# Set x-axis labels
plt.xticks(years)

# Set axis labels
# plt.xlabel('Years')
plt.ylabel('Growth Since 2018 (%)', fontdict={'family':'Rockwell', 'size':'larger', 'weight':'bold'})

# Set plot title
# plt.title('DiT Wage Growth Relative to Various Indices of Living Costs')

# Remove borders on right and top sides
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)

# Show legend
legend = plt.legend(fontsize='large')
legend.get_frame().set_linewidth(0) # remove border
legend.get_frame().set_alpha(0)

# Add value labels to the final data point in each series
last_index = len(years) - 1
padding = 2

for s in [salary_values, inflation_values, ahpra_values, rent_values]:
    x = years[last_index]
    y = s[last_index] + padding
    value = str(round(s[last_index], 1))
    text = f'+{value}%'
    plt.text(x, y, text, ha='center', va='bottom')

# Save the figure as SVG
plt.savefig('_site/attachments/dit-pay-trends.svg', bbox_inches='tight', transparent="True", pad_inches=0)