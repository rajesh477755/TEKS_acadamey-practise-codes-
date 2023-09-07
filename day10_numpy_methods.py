'''menthods in numpy'''
#1 finding dimesions of array
import numpy as np

a = np.array([1, 2, 3, 4])
print(a.ndim)
'''this method is used to find the dimension of given array'''
#2 creating a array a particular dimensions
import numpy as np

a = np.array([1, 2, 3, 4], ndmin=5)
print(a)
'''this method will print a array with number of dimensions that we give as input '''
'''operations on arrays using numpy library'''
#3 finding shape of an array
import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)
#4 reshaping the array
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
new = arr.reshape(4, 3)
print(new)
#5 efficent looping
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
for x in np.nditer(arr):
  print(x)
#6 copying one array to another
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)
#7 viewing one array
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 47
print(arr)
print(x)
