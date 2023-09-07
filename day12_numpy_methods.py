'''searching through arrays
for this we will use where method '''
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x1 = np.where(arr % 2 == 0)
x2 = np.where(arr % 2 == 1)
print(x1)
print(x2)
'''search sorting 
for this we will use where searchsorted and we will use a value or element of the array as parameter for searching the index of that element and side for searching from which side '''
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x1 = np.searchsorted(arr, 7)
x2 = np.searchsorted(arr, 7, side="right")
x3 = np.searchsorted(arr, 7, side="left")
x4 = np.searchsorted(arr, [2, 4, 6])
print(x1)
print(x2)
print(x3)
print(x4)
'''sort
for this operation we will use sort method where it will sort the given array from high value to low value '''
import numpy as np

arr = np.array([1, 3, 5, 7, 9])
x = np.sort(arr)
print(x)
'''filtering arrays
for this we can take reference with another array and get output'''
import numpy as np

arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
new_arr = arr[x]
print(new_arr)
