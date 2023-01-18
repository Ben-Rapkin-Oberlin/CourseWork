


import numpy as np
cimport numpy
cimport cython

#ctypedef numpy.float_t DTYPE_t
ctypedef numpy.float64_t DTYPE_t

@cython.boundscheck(False) # turn off bounds-checking for entire function
@cython.wraparound(False)


def train(numpy.ndarray[DTYPE_t, ndim=2] trainData, numpy.ndarray[DTYPE_t, ndim=2] validData ,numpy.ndarray[DTYPE_t, ndim=1] weights,learning_rate,e):
    #test is data used to alter weights
    #validation is the test at the end of each epoch to test accuracy
    #test is the final test to test accuracy after training is done either via 99% or 500 epochs
    
    cdef int ncol=len(trainData[0])
    #weights=initalWeights #we use the full distance as 21 wi and one offest w0
    #print (len(weights))
    cdef int fail=0
    cdef float yhat=0.0
    cdef float exponent=0.0
    cdef float yhatprime=0.0
    cdef float temp=0.0
    cdef float deltaw=0.0
    cdef float accuracy=0.0
    cdef int tsize = trainData.shape[0]
    cdef int vsize = validData.shape[0]


    for epoch in range(500):
        #print("wieght0=",weights[0])
        for i in range(tsize):
            #calculate yhat
            yhat=0.0
            exponent=0.0
            for x in range (1,ncol):
                #calculate exponent
                exponent+=weights[x]*trainData[i][x]
            exponent+=weights[0]
            #calculate w0
            try:
                yhat=1/(1+(e**(-1*exponent)))
                yhatprime=yhat*(1-yhat)
                temp=(-1)*yhatprime*(trainData[i][0]-yhat)
                weights[0]=weights[0]-(learning_rate*temp)
            except:
                yhat=0.0
                yhatprime=0.0
            for j in range(1,ncol):
                try:
                    #y^j is instance[0] as that is the label
                    #x_i^j is instance[j] as that is the specific attribute of instance
                    deltaw=(-1*trainData[i][j])*yhatprime*(trainData[i][0]-yhat)
                    weights[j]=weights[j]-(learning_rate*deltaw)
                except:
                    fail+=1
        #calculate accuracy
        accuracy=0.0
        for i in range(vsize):
            yhat=0.0
            exponent=0.0
            for x in range (1,ncol):
                #calculate exponent
                exponent+=weights[x]*validData[i][x]
            exponent+=weights[0]
            if exponent>=0:
                yhat=1
            else:
                yhat=0
            if yhat==validData[i][0]:
                accuracy+=1
        accuracy=accuracy/vsize
        if accuracy>=.99:
            break
        #if i>50:
         #break
        #print ("Epoch: ",i," Accuracy: ",accuracy,"%")
        #print(accuracy)
    return weights