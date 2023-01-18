
import numpy as np


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


def forward_prop(x, W1):
    # Implement Forward Propagation to calculate acitvations
    a=np.dot(W1,x)
    Z1 = np.dot(W1, x)
    A1 = np.tanh(Z1)
    Z2 = np.dot(W2, A1)
    A2 = sigmoid(Z2)
      
    # here the cache is the data of previous iteration
    # This will be used for backprop
    cache = {"Z1": Z1,
             "A1": A1,
             "Z2": Z2,
             "A2": A2}
      
    return A2, cache

def compute_cost(Activation, label):
    label-

def back_propagate(W1, b1, W2, b2, cache):
   
    # Retrieve also A1 and A2 from dictionary "cache"
    A1 = cache['A1']
    A2 = cache['A2']
  
    # Backward prop: calculate dW1, db1, dW2, db2. 
    dZ2 = A2 - y
    dW2 = (1 / m) * np.dot(dZ2, A1.T)
    db2 = (1 / m) * np.sum(dZ2, axis = 1, keepdims = True)
  
    dZ1 = np.multiply(np.dot(W2.T, dZ2), 1 - np.power(A1, 2))
    dW1 = (1 / m) * np.dot(dZ1, x.T)
    db1 = (1 / m) * np.sum(dZ1, axis = 1, keepdims = True)
      
    # Updating the parameters according to algorithm
    W1 = W1 - learning_rate * dW1
    b1 = b1 - learning_rate * db1
    W2 = W2 - learning_rate * dW2
    b2 = b2 - learning_rate * db2




x=np.array([['a','b','c'],['a','b','c']]) 
#shape is 2x3  (input size, number of examples)
# each data point is a column: [a,a],[b,b],[c,c]


y=[["A","B","C"]] 
#shape is 1x3 (output size, number of examples)
# each data label is a column: [A,B,C]



W1 = np.random.randn(4, x.shape[0]) * 0.01
  
W2 = np.random.randn(y.shape[0], 4) * 0.01


for i in range(0, num_iterations):
    
        # Forward prop. Inputs: "x, parameters". return: "A2, cache".
        A2, cache = forward_prop(x, W1, W2, b1, b2)
          
        # Cost function. Inputs: "A2, y". Outputs: "cost".
        cost = compute_cost(A2, y)
   
        # Backprop. Inputs: "parameters, cache, x, y". Outputs: "grads".
        W1, W2, b1, b2 = backward_prop(W1, b1, W2, b2, cache)
          
        # Print the cost every 1000 iterations
        if print_cost and i % 1000 == 0:
            print ("Cost after iteration % i: % f" % (i, cost))