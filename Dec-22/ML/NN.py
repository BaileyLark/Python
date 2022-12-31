import numpy as np 

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


inputs = [1, 2, 3, 2.5] # imputs from 4 previous neuron
weights = [[0.2, 0.8, -0.5, 1], 
           [0.5, -0.91, 0.26, -0.5], 
           [-0.26, -0.27, 0.17, 0.87]]

bias = [2, 3, 0.5]
output = np.dot(weights, inputs) + bias 
# for a single nueron, the first parameter (weights) is how many indexes should be returned
print(output)




'''
layer_outputs = []
for neuron_weights, neuron_bias in zip(weights, baises):
    neuron_output = 0 
    for n_input, weight in zip(inputs, neuron_weights):
       neuron_output += n_input*weight
    neuron_output += neuron_bias
    layer_outputs.append(neuron_output)
print(layer_outputs)
'''