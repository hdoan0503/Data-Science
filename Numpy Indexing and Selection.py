import numpy as np

arr = np.arange(0, 11)

# get the value at index in array
arr[8]
arr[1:5]  # from 1 to 4
arr[0:5]  # from 0 to 4
arr[0:6]  # from 0 to 5
arr[5:]  # everything beyond 5 and including 5

# copy the array
arr_copy = arr.copy()
arr_copy[1] = 100  # will not affect the original array

# create a 2d array
arr_2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])

# grab 5 out of 2d array
arr_2d[0][0]
# grab 25 out of 2d array
arr_2d[1][1]
# grab 40 out of 2d array
arr_2d[2][1]
# or
arr_2d[2, 1]

# grab first and second row
# also second and third column
arr_2d[:2, 1:]

# new array
arr1 = np.arange(1, 11)

# comparision will return a array of boolean
bool_arr = arr1 > 5
# conditional collection
arr1[bool_arr]  # return any "true" element

# shorthand
arr1[arr1 > 5]

# make a 2d array with arange and reshape
arr_2dd = np.arange(50).reshape(5, 10)

# sum all column in a matrix
# axis:
# 0: indicate column
# 1: indicate index
arr1.sum(axis=0)
