import numpy as np 
import nnfs
from nnfs.datasets import spiral_data


nnfs.init()

# shape 
'''
l1 = [1, 5, 3, 1] # shape (4) or 1d array/vector
l2 = [[1, 3, 4, 5]
     [3, 4, 5, 1]] # shape (2, 4) or 2d Array/matrix 
l3 = [[[2, 3, 5, 4], # shape (3, 2, 4) or 3d array
     [3, 4 , 3, 3]]
     [[2, 3, 4, 5],
     [2, 4, 5, 6]],
     [[2, 3, 5, 6],
     [8, 5, 5, 4]]]
'''
# CALCULATIONS
# (1 * 0.2) + (2 * 0.8) + (3 * -0.5) (1 * 1) + 2  is equal to neuron output 1
# the dot product adds two array together dot_product = ([0] * [0]) + ([1] * [1])

''' SINGLE NEURON 
inputs = [1, 2, 3, 2.5] # imputs from 4 previous neuron
weights = [[0.2, 0.8, -0.5, 1], 
           [0.5, -0.91, 0.26, -0.5], 
           [-0.26, -0.27, 0.17, 0.87]]

bias = [2, 3, 0.5]
output = np.dot(weights, inputs) + bias 
# for a single nueron, the first parameter (weights) is how many indexes should be returned
print(output)
'''
# ADDING MATRICES (times two values together, then add them) 
# first row + first column    X 0 0 0 

# first row + second column   0 X 0 0

# second row + first column   O O O O 
#                             X 0 0 0
# After, add the bais to the output for each line

# TRANSPOSING, switch the rows and columns of two matrices 

# ACTIVATION FUNCTION
# after the calculation with the bais.
# Step Function, if the input is <= 0 then it's 0, if > 0 then it's 1
# Sigmoid Functiom, 0 to 1, x0y0 is 0.5
# Rectified Linear function, only if x > 0 will it output x

# inputs = x 
X = [[1, 2, 3, 2.5],
     [2.0, 5.0, -1.0, 2.0],
     [-1.5, 2.7, 3.3, -0.8]] # iNputs from 4 previous neuron

X, y = spiral_data(100, 3)

class Layer_Dense:
     def __init__(self, n_inputs , n_neurons): # the shape of the matrix 
          self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
          self.biases = np.zeros((1, n_neurons))
     def forward(self, inputs):
          self.output = np.dot(inputs, self.weights) + self.biases

class Activation_ReLU: # if the input is negative, set it to 0. 
     def forward(self, inputs):
          self.output = np.maximum(0, input)


#each layer is a neuron
layer1 = Layer_Dense(2, 5) # second param must be the size of th efirst
activation1 = Activation_ReLU()
layer1.forward(X) # first neuron takes the input
activation1.forward(layer1.output)

print(activation1.output)
