#heart disease ML
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
import pickle


df=pd.read_csv("heart_disease_cleveland.csv")
print("Head", df.head(100))
print("Tail",df.tail(6))


print("isna",df.isna())
print(df.isnull().sum())
print(df.head())

print("df.shape:         " , df.shape)


print(df.dtypes)

print(df.columns)

print(df.shape)

print(df.info()) 



print(df.describe)  

print("Single_columns___")

single_column=df["ca"]
print(single_column)  
print("Multiple_column__")
Mutiple_columns=df[["thalach","chol"]]

print(Mutiple_columns)



print(df.columns.tolist())

coumn1=df["cp"]
print(coumn1)


print(".loc") 
second_row=df.loc[1]
print(second_row)
print("Multiple rows")


second_row2=df.loc[[1,4]]
print(second_row2)


print(df.loc[df["cp"]==1])


second_row4=df.loc[df["thalach"]=="150"]
print(second_row4)

second_row5=df.loc[df["age"]=="56"]
print(second_row5)

second_row6=df.loc[df["thal"]==3]
print(second_row6)

print(df.isnull().sum())
print(df.drop_duplicates(inplace=True))



second_row6=df.loc[:1,"thal"]
print(second_row6)


second_row7=df.loc[:3,["age","trestbps"]]
print(second_row7) 


second_row8=df.loc[:4,"age":"chol"]
print(second_row8)

second_row9=df.loc[df["age"]=="70","oldpeak":"target"]
print(second_row9)

print("# Case 2 : using .loc with index_col - starts here____")
df_index_col=pd.read_csv("heart_disease_cleveland.csv",index_col="age")
print(df_index_col)

print(df_index_col.dtypes)
print(df_index_col.info())


#Selecting a single row using .loc

# Agar aapko row number ke hisaab se row access karni hai (jaise 2nd row):
second_row = df.iloc[1]  # Python mein counting 0 se shuru hoti hai
print(second_row)

# Agar aapko columns select karne hain (jaise age se chol tak):
subset = df.loc[:, 'age':'chol']
print(subset)
print(second_row)

second_row9=df_index_col.loc[:,"exang":"target"]
print(second_row9)
print(df_index_col.columns)


sec_row = df[df["thalach"] == 147].iloc[:, :2]


print("# Case 3 : Using .iloc - starts here")

df1=df.iloc[1]
print(df1)
df2=df.iloc[1,6]
print(df2)
df3=df_index_col.iloc[1:4,2:4]
print(df3)


df4=df_index_col.iloc[[1, 3, 5]]
print(df4)


df5=df_index_col.iloc[1:5]
print(df5) 
print("ILOC SLICING")
df6=df_index_col.iloc[:,[1,4]]
print(df6)  
df7=df_index_col.iloc[:,2:4]
print(df7)


#Combined row and column selection using .iloc

row_col=df_index_col.iloc[[1,3,5],[2,4]]
print(row_col)


row_col1=df_index_col.iloc[1:3,[2,7]]
print(row_col1)

 


print(df)

df.drop(1, axis=0 , inplace=True)
# delete row with index 1
df.drop(index=2, inplace=True)
# delete rows with index 3 and 5
df.drop([3, 5], axis=0, inplace=True)
# display the modified DataFrame after deleting rows
print("Modified DataFrame - Remove Rows:")
print(df)

df.drop("age" ,axis=1, inplace=True)

# rename column one index label
df.rename(index={0: 7}, inplace=True)
# rename columns multiple index labels
df.rename(mapper={1: 10, 2: 100}, axis=0, inplace=True)
# display the DataFrame after renaming column
print("Modified DataFrame - Rename Row - 0  >>> 7 , 1 >>> 10 , 2 >>> 100  Labels:")
print(df)





print(df.columns)




# sort DataFrame by price in ascending order
sorted_df=df.sort_values(by='target')
print(sorted_df.to_string(index=False))

#Sort Pandas DataFrame by Multiple Columns

