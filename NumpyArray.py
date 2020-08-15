# create a list
lst = [1, 2, 3]

# import numpy library
import numpy as np

# create an array from a list
arr = np.array(lst)

# create a 3x3 matrix
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
np.array(mat)

# create an array using arange
# arange(start,top,step)
np.arange(0, 11, 2)

# generate an array with all zeros
np.zeros(3)

# using tuple as an argument to make a size of a array
np.zeros((3, 4))

# we can create an array with ones also
np.ones((3, 4))

# linspace(start, stop, num)
# work same with arange but the third argument is how many point
np.linspace(0, 5, 10)  # from 0 to 5 make it 10 evenly space

# create a identity matrix
np.eye(4)

# create a random number of array (range above zero)
np.random.rand(5) # 1-D
np.random.rand(5,5) # 5x5 random matrix

# create a random number of array (range around zero)
np.random.randn(2)
np.random.randn(4,4)

# get a random integer
# randint(low, high, size)
np.random.randint(1, 100)
np.random.randint(1, 100, 10) #create an array with 10 random integer

#reshape an array
#make sure row * column equal the size of the array
arr1 = np.arange(0,25)
arr1.reshape(5,5)

#max() and min()
arr.max() #get the largest element
arr.min() #get the smallest element

#argmax() and argmin()
arr1.argmax() #get the index of the largest element
arr1.argmin() #get the index of the smallest element

#get the shape of the vector
arr1.shape

#get the datatype of an array
arr.dtype



