
import numpy as np
import matplotlib.pylab as plt
import data
import math
import time
import sys
import pandas as pd

import warnings
warnings.filterwarnings("error")

class ANN:
    def __init__(self, layers_size):
        self.layers_size = layers_size
        self.parameters = {} #The self.parameters will be a dictonary object where we keep all the W and b. 
        self.L = len(self.layers_size)-1
        self.n = 0
        self.costs = []
	
    def sigmoid(self, Z):
        return 1 / (1 + np.exp(-Z))
    
    def sigmoid_derivative(self, Z):
        s = 1 / (1 + np.exp(-Z))
        return s * (1 - s)

    def initialize_parameters(self):
    
        for l in range(1, len(self.layers_size)):

            self.parameters["W" + str(l)] = np.random.rand(self.layers_size[l], self.layers_size[l - 1])
            self.parameters["b" + str(l)] = np.zeros((self.layers_size[l], 1))

    def fit(self, X, Y, learning_rate):
    #The fit() function will first call initialize_parameters() to create all the necessary W and b for each layer.

        for loop in range(500):
            A, store = self.forward(X)
            #A=np.array([ if x > for x in A])
            for i in range (len(A[0])):
                #print("#"*10,A[i])
                if A[0][i]==0:
                    A[0][i]=0.000001
                elif A[0][i]==1:
                    A[0][i]=0.999999
            try:
                cost = np.squeeze(-(Y.dot(np.log(A.T)) + (1 - Y).dot(np.log(1 - A.T))) / self.n)
            except:
                print("Error")
                print(A.T.shape)
                #print(-(Y.dot(np.log(A.T))))
                print(Y)
                print(A)
                #print((1 - Y).dot(np.log(1 - A.T)))
                print(self.n)
                exit()
            derivatives = self.backward(X, Y, store)
    
            for l in range(1, self.L + 1):
                self.parameters["W" + str(l)] = self.parameters["W" + str(l)] - learning_rate * derivatives[
                    "dW" + str(l)]
                self.parameters["b" + str(l)] = self.parameters["b" + str(l)] - learning_rate * derivatives[
                    "db" + str(l)]

            if loop % 150 == 0 or loop<6:
                print("Epoch ", loop, ": cost: ", cost)
                #print("cost", cost)
                ann.predict(X,Y,5)
            self.costs.append(cost)


    def forward(self, X):
        store = {}
 
        A = X.T
        for l in range(self.L - 1):
            Z = self.parameters["W" + str(l + 1)].dot(A) + self.parameters["b" + str(l + 1)]
            A = self.sigmoid(Z)
            store["A" + str(l + 1)] = A
            store["W" + str(l + 1)] = self.parameters["W" + str(l + 1)]
            store["Z" + str(l + 1)] = Z
 
        Z = self.parameters["W" + str(self.L)].dot(A) + self.parameters["b" + str(self.L)]
        A = self.sigmoid(Z)
        store["A" + str(self.L)] = A
        store["W" + str(self.L)] = self.parameters["W" + str(self.L)]
        store["Z" + str(self.L)] = Z
 
        return A, store


    def backward(self, X, Y, store):
 
        derivatives = {}
    
        store["A0"] = X.T
    
        A = store["A" + str(self.L)]
        dA = -np.divide(Y, A) + np.divide(1 - Y, 1 - A)
    
        dZ = dA * self.sigmoid_derivative(store["Z" + str(self.L)])
        dW = dZ.dot(store["A" + str(self.L - 1)].T) / self.n
        db = np.sum(dZ, axis=1, keepdims=True) / self.n
        dAPrev = store["W" + str(self.L)].T.dot(dZ)
    
        derivatives["dW" + str(self.L)] = dW
        derivatives["db" + str(self.L)] = db
    
        for l in range(self.L - 1, 0, -1):
            dZ = dAPrev * self.sigmoid_derivative(store["Z" + str(l)])
            dW = 1. / self.n * dZ.dot(store["A" + str(l - 1)].T)
            db = 1. / self.n * np.sum(dZ, axis=1, keepdims=True)
            if l > 1:
                dAPrev = store["W" + str(l)].T.dot(dZ)
    
            derivatives["dW" + str(l)] = dW
            derivatives["db" + str(l)] = db
    
        return derivatives

    def predict(self, X, Y,threshold):
        A, cache = self.forward(X)
        n = X.shape[0]
        p = np.zeros((1, n))
    
        for i in range(0, A.shape[1]):
            if A[0, i] > 0.5:
                p[0, i] = 1
            else:
                p[0, i] = 0
    
        print("Accuracy: " + str(np.sum((p == Y) / n)))


    def plot_cost(self):
        plt.figure()
        plt.plot(np.arange(len(self.costs)), self.costs)
        plt.xlabel("epochs")
        plt.ylabel("cost")
        plt.show()
 

if __name__ == '__main__':

    #path='C:\\Users\\benra\\Documents\\Academics\\fall 22\\374\\temp\\monks1.csv'
    path="mnist_5v8.csv"
    #path="seismic.csv"
    Rseed=6
    split=0.8
    round=.5
    learning_rate=.01



    np.random.seed(Rseed)
   # df=data.readData(path)
    df=pd.read_csv(path,dtype='float64')
    df = df.sample(frac=1, random_state=Rseed).reset_index(drop=True)
    
    trainSize=int(df.shape[0]*split)
    valSize=int(((df.shape[0]-trainSize)//2)+trainSize)

    X_training=df.iloc[0:trainSize,1:].to_numpy()
    X_validation=df.iloc[trainSize:valSize,1:].to_numpy()   
    X_testing=df.iloc[valSize:,1:].to_numpy() 

    Y_training=df.iloc[0:trainSize,0].to_numpy() 
    Y_validation=df.iloc[trainSize:valSize,0].to_numpy() 
    Y_testing=df.iloc[valSize:,0].to_numpy() 




    print("df's shape: " + str(df.shape))
    print(df.head())
    #layers_dims = [df.shape[1]-1, 2, 1] #input size, #number of nodes, #number of nodes,..., 1]
    layers_dims =[df.shape[1]-1,10,1]
    ann = ANN(layers_dims)
    ann.n=trainSize #number of training examples
    print("ann's n: " + str(ann.n))
    ann.initialize_parameters()
    print(ann.parameters.get("W1").shape)
    print(ann.parameters.keys())
    ann.fit(X_training, Y_training, learning_rate)
    ann.predict(X_testing, Y_testing,round)
    ann.plot_cost()

    #print(ann.parameters)
   # ann.fit(train_x, train_y, learning_rate=0.1, n_iterations=1000)
   # ann.predict(train_x, train_y)
   # ann.predict(test_x, test_y)
   # ann.plot_cost()

#lr=5 monks1.csv