# 1. Sort DataFrame by 'Age' and then by 'Score' (Both in ascending order)
df1 = df.sort_values(by=['restecg', 'chol'])

print(" (ascending):\n")
print(df1.to_string(index=False))







grouped = df.groupby('chol')['target'].sum()

print(grouped.to_string())
print("grouped :" , len(grouped))

import numpy as np

import numpy as np

# Pandas DataFrame se target column ko NumPy array mein convert karna
target = df["target"].to_numpy()

# Ab yeh saare NumPy functions bilkul theek chalenge:
print("sum target", np.sum(target))
print("avg target", np.average(target))
print("max target", np.amax(target))
print("min target", np.amin(target))
print("std target", np.std(target))
print("median target", np.median(target))

print(np.square(target))
print(np.sqrt(target))
print("sum target",np.sum(target))
print("avg target",np.average(target))
print(np.amax(target))
print(np.amin(target))
print(np.std(target))
print(np.median(target))



print(np.square(target))
print(np.sqrt(target))






import pandas as pd
import numpy as np

df = pd.read_csv('heart_disease_cleveland.csv')


target_num = df['target'].to_numpy()


print("Average Growth Rate:", np.mean(target_num))
print("Maximum Growth Rate:", np.max(target_num))
print("Minimum Growth Rate:", np.min(target_num))


high_target =target_num[target_num > 100]
print("High Growth Startups Count:", len(target))

print(df.isnull().sum())


df_cleaned = df.dropna()



print(df.isnull().sum())

df_cleaned=df.dropna()







df.plot.scatter(x='cp', y='chol', title='Scatter Plot of cp and chol percentages');
plt.show()



print("df.corr():        " , df.corr())


print("df.describe():                    " , df.describe())


print(" df['target'] :     " , df['target'])
print("  df['chol']   :    ", df['chol']   )


y = df['sex'].values.reshape(-1, 1)
X = df['chol'].values.reshape(-1, 1)
  


print("y :  " , y)
print("X :   " , X)

#Scikit-Learn's linear regression model 

print(df['target'].values) 
print(df['target'].values.shape) 

print(X.shape) 
print(X)      

SEED = 42

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = SEED)



print(X_train) 
print(y_train) 

#Training a Linear Regression Model

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()



regressor.fit(X_train, y_train)

print(regressor.intercept_)


print(regressor.coef_)


def calc(slope, intercept, hours):
    return slope*hours+intercept

score = calc(regressor.coef_, regressor.intercept_, 9.5)
print(score) # [[94.80663482]]

score = regressor.predict([[9.5]])
print(score) # 94.80663482



y_pred = regressor.predict(X_test)

df_preds = pd.DataFrame({'Actual': y_test.squeeze(), 'Predicted': y_pred.squeeze()})
print(df_preds)



from sklearn.metrics import mean_absolute_error, mean_squared_error,r2_score

import numpy as np

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)


print(f'Mean absolute error: {mae:.2f}')
print(f'Mean squared error: {mse:.2f}')
print(f'Root mean squared error: {rmse:.2f}')
print(f'R2 Score: {r2:.2f}')









df.plot.scatter(x='thal', y='chol', title='Scatter Plot of age and chol percentages');
plt.show()



print("df.corr():        " , df.corr())


print("df.describe():                    " , df.describe())


print(" df['fbs'] :     " , df['fbs'])
print("  df['chol']   :    ", df['chol']   )



y = df['fbs'].values.reshape(-1, 1)
X = df['chol'].values.reshape(-1, 1)
  



print("y :  " , y)
print("X :   " , X)

#Scikit-Learn's linear regression model expects 

print(df['target'].values) 
print(df['target'].values.shape)


print(X.shape)
print(X)      


SEED = 23

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = SEED)



print(X_train) 
print(y_train) 


#Training a Linear Regression Model

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()



regressor.fit(X_train, y_train)


print(regressor.intercept_)



print(regressor.coef_)


def calc(slope, intercept, hours):
    return slope*hours+intercept

