# Numpy:
# Numpy (Numerical python) is a python library used for scitific and mathematical computing :
# it provide:
# -> powerfull array objects(more effective than python lists)
# -> vectorized operation (fast elemnt wise calculation ).
# ->Support for linear algebra ,  statistics, random numbers operation etc .

#importing the numpy library.
# import numpy as np 

#creating an array with numpy :
# 1D Array :
# A1D = np.array([1,2,3,4,5])
# print(AID)
# #2D Array:
# A2D = np.array([[1,2,3],[4,5,6],[7,8,9]])

#[
#     1  2  3
#     4  5  6
#     7  8  9
# ]
# print(A2D)

# methods and operators in numpy arrays:
#  basic array information methods:
# A = numpy.array([1,2,3,4,5])
#ndim():Returns the no of dimensions of the array
# print(A.ndim)
# print (A2d.ndim)
# # shape: returns a tuple showing the size of the array in each dimension (rowes,columns,etc)
#  print(A2D).shape)
# # size: Returns the total number of elements in the array.
# print(A2D.size)
# datatype:returns the data of the elemnts in the array .
# print(A2D.dtypes)# = type

#2. creating an array with numpy:
import numpy as np

# # zeroes :creates an array of 6 zeroes.
# print(np.zeros(6))

# # one: creates an array of 6 ones 
# print(np.ones(5))

# # arrange:creates and array from 1 - 10 based on the ranges.
# print(np.arange(1,11,1))

# # linspace: crteates an 3 numbers enevnly spaceed b/w 0 &1
# print(np.linspace(0,1,3))


#mathematical operation:

# A = np.array([1,2,3,4,5])
# L = [1,3,5,7,9]
# print(A+6)
# print(A-6)
# print(A*6)
# print(A/6)
# print(A**6)
# print(A//6)

#Aggregate Functions:
# A = np.array([1,2,3,4,5])
# sum():
# print(np.sum(A))
#mean():
# print(np.mean(A))

#Max():
# print(np.max(A))
#  #min():
# print(np.min(A))

# # median:
# print(np.mediam (A))
#  #  std:
# print(np.std(A))

# cumpod:
# print(np.cumpod(A))


# # matrix operstion :
# mat1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# mat2 = np.array,([[7,8,9],[4,5,6],[1,2,3]])
# print(mat1 + mat2)
# print(mat1 * mat2)
# print(mat1 ** mat2)

# #dot():
# print(np.dot(mat1,mat2))

# #transpowse:
# print(np.transpose(mat1))

