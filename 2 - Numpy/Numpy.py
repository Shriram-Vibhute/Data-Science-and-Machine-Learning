import numpy as np

# array creation
arr = np.array([1, 2, 3], np.int64)
print(arr[2])  # Indexing starts from 0, so the third element is at index 2

print(np.shape(arr))
print(arr.dtype)

# Array Creation methods and routines

# 1 -> Conversion from other Python structures (e.g., lists, tuples)
arr = np.array([[1,2,4], [5,6,7], [8,9,0]])
print(arr)
print(np.shape(arr))
print(arr.dtype)

arr2 = np.array({1,2,3})
print(arr2.dtype)
arr3 = np.array({"name": "Jonny"}.keys())
print(arr3.dtype)


# Intrinsic numpy array creation objects (e.g., arange, ones, zeros, etc.)
# 1 -> zeros function
arr = np.zeros((2,3)) # dtype -> float64
print(arr)

# 2 -> arange function
arr2 = np.arange(10)
print(arr2)
print(type(arr2))

arr2 = np.arange(2, 10, dtype = float)
print(arr2)

arr3 = np.arange(2, 3, 0.1)
print(arr3)

# 3 -> linespace function
arr4 = np.linspace(0, 10, 5)
print(arr4)

# Some Other functions
# empty function
arr = np.empty((3,4))
print(arr)

arr2 = np.empty_like(arr4)
print(arr2)

arr3 = np.identity((4))
print(arr3)

arr4 = arr3.reshape(8,2) # multiplication must be 16 as len(arr3) = 16
print(arr4)

arr = arr4.ravel() # Creation of 1D array from nD array
print(arr)