score = calc(regressor.coef_, regressor.intercept_, 9.5)
print(score) 

score = regressor.predict([[9.5]])
print(score) 



y_pred = regressor.predict(X_test)


df_preds = pd.DataFrame({'Actual': y_test.squeeze(), 'Predicted': y_pred.squeeze()})
print(df_preds)




from sklearn.metrics import mean_absolute_error, mean_squared_error,r2_score
import numpy as np

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)


print(f'Mean absolute error: {mae:.2f}')
print(f'Mean squared error: {mse:.2f}')
print(f'Root mean squared error: {rmse:.2f}')
print(f'R2 Score: {r2:.2f}')








print("isna",df.isna())
print(df.isnull().sum())
print(df.head())

print("df.shape:         " , df.shape)


df.plot.scatter(x='thalach', y='trestbps', title='Scatter Plot of thalach and trestbps percentages');
plt.show()



print("df.corr():        " , df.corr())


print("df.describe():                    " , df.describe())


print(" df['thalach'] :     " , df['thalach'])
print("  df['trestbps']   :    ", df['trestbps']   )


y = df['thalach'].values.reshape(-1, 1)
X = df['trestbps'].values.reshape(-1, 1)
  


print("y :  " , y)
print("X :   " , X)

#Scikit-Learn's linear regression model 

print(df['thalach'].values) 
print(df['thalach'].values.shape) 

print(X.shape) 
print(X)      

SEED = 42

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = SEED)



print(X_train) 
print(y_train) 

#Training a Linear Regression Model

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()



regressor.fit(X_train, y_train)

print(regressor.intercept_)


print(regressor.coef_)


def calc(slope, intercept, hours):
    return slope*hours+intercept

score = calc(regressor.coef_, regressor.intercept_, 9.5)
print(score) 

score = regressor.predict([[9.5]])
print(score) 

y_pred = regressor.predict(X_test)

df_preds = pd.DataFrame({'Actual': y_test.squeeze(), 'Predicted': y_pred.squeeze()})
print(df_preds)



from sklearn.metrics import mean_absolute_error, mean_squared_error,r2_score

import numpy as np

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)


print(f'Mean absolute error: {mae:.2f}')
print(f'Mean squared error: {mse:.2f}')
print(f'Root mean squared error: {rmse:.2f}')
print(f'R2 Score: {r2:.2f}')









df.plot.scatter(x='thalach', y='trestbps', title='Scatter Plot of thalach and trestbps percentages');
plt.show()



print("df.corr():        " , df.corr())


print("df.describe():                    " , df.describe())


print(" df['thalach'] :     " , df['thalach'])
print("  df['trestbps']   :    ", df['trestbps']   )



y = df['thalach'].values.reshape(-1, 1)
X = df['trestbps'].values.reshape(-1, 1)
  



print("y :  " , y)
print("X :   " , X)

#Scikit-Learn's linear regression model expects 

print(df['thalach'].values) 
print(df['thalach'].values.shape)


print(X.shape)
print(X)      


SEED = 23

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = SEED)



print(X_train) 
print(y_train) 


#Training a Linear Regression Model

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()



regressor.fit(X_train, y_train)


print(regressor.intercept_)



print(regressor.coef_)


def calc(slope, intercept, hours):
    return slope*hours+intercept

score = calc(regressor.coef_, regressor.intercept_, 9.5)
print(score) # [[94.80663482]]


score = regressor.predict([[9.5]])
print(score) 



y_pred = regressor.predict(X_test)


df_preds = pd.DataFrame({'Actual': y_test.squeeze(), 'Predicted': y_pred.squeeze()})
print(df_preds)




from sklearn.metrics import mean_absolute_error, mean_squared_error,r2_score
import numpy as np

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)


print(f'Mean absolute error: {mae:.2f}')
print(f'Mean squared error: {mse:.2f}')
print(f'Root mean squared error: {rmse:.2f}')
print(f'R2 Score: {r2:.2f}')


# I need to find a regression problem in this assignment , and I’ve found regression in all of them.