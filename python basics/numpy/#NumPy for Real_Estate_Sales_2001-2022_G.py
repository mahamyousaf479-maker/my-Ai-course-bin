#NumPy for Real_Estate_Sales_2001-2022_GL-Short.csv
import numpy as np

AssessedValue , SaleAmount , SalesRatio = np.genfromtxt('Real_Estate_Sales_2001-2022_GL-Short.csv', delimiter=',' , usecols=(0,1,2) , unpack= True , dtype= None , skip_header= 1)

print(AssessedValue)
print(SaleAmount)
print(SalesRatio)

#statistics operations

print("Real_Estate_Sales_2001-2022_GL-Short.csv-mean: ", np.mean(AssessedValue))
print("Real_Estate_Sales_2001-2022_GL-Short.csv-average:", np.average(AssessedValue))
print("Real_Estate_Sales_2001-2022_GL-Short.csv-median:", np.median(AssessedValue))
print("Real_Estate_Sales_2001-2022_GL-Short.csv-min:", np.min(AssessedValue))
print("Real_Estate_Sales_2001-2022_GL-Short.csv-max:", np.max(AssessedValue))
print("Real_Estate_Sales_2001-2022_GL-Short.csv-mod:", np.mod(AssessedValue,SaleAmount))
print("Real_Estate_Sales_2001-2022_GL-Short.csv-percentile:", np.percentile(AssessedValue,25))

#Maths operations

print("Real_Estate_Sales_2001-2022_GL-Short.csv-square:",np.square(AssessedValue))
print("Real_Estate_Sales_2001-2022_GL-Short.csv-sqrt:",np.sqrt(AssessedValue))
print("Real_Estate_Sales_2001-2022_GL-Short.csv-abstract:",np.abs(AssessedValue))
print("Real_Estate_Sales_2001-2022_GL-Short.csv-power:", np.power(AssessedValue, AssessedValue))

#perform basic arithmetic 

addition = AssessedValue + SaleAmount
print("Real_Estate_Sales_2001-2022_GL-Short.csv-addition:",addition)
subtraction = AssessedValue - AssessedValue
print("Real_Estate_Sales_2001-2022_GL-Short.csv-subtraction:",subtraction)
multiplication = AssessedValue * SaleAmount
print("Real_Estate_Sales_2001-2022_GL-Short.csv-multiplication:",multiplication)
division = AssessedValue / SaleAmount
print("Real_Estate_Sales_2001-2022_GL-Short.csv-division:",division)

#perform trigonometric functions
sine_values = np.sin(SaleAmount)
print("Real_Estate_Sales_2001-2022_GL-Short.csv-sine:",sine_values)
cosine_values = np.cos(SaleAmount)
print("Real_Estate_Sales_2001-2022_GL-Short.csv-cosine:",cosine_values)
tangent_values = np.tan(SaleAmount)
print("Real_Estate_Sales_2001-2022_GL-Short.csv-tangent:",tangent_values)

# Calculate the natural logarithm and base-10 logarithm
log_array = np.log(AssessedValue)
print("Real_Estate_Sales_2001-2022_GL-Short.csv-natural logrithm value:",log_array)
log10_array = np.log10(AssessedValue)
print("Real_Estate_Sales_2001-2022_GL-Short.csv-log base10 value:",log10_array)

# Calculate the hyperbolic cosine of each element
sinh_values = np.sinh(AssessedValue)
print("Real_Estate_Sales_2001-2022_GL-Short.csv-sinh:", sinh_values)
cosh_values = np.cosh(AssessedValue)
print("Real_Estate_Sales_2001-2022_GL-Short.csv-cosh:", cosh_values)
tanh_value = np.tanh(AssessedValue)
print("Real_Estate_Sales_2001-2022_GL-Short.csv-tanh:", tanh_value)

# 2 dimentional arrary
D2array = np.array([AssessedValue,SaleAmount])
print("Real_Estate_Sales_2001-2022_GL-Short.csv-D2array:", D2array)

print("Real_Estate_Sales_2001-2022_GL-Short.csv-D2array - dimension" , D2array.ndim) 
# return total number of elements in array1
print("Real_Estate_Sales_2001-2022_GL-Short.csv-D2array -total number of elements:", D2array.size)
# return a tuple that gives size of array in each dimension
print("Real_Estate_Sales_2001-2022_GL-Short.csv-D2array -size of array of each dimension:", D2array.shape)
# check the data type of array1
print("Real_Estate_Sales_2001-2022_GL-Short.csv-D2array -data type:", D2array.dtype)

# Splicing array
D2array=  D2array[0:1:1 , 1:5:1]
print("Real_Estate_Sales_2001-2022_GL-Short.csv-D2array - 2 dimentional arrary - Splicing array - D2array[:1,:5] " , D2array)
D2arraySlice2=  D2array[:1, 4:15:4]
print("Real_Estate_Sales_2001-2022_GL-Short.csv-D2array - 2 dimentional arrary - Splicing array - D2array[:1, 4:15:4] " , D2arraySlice2)
# Indexing array
D2arraySliceItemOnly=  D2array[0,1]
print("Real_Estate_Sales_2001-2022_GL-Short.csv-D2array  - 2 dimentional arrary - Index array - D2array[1,5] " , D2arraySliceItemOnly)
D2arraySlice2ItemOnly=  D2array[0, 2]
print("Real_Estate_Sales_2001-2022_GL-Short.csv-D2array - 2 dimentional arrary - index array - D2array2[0, 2]", D2arraySlice2ItemOnly)

#You should use the builtin function nditer, if you don't need to have the indexes values.
for elem in np.nditer(D2array):
    print(elem)

#EDIT: If you need indexes (as a tuple for 2D table), then:
for index, elem in np.ndenumerate(D2array):
    print(index, elem)