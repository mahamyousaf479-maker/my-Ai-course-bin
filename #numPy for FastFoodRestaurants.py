#numPy for FastFoodRestaurants.csv
import numpy as np

latitude , longitude , postalCode = np.genfromtxt('FastFoodRestaurants.csv', delimiter=',' , usecols=(1,2,3) , unpack= True , dtype= None , skip_header= 1)

print(latitude)
print(longitude)
print(postalCode)

#statistics operations

print("FastFoodRestaurants.csv-mean: ", np.mean(postalCode))
print("FastFoodRestaurants.csv-average:", np.average(postalCode))
print("FastFoodRestaurants.csv-median:", np.median(postalCode))
print("FastFoodRestaurants.csv-min:", np.min(postalCode))
print("FastFoodRestaurants.csv-max:", np.max(postalCode))
print("FastFoodRestaurants.csv-mod:", np.mod(postalCode,latitude))
print("FastFoodRestaurants.csv-percentile:", np.percentile(postalCode,25))

#Maths operations

print("FastFoodRestaurants.csv-square:",np.square(postalCode))
print("FastFoodRestaurants.csv-sqrt:",np.sqrt(postalCode))
print("FastFoodRestaurants.csv-abstract:",np.abs(postalCode))
print("FastFoodRestaurants.csv-power:", np.power(postalCode, postalCode))

#perform basic arithmetic 

addition = postalCode + postalCode
print("FastFoodRestaurants.csv-addition:",addition)
subtraction = postalCode - postalCode
print("FastFoodRestaurants.csv-subtraction:",subtraction)
multiplication = postalCode * postalCode
print("FastFoodRestaurants.csv-multiplication:",multiplication)
division = postalCode / postalCode
print("FastFoodRestaurants.csv-division:",division)

#perform trigonometric functions
sine_values = np.sin(postalCode)
print("FastFoodRestaurants.csv-sine:",sine_values)
cosine_values = np.cos(postalCode)
print("FastFoodRestaurants.csv-cosine:",cosine_values)
tangent_values = np.tan(postalCode)
print("FastFoodRestaurants.csv-tangent:",tangent_values)

# Calculate the natural logarithm and base-10 logarithm
log_array = np.log(postalCode)
print("FastFoodRestaurants.csv-natural logrithm value:",log_array)
log10_array = np.log10(postalCode)
print("FastFoodRestaurants.csv-log base10 value:",log10_array)

# Calculate the hyperbolic cosine of each element
sinh_values = np.sinh(postalCode)
print("FastFoodRestaurants.csv-sinh:", sinh_values)
cosh_values = np.cosh(postalCode)
print("FastFoodRestaurants.csv-cosh:", cosh_values)
tanh_value = np.tanh(postalCode)
print("FastFoodRestaurants.csv-tanh:", tanh_value)

# 2 dimentional arrary
D2array = np.array([postalCode,latitude])
print("FastFoodRestaurants.csv-D2array:", D2array)

print("FastFoodRestaurants.csv-D2array - dimension" , D2array.ndim) 
# return total number of elements in array1
print("FastFoodRestaurants.csv-D2array -total number of elements:", D2array.size)
# return a tuple that gives size of array in each dimension
print("FastFoodRestaurants.csv-D2array -size of array of each dimension:", D2array.shape)
# check the data type of array1
print("FastFoodRestaurants.csv-D2array -data type:", D2array.dtype)

# Splicing array
D2array=  D2array[0:1:1 , 1:5:1]
print("FastFoodRestaurants.csv-D2array - 2 dimentional arrary - Splicing array - D2array[:1,:5] " , D2array)
D2arraySlice2=  D2array[:1, 4:15:4]
print("FastFoodRestaurants.csv-D2array - 2 dimentional arrary - Splicing array - D2array[:1, 4:15:4] " , D2arraySlice2)
# Indexing array
D2arraySliceItemOnly=  D2array[0,1]
print("FastFoodRestaurants.csv-D2array  - 2 dimentional arrary - Index array - D2array[1,5] " , D2arraySliceItemOnly)
D2arraySlice2ItemOnly=  D2array[0, 2]
print("FastFoodRestaurants.csv-D2array - 2 dimentional arrary - index array - D2array2[0, 2]", D2arraySlice2ItemOnly)

#You should use the builtin function nditer, if you don't need to have the indexes values.
for elem in np.nditer(D2array):
    print(elem)

#EDIT: If you need indexes (as a tuple for 2D table), then:
for index, elem in np.ndenumerate(D2array):
    print(index, elem)

