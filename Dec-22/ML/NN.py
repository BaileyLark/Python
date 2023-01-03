import numpy as np 
import nnfs
from nnfs.datasets import spiral_data
import math

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

# EXPONENTIAL FUNCTION (y = e^x) 
# on a graph, when X < 0, Y cannot be 0. Simply prevents negative numbers
# e = 2.71828182...
# output(y) = (e)euluers number ^ (x)input

# NORMALIZE 
# Gives probabilty distribution

# ACTIVATION FUNCTION
# after the calculation with the bais.
# Step Function, if the input is <= 0 then it's 0, if > 0 then it's 1
# Sigmoid Functiom, 0 to 1, x0y0 is 0.5
# Rectified Linear function, only if x > 0 will it output x
# Soft Max Activation function is Exponential + Normalization

# inputs = x 

# MULTIPLE LAYERS OF NEURONS + RLF ACTIVATION FUNCTION 


class Layer_Dense:
     def __init__(self, n_inputs , n_neurons): # the shape of the matrix 
          self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
          self.biases = np.zeros((1, n_neurons))
     def forward(self, inputs):
          self.output = np.dot(inputs, self.weights) + self.biases

class Activation_ReLU: # if the input is negative, set it to 0. 
     def forward(self, inputs):
          self.output = np.maximum(0, input)

class Activation_Softmax:
     def forward(self, inputs):
          exp_values = np.exp(inputs, - np.max(inputs, axis=1, keepdims=True))
          probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
          self.output = probabilities

X,y = spiral_data(samples=100, classes=3)

dense1 = Layer_Dense(2, 3)
activation1 = Activation_ReLU()

dense2 = Layer_Dense(3, 3)
activation2 = Activation_Softmax()

dense1.forward(X)
activation1.forward(dense1.output)

dense2.forward(activation1.output)
activation2.forward(dense2.output)

print(activation2.output[:5])


'''#each layer is a neuron
layer1 = Layer_Dense(2, 5) # second param must be the size of th efirst
activation1 = Activation_ReLU()
layer1.forward(X) # first neuron takes the input
activation1.forward(layer1.output)

print(activation1.output)


# SOFTMAX ACTIVATION
layer_outputs = [[4.8, 1.21, 2.385], 
                 [8.9, -1.81, 0.2],
                 [1.41, 1.051, 0.026]]

exp_values = np.exp(layer_outputs) # (E ^ each value), axis=1 add each rows, keep dims converts the shape from (3, 1) to (1 , 3)
norm_values = exp_values / np.sum(exp_values, axis=1, keepdims=True) # takes each expontential value and divides it by total 

print(norm_values)'''
