#seaborn practice for real estate
import seaborn as sns
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('RealEstate-USA.csv',delimiter=",")

print(df)
df = df.head(50)
sns.lineplot(data=df , x="city" , y="price")
plt.show()
#themes
sns.set_theme(style='dark')
sns.lineplot(data=df, x="city", y="price")
plt.show()

sns.set_theme(style='darkgrid')
sns.lineplot(data=df, x="city", y="price")
plt.show()

sns.set_theme(style="ticks")
sns.lineplot(data=df, x="city",y="price")
plt.show()

sns.set_theme(style="white")
sns.lineplot(data=df, x="city", y="price")

read = input("Wait for me....")

#scatterplot
sns.scatterplot(data=df, x="street", y="bed")
plt.show()

# Display the plot2
read = input("Wait for me....")

#relplot
sns.relplot(data=df , x="bed" , y="price")
plt.show()

# Display the plot
read = input("Wait for me....")

#boxplot
sns.boxplot(data=df , x="zip_code" , y="state")
plt.show()

sns.set_theme(style='dark')
sns.boxplot(data=df, x="zip_code", y="state")
plt.show()

# Display the plot
read = input("Wait for me....")

#heatmap
sns.heatmap(data=df ,x="price" , y="bed")
plt.show()



