import numpy as np
arr = np.array([[1,2,3], [4,5,6], [7,1,0]], np.int64)

# Axis wise sum
print(arr.sum(axis=0))
print(arr.sum(axis=1))

# Transpose of matrix
arr_t = arr.transpose() # Only transpost attribute returns an iterator
print(arr_t)

arr_flat = arr.flat # Property
for i in arr_flat:
    print(i)

print("Dimention: ", arr.ndim)

print("size : ", arr.size)

print("bytes : ", arr.nbytes)
# in 32 bytes -> size(int) = 4 bytes
# in 64 bytes -> size(int) = 8 bytes

# 2D Array -> methods
print(arr.argmax(axis=1))
print(arr.argmin(axis=0))

# These methods convert the nD matrix to 1D and then returns the index number where max/min element is present
print(arr.argmin())
print(arr.argmax())



# print(arr.argsort())
print("Array sort default :\n", arr.argsort(), '\n')

# arr_sort_default = arr.argsort()
# arr_sort_default = arr_sort_default.ravel()
# for i in arr_sort_default:
#     print(arr[i])

print("Array sort Horizontally :\n",arr.argsort(axis=1), '\n')
print("Array sort Vertically :\n",arr.argsort(axis=0), '\n')


# 1D Array -> methods
ar = np.array([45, 12, -67, 0, 54, 54], np.int32)

print(ar.argmax()) # Returns the index of element which is max (if more than one present the n 1st occurance)

print(ar.argmin())

print(ar.argsort()) # reurns the index of elements in sorted order - The sorting is based on the elements


# Matrix Operations
arr1 = np.array([[1,2,3], [4,5,6], [7,8,9]])
arr2 = np.array([[7,8,9], [4,5,6], [1,2,3]])

print(arr1 + arr2)
print(arr2 * arr1)

print(np.sqrt(arr2))

print(arr.min())
print(arr.max())

print(arr.sum())

# where method
print(np.where(arr1 > 3)) # Elements which greater than 3

# nonzero and count_non_zero methods
print(np.nonzero(arr1)) # Tuple of indices where they are loated
print(np.count_nonzero(arr1)) # Total elements which are non zero