#NumPy for startup_growth_investment_data.csv
import numpy as np

FundingRounds , InvestmentAmount , NumberofInvestors = np.genfromtxt('startup_growth_investment_data.csv', delimiter=',' , usecols=(2,3,5) , unpack= True , dtype= None , skip_header= 1)

print(FundingRounds)
print(InvestmentAmount)
print(NumberofInvestors)

#statistics operations

print("startup_growth_investment_data.csv-mean: ", np.mean(FundingRounds))
print("startup_growth_investment_data.csv-average:", np.average(FundingRounds))
print("startup_growth_investment_data.csv-median:", np.median(FundingRounds))
print("startup_growth_investment_data.csv-min:", np.min(FundingRounds))
print("startup_growth_investment_data.csv-max:", np.max(FundingRounds))
print("startup_growth_investment_data.csv-mod:", np.mod(FundingRounds,InvestmentAmount))
print("startup_growth_investment_data.csv-percentile:", np.percentile(FundingRounds,25))

#Maths operations

print("startup_growth_investment_data.csv-square:",np.square(NumberofInvestors))
print("startup_growth_investment_data.csv-sqrt:",np.sqrt(NumberofInvestors))
print("startup_growth_investment_data.csv-abstract:",np.abs(NumberofInvestors))
print("startup_growth_investment_data.csv-power:", np.power(NumberofInvestors,NumberofInvestors))

#perform basic arithmetic 

addition = FundingRounds + InvestmentAmount
print("startup_growth_investment_data.csv-addition:",addition)
subtraction = FundingRounds - InvestmentAmount
print("startup_growth_investment_data.csv-subtraction:",subtraction)
multiplication = FundingRounds * InvestmentAmount
print("startup_growth_investment_data.csv-multiplication:",multiplication)
division = FundingRounds / InvestmentAmount
print("startup_growth_investment_data.csv-division:",division)

#perform trigonometric functions
sine_values = np.sin(FundingRounds)
print("startup_growth_investment_data.csv-sine:",sine_values)
cosine_values = np.cos(FundingRounds)
print("startup_growth_investment_data.csv-cosine:",cosine_values)
tangent_values = np.tan(FundingRounds)
print("startup_growth_investment_data.csv-tangent:",tangent_values)

# Calculate the natural logarithm and base-10 logarithm
log_array = np.log(FundingRounds)
print("startup_growth_investment_data.csv-natural logrithm value:",log_array)
log10_array = np.log10(FundingRounds)
print("startup_growth_investment_data.csv-log base10 value:",log10_array)

# Calculate the hyperbolic cosine of each element
sinh_values = np.sinh(FundingRounds)
print("startup_growth_investment_data.csv-sinh:", sinh_values)
cosh_values = np.cosh(FundingRounds)
print("startup_growth_investment_data.csv-cosh:", cosh_values)
tanh_value = np.tanh(FundingRounds)
print("startup_growth_investment_data.csv-tanh:", tanh_value)

# 2 dimentional arrary
D2array = np.array([FundingRounds,InvestmentAmount])
print("startup_growth_investment_data.csv-D2array:", D2array)

print("startup_growth_investment_data.csv-D2array - dimension" , D2array.ndim) 
# return total number of elements in array1
print("startup_growth_investment_data.csv-D2array -total number of elements:", D2array.size)
# return a tuple that gives size of array in each dimension
print("startup_growth_investment_data.csv-D2array -size of array of each dimension:", D2array.shape)
# check the data type of array1
print("startup_growth_investment_data.csv-D2array -data type:", D2array.dtype)

# Splicing array
D2array=  D2array[0:1:1 , 1:5:1]
print("startup_growth_investment_data.csv-D2array - 2 dimentional arrary - Splicing array - D2array[:1,:5] " , D2array)
D2arraySlice2=  D2array[:1, 4:15:4]
print("startup_growth_investment_data.csv-D2array - 2 dimentional arrary - Splicing array - D2array[:1, 4:15:4] " , D2arraySlice2)
# Indexing array
D2arraySliceItemOnly=  D2array[0,1]
print("startup_growth_investment_data.csv-D2array  - 2 dimentional arrary - Index array - D2array[1,5] " , D2arraySliceItemOnly)
D2arraySlice2ItemOnly=  D2array[0, 2]
print("startup_growth_investment_data.csv-D2array - 2 dimentional arrary - index array - D2array2[0, 2]", D2arraySlice2ItemOnly)

#You should use the builtin function nditer, if you don't need to have the indexes values.
for elem in np.nditer(D2array):
    print(elem)

#EDIT: If you need indexes (as a tuple for 2D table), then:
for index, elem in np.ndenumerate(D2array):
    print(index, elem)