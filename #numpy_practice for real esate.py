#numpy_practice for real esate 
import numpy as np
price , acre_lot = np.genfromtxt('week4 RealEstate-USA.csv',delimiter=',' , usecols=(2,4),unpack=True , dtype=none ,skip_header=1)
print(price)
print(acre_lot)
