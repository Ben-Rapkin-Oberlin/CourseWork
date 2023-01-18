import pandas as pd
import numpy as np
import sys
import math
import random
import time
import csv
import getData as gd
import node 
import nold
import network
import st as yy

"""
1) It should take as input six parameters:
    a. The path to a file containing a data set (e.g., monks1.csv)
    b. The number of neurons to use in the hidden layer
    c. The learning rate � to use during backpropagation
    d. The percentage of instances to use for a training set
    e. A random seed as an integer
    f. The threshold to use for deciding if the predicted label is a 0 or 1
"""
print("-"*100)
print("-"*100)
st=time.process_time()
#read csv file
datafram=gd.readData(sys.argv[1])

#shuffle data
datafram = datafram.sample(frac=1, random_state=int(sys.argv[5])).reset_index(drop=True)

#get bounds for train, valid, test
l=len(datafram)
t=math.floor(l*float(sys.argv[3]))
v=math.floor(l*float(sys.argv[4]))+t

#convert to numpy array as looping through rows is slow with pandas
data=datafram.to_numpy()

#split data into train, valid, test
trainData=data[0:t]
valid=data[t+1:v]
test=data[v+1:l]

#print(data.shape[0])
#print(data.dtype)
#print(data.ndim)

#train
random.seed(sys.argv[5])
ncol=len(trainData[0])
weights =np.array([random.uniform(-.1,.1) for x in range(ncol)])
#print(weights.dtype)

#weights=[random.uniform(-.1,.1) for x in range(ncol)]
learning_rate=float(sys.argv[2])
st=time.process_time()
#weights=node.train(trainData,valid,weights,learning_rate)
#(nodes,learning_rate,seed,threshold,trainData,validData)
a=0.0
for i in valid:
    a+=i[0]
print("avg:",a/len(valid))
#weights=network.trainNet(10,.2,4,.5,trainData,valid)
print("time taken to train: ",time.process_time()-st)
