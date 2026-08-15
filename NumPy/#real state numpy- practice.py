#real Estate numpy practice 
import numpy as np

price , city , zipcode = np.genfromtxt('RealEstate-USA.csv', delimiter=',' , usecols=(2,8,10) , unpack= True , dtype= None , skip_header= 1)

print(price)
print(city)
print(zipcode)

#statistics operations

print("RealEstate-USA.csv-mean: ", np.mean(price))
print("RealEstate-USA.csv-average:", np.average(price))
print("RealEstate-USA.csv-median:", np.median(price))
print("RealEstate-USA.csv-min:", np.min(price))
print("RealEstate-USA.csv-max:", np.max(price))
print("RealEstate-USA.csv-mod:", np.mod(price,zipcode))
print("RealEstate-USA.csv-percentile:", np.percentile(price,25))

#Maths operations

print("RealEstate-USA.csv-square:",np.square(price))
print("RealEstate-USA.csv-sqrt:",np.sqrt(price))
print("RealEstate-USA.csv-abstract:",np.abs(price))
print("RealEstate-USA.csv-power:", np.power(price, price))

#perform basic arithmetic 

addition = price + zipcode
print("RealEstate-USA.csv-addition:",addition)
subtraction = price - zipcode
print("RealEstate-USA.csv-subtraction:",subtraction)
multiplication = price * zipcode
print("RealEstate-USA.csv-multiplication:",multiplication)
division = price / zipcode
print("RealEstate-USA.csv-division:",division)

#perform trigonometric functions
sine_values = np.sin(price)
print("RealEstate-USA.csv-sine:",sine_values)
cosine_values = np.cos(price)
print("RealEstate-USA.csv-cosine:",cosine_values)
tangent_values = np.tan(price)
print("RealEstate-USA.csv-tangent:",tangent_values)

# Calculate the natural logarithm and base-10 logarithm
log_array = np.log(price)
print("RealEstate-USA.csv-natural logrithm value:",log_array)
log10_array = np.log10(price)
print("RealEstate-USA.csv-log base10 value:",log10_array)

# Calculate the hyperbolic cosine of each element
sinh_values = np.sinh(price)
print("RealEstate-USA.csv-sinh:", sinh_values)
cosh_values = np.cosh(price)
print("RealEstate-USA.csv-cosh:", cosh_values)
tanh_value = np.tanh(price)
print("RealEstate-USA.csv-tanh:", tanh_value)

# 2 dimentional arrary
D2array = np.array([price,zipcode])
print("RealEstate-USA.csv-D2array:", D2array)

print("RealEstate-USA.csv-D2array - dimension" , D2array.ndim) 
# return total number of elements in array1
print("RealEstate-USA.csv-D2array -total number of elements:", D2array.size)
# return a tuple that gives size of array in each dimension
print("RealEstate-USA.csv-D2array -size of array of each dimension:", D2array.shape)
# check the data type of array1
print("RealEstate-USA.csv-D2array -data type:", D2array.dtype)

# Splicing array
D2array=  D2array[0:1:1 , 1:5:1]
print("RealEstate-USA.csv-D2array - 2 dimentional arrary - Splicing array - D2array[:1,:5] " , D2array)
D2arraySlice2=  D2array[:1, 4:15:4]
print("RealEstate-USA.csv-D2array - 2 dimentional arrary - Splicing array - D2array[:1, 4:15:4] " , D2arraySlice2)
# Indexing array
D2arraySliceItemOnly=  D2array[0,1]
print("RealEstate-USA.csv-D2array  - 2 dimentional arrary - Index array - D2array[1,5] " , D2arraySliceItemOnly)
D2arraySlice2ItemOnly=  D2array[0, 2]
print("RealEstate-USA.csv-D2array - 2 dimentional arrary - index array - D2array2[0, 2]", D2arraySlice2ItemOnly)

#You should use the builtin function nditer, if you don't need to have the indexes values.
for elem in np.nditer(D2array):
    print(elem)

#EDIT: If you need indexes (as a tuple for 2D table), then:
for index, elem in np.ndenumerate(D2array):
    print(index, elem)

"""# for loop
rows = np.shape(D2LongLat[0])[0]
cols = np.shape(D2LongLat[1])[0]
for i in range(0, (rows + 1)):
    for j in range(0, (cols + 1)):
        print (D2LongLat[i,j])
"""

