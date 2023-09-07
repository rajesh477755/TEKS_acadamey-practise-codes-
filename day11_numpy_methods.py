'''1) Iterating array with different data types 
We can change datatype of the element in array using flag,op_datatype as parameter in nditer function
'''
import numpy as np

arr = np.array([1, 2, 3])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)
'''2) Iterating with different step sizes '''
import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::2]):
  print(x)
'''3)Enumerator iteration using ndenumerate'''
import numpy as np

arr = np.array([1, 2, 3])
for idx, x, in np.ndenumerate(arr):
  print(idx, x)
'''4) Joining Arrays
For this operation we will use concatenate method where in which we can give axis as a parameter which will add'''
import numpy as np

arr1 = np.array([[1, 2, 3], [7, 8, 9]])
arr2 = np.array([[4, 5, 6], [10, 11, 12]])
arr3 = np.concatenate((arr1, arr2))
arr4 = np.concatenate((arr1, arr2), axis=1)
print(arr4)
print(arr3)
'''stacking 
this aslo a way of adding up the arrays
there are 3 ways to do this '''
#1) Staking along the rows
# for this method we will use hstack() function
import numpy as np

arr = np.hstack((arr1, arr2))
print(arr)
#2) Stacking along the column
#for this method we will use ustack() function
import numpy as np

arr = np.vstack((arr1, arr2))
print(arr)
#3) Stacking along the height
# In this method we will use dstack() function
import numpy as np

arr = np.dstack((arr1, arr2))
print(arr)
'''Spliting arrays 
This is reverse process of joining the arrays 
in this method we will use array_spliter() function and a number for no of arrays we want to get from the input array and axis for how to slpit array'''
import numpy as np

arr1 = ([1, 2, 3, 4, 5])
arr2 = ([[1, 2], [3, 4], [5, 6], [7, 8]])
new_arr1 = np.array_split(arr1, 3)
new_arr2 = np.array_split(arr2, 3)
new_arr3 = np.array_split(arr2, 3, axis=1)
print(new_arr1)
print(new_arr2)
print(new_arr3)
