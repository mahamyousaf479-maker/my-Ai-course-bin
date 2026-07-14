#pandas for FastFoodRestaurants
import pandas as pd

df =pd.read_csv('FastFoodRestaurants.csv', delimiter=(','))
print(df)

#data type
print('df data type',df.dtypes)
#info
print('df info',df.info)
#print last rows 
print('df last three rows',df.tail(3))
#print first three rows
print('df first three rows',df.head(3))
#Summary of Statistics of DataFrame using describe() method.
print('Summary of Statistics of DataFrame using describe() method',df.describe())
#Counting the rows and columns in DataFrame using shape(). It returns the no. of rows and columns enclosed in a tuple.
print('Counting the rows and columns in DataFrame using shape',df.shape)
#remove duplicates rows
print('remove duplicates rows',df.drop_duplicates)
#acess the colomn name 
latitude = df['latitude']
print('acess the column name: df :')
print(latitude)

#acess multiple columns
country_key = df[['country','keys']]
print('acess the multiple colums:df:')
print(country_key)

#Case1 using .loc
#selecting  a single row using .loc
second_row = df.loc[1]
print(second_row)
#Selecting multiple rows using .loc
second_row2 = df.loc[[1,3]]
print(second_row2)
#Selecting a slice of rows using .loc
second_row3 = df.loc[2:3]
print(second_row3)
#Conditional selection of rows using .loc
second_row4 = df.loc[df['city'] == 'Massena']
print(second_row4)
#Selecting a single column using .loc
second_row5 = df.loc[2:3,'city']
print(second_row5)
#Selecting multiple columns using .loc
second_row6 = df.loc[3:4,['longitude','name']]
print(second_row6)
#Selecting a slice of columns using .loc
second_row7 = df.loc[2:5,'longitude':'name']
print(second_row7)
#Combined row and column selection using .loc
second_row8 = df.loc[df['city'] == 'Lexington', 'province']
print(second_row8)
#case 2: using .loc with index_col  -  ends here

#Case 3 starts here using .iloc 

#Selecting a single row using .iloc
second_row = df.iloc[0]
print("#Selecting a single row using .iloc")
print(second_row)

#Selecting multiple rows using .iloc
second_row2 = df.iloc[[1, 3,5]]
print("#Selecting multiple rows using .iloc")
print(second_row2)
print()

#Selecting a slice of rows using .iloc
second_row3 = df.iloc[2:5]
print("#Selecting a slice of rows using .iloc")
print(second_row3)
print()

#Selecting a single column using .iloc
second_row5 = df.iloc[:,2]
print("#Selecting a single column using .iloc")
print(second_row5)
print()

#Selecting multiple columns using .iloc
second_row6 = df.iloc[:,[2,4]]
print("#Selecting multiple columns using .iloc")
print(second_row6)
print()

#Selecting a slice of columns using .iloc
second_row7 = df.iloc[:,2:4]
print("#Selecting a slice of columns using .iloc")
print(second_row7)
print()

#Combined row and column selection using .iloc
second_row8 = df.iloc[[1, 3,5],2:4]
print("#Combined row and column selection using .iloc")
print(second_row8)
print()

# Case 3 : Using .iloc - ends here
