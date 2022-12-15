from tkinter import N
import numpy as np 

# numpy array 

np.zeros(5) # an array of 5 float, 0's. ([0,0,0,0,0])
np.ones(5) # an array of 5 floats, 1's ([1,1,1,1,1])
np.array(3) # an empty array 
np.linspace(2, 10, 5) # an of 5 floats between 2 and 5 ([2, 4, 6, 8, 10])
np.array([2,35,6,7,2,3]) # a specified array

np.array([[[92,23,23,2], [12,3,112,21]]]) # two dimentional array
arr = np.random.randint(10, size=6) # a random float array between 0-10, of size 6
arr[0] # first index
arr[-1] # last index 


