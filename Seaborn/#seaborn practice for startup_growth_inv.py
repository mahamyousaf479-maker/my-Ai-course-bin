#seaborn practice for startup_growth_investment_data.csv
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('startup_growth_investment_data.csv' , delimiter=",")
print(df)
df = df.head(50)
sns.lineplot(data=df , x="Country" , y="Industry")
plt.show()
#themes
sns.set_theme(style='dark')
sns.lineplot(data=df, x="Country", y="Industry")
plt.show()

sns.set_theme(style='darkgrid')
sns.lineplot(data=df, x="Country", y="Industry")
plt.show()

sns.set_theme(style="ticks")
sns.lineplot(data=df, x="Country",y="Industry")
plt.show()

sns.set_theme(style="white")
sns.lineplot(data=df, x="Country", y="Industry")

read = input("Wait for me....")

#barplot
sns.barplot(data=df, x="Funding Rounds", y="Investment Amount (USD)")
plt.show()

# Display the plot2
read = input("Wait for me....")

#boxplot
sns.boxplot(data=df , x="Year Founded" , y="Number of Investors")
plt.show()

sns.set_theme(style='dark')
sns.boxplot(data=df, x="Year Founded", y="Number of Investors")
plt.show()

# Display the plot
read = input("Wait for me....")

#catplot
sns.catplot(data=df ,x="Investment Amount (USD)" , y="Valuation (USD)")
plt.show()
