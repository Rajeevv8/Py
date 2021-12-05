#Numpy intro
import numpy as np
#Values in lists are stored non contiguously
#Values in np arrays are stored contiguously
#1D array
a=np.array([1,2,3])
print(a)
#2D array
b=np.array([[1,2,3],[4,5,6]])
print(b)
#Array dimension
print(b.ndim)