'''Random numbers : Picking up a number randomly from the given range of numbers is random number'''
'''this is a python library which is used for propablity which is inside numpy '''
import numpy as np
from numpy import random
'''for getting a random float value we use rand() function where values vary from 0 to 1'''
x = random.rand()
#for getting a random integer value we use randint() function
y = random.randint(100)
'''we can aslo choose a random interger from given range by giving number in randint() function as parameter'''
'''we can aslo get a list of float values by giving number in rand() function as parameter which will give a '''
a = random.rand(6)
'''Choosing a  random number from the given list of numbers 
for this we will use choice() function where we can pass list of numbers as parameter or a variable which holds the list of nummbers '''
b = random.choice([1, 2, 3, 4, 5])
arr = np.array([1, 2, 3, 4, 5])
c = random.choice(arr)
''' we can aslo make a matrix with random values by using size as a parameter for choice(),randint() functions '''
d = random.choice(arr, size=(3, 3))
e = random.randint(100, size=(3, 3))
'''shuffing arrays'''
''' we can shuffel arrays using shuffel() function and pass array which we cant shuffel as a parameter '''
f = random.shuffle([1, 2, 3, 4, 5])
print(x)
print(y)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
