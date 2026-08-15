#seaborn practice for US Restaurants Dataset:
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('FastFoodRestaurants.csv' , delimiter=",")
print(df)
df = df.head(50)
sns.lineplot(data=df , x="city" , y="country")
plt.show()
#themes
sns.set_theme(style='dark')
sns.lineplot(data=df, x="city", y="country")
plt.show()

sns.set_theme(style='darkgrid')
sns.lineplot(data=df, x="city", y="country")
plt.show()

sns.set_theme(style="ticks")
sns.lineplot(data=df, x="city",y="country")
plt.show()

sns.set_theme(style="white")
sns.lineplot(data=df, x="city", y="country")

read = input("Wait for me....")

#scatterplot
sns.scatterplot(data=df, x="keys", y="country")
plt.show()

# Display the plot2
read = input("Wait for me....")

#relplot
sns.relplot(data=df , x="name" , y="province")
plt.show()

# Display the plot
read = input("Wait for me....")

#boxplot
sns.boxplot(data=df , x="latitude" , y="longitude")
plt.show()

sns.set_theme(style='dark')
sns.boxplot(data=df, x="latitude", y="longitude")
plt.show()

# Display the plot
read = input("Wait for me....")

#catplot
sns.catplot(data=df ,x="keys" , y="name")
plt.show()
