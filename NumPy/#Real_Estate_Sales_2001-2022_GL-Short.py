#Seaborn Real_Estate_Sales_2001-2022_GL-Short.csv
import seaborn as sns
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Real_Estate_Sales_2001-2022_GL-Short.csv',delimiter=",")

print(df)
df = df.head(50)
sns.lineplot(data=df , x="Town" , y="Address")
plt.show()
#themes
sns.set_theme(style='dark')
sns.lineplot(data=df, x="Town", y="Address")
plt.show()

sns.set_theme(style='darkgrid')
sns.lineplot(data=df, x="Town", y="Address")
plt.show()

sns.set_theme(style="ticks")
sns.lineplot(data=df, x="Town",y="Address")
plt.show()

sns.set_theme(style="white")
sns.lineplot(data=df, x="Town", y="Address")

read = input("Wait for me....")

#scatterplot
sns.scatterplot(data=df, x="Sale Amount", y="Sales Ratio")
plt.show()

# Display the plot2
read = input("Wait for me....")

#relplot
sns.relplot(data=df , x="Property Type" , y="List Year")
plt.show()

# Display the plot
read = input("Wait for me....")

#catplot
sns.catplot(data=df , x="Date Recorded" , y="Sale Amount")
plt.show()

sns.set_theme(style='dark')
sns.boxplot(data=df, x="Date Recorded", y="Sale Amount")
plt.show()

# Display the plot
read = input("Wait for me....")

#swarmplot
sns.swarmplot(data=df ,x="Serial Number" , y="Sales Ratio")
plt.show()