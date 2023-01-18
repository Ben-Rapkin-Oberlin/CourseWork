from calendar import EPOCH
from nold import train
import numpy as np
import random
#cimport numpy

e=2.71828182845904523536028747135266249775724709369995

def buildNet(inputSize,nodes, seed):
    random.seed(seed)
    #hidden=np.zeros((4,1))
    hidden=[]
    #print(hidden)
    for i in range (nodes):
        weights =[random.uniform(-0.1,0.1) for x in range(inputSize)]
        hidden.append(weights)
    hidden=np.array(hidden)
    out=np.array([random.uniform(-0.1,0.1) for x in range(nodes)])
    
    intercepts=np.array([random.uniform(-0.1,0.1) for x in range(nodes+1)])
    
    return hidden,out,intercepts

def runNode(weights,data):
    #will get past a list of weights
    #will get past a list of data
    #will return hactivation
    pass
    


def backprop(weights,trainData,learning_rate):
    pass


#prime=activation*(1-activation)


lastDelta=(np.multiply(error,activation))
currentDelta=




def backpropagation(weights,trainData,learning_rate,error,lastdelata):
    #where error=xL-t (x last - actual)
    lastDelta=()























def trainNet(nodes,learning_rate,seed,threshold,trainData,validData):
    ncol=len(trainData[0])
    hidden,out=buildNet(ncol,nodes,seed)
    print(ncol)
    hActivations=np.array([0.0 for x in range(nodes)])

    exponent=0.0
    yhat=0.0
    yhatprime=0.0
    answer=0.0
    for i in range (500):
        for instance in trainData:
    
            #calculate hidden activations
            for j in range(nodes):
                exponent=hidden[j][0]
                for x in range (1,ncol):
                    #calculate exponent
                    exponent+=hidden[j][x]*instance[x]
                hActivations[j]=1/(1+(e**(-1*exponent)))

            #calculate output activation
            exponent=out[0]
            for j in range (nodes):
                exponent+=(out[j+1]*hActivations[j])
            answer=1/(1+(e**(-1*exponent)))
            
            #update output weight
            error=instance[0]-answer
            activation=answer*(1-answer)
            deltaO=error*activation
            delta=(-1)*deltaO
            out[0]=out[0]-(learning_rate*delta)

            for j in range (nodes):
                delta=(-1)*(hActivations[j])*deltaO
                out[j+1]=out[j+1]-(learning_rate*delta)

            #update hidden weights
            for j in range (nodes):
                activation=hActivations[j]*(1-hActivations[j])
                deltak=activation*deltaO*out[j+1]
                delta=(-1)*deltak
                hidden[j][0]=hidden[j][0]-(learning_rate*delta)
                for x in range (1,ncol):
                    delta=(-1)*instance[x]*deltak
                    hidden[j][x]=hidden[j][x]-(learning_rate*delta)

        accuracy=0.0
        for instance in validData:

            #calculate hidden hactivations
            for j in range(nodes):
                exponent=hidden[j][0]
                for x in range (1,ncol):
                    #calculate exponent
                    exponent+=hidden[j][x]*instance[x]
                hActivations[j]=1/(1+(e**(-1*exponent)))

            #calculate output activation    
            exponent=out[0]
            for j in range (nodes):
                exponent+=(out[j+1]*hActivations[j])
            answer=1/(1+(e**(-1*exponent)))

            #calculate accuracy
            if answer>=threshold:
                answer=1
           #     summ+=1
            else:
                answer=0

            if answer==instance[0]:
                accuracy+=1
       
        accuracy=accuracy/len(validData)
        print(accuracy, i)

        if accuracy>=.99:
            print("victory!!!!!!!!")
            break
        if i>=500:
            break
    return 
            

def trainMatMut(nodes,learning_rate,seed,threshold,trainData,validData):
    ncol=len(trainData[0])
    hidden,outNode,intercepts=buildNet(ncol,nodes,seed)
    print(ncol)
    hActivations=np.array([0.0 for x in range(nodes)])
    #exponent=0.0
    yhat=0.0
    yhatprime=0.0
    answer=0.0

    for i in range (500):
        for instance in trainData:
            #hidden is node x inputs
            #instance is 1 x inputs
            #transpose instance to inputs x 1
            #multiply hidden by instance to produce sum of weights x inputs
            #prodcues a node x 1 matrix
            trans=np.transpose(instance)
            exponents=np.matmul(hidden,trans)

            #add intercepts to exponents
            for j in range (nodes):
                exponents[j]+=intercepts[j]
           
            #apply sigmoid to exponents
            for j in range (nodes):
                hActivations[j]=1/(1+(e**(-1*exponents[j])))

            #calculate outNode
            #outNode is 1 x nodes
            #hActivations is nodes x 1
            #multiply outNode by hActivations
            #result is 1 x  1 and thus the output activation
            exponents=np.matmul(hActivations,outNode) #TODO will this return a 1x1 matrix or a scalar?
            exponents=intercepts[nodes]+exponents[0] #add intercept of outNode
            answer=1/(1+(e**(-1*exponents)))


            #calculate Outerror
            error=instance[0]-answer
            activation=answer*(1-answer)
            deltaO=error*activation
            delta=(-1)*deltaO
            intercepts[nodes]=intercepts[nodes]-(learning_rate*delta)

            outNode=
            np.matmul(outNode

            #update output weight
            error=instance[0]-answer
            activation=answer*(1-answer)
            deltaO=error*activation
            delta=(-1)*deltaO
            out[0]=out[0]-(learning_rate*delta)

            for j in range (nodes):
                delta=(-1)*(hActivations[j])*deltaO
                out[j+1]=out[j+1]-(learning_rate*delta)




            #Train outNode

            #Train hidden








    


    #algo
    #for each epoch 
        #train the the hidden layer
        #train the output layer
        #calculate instance's accuracy
        #backpropogate
        #calculate accuracy
        #if accuracy is good enough, break
    #return weights


        

    
#print(buildNet(1, 3,50))
        
