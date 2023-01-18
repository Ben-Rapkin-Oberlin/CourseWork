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
        weights =[random.uniform(-0.1,0.1) for x in range(inputSize+1)]
        hidden.append(weights)
    hidden=np.array(hidden)
    out=np.array([random.uniform(-0.1,0.1) for x in range(nodes+1)])
    return hidden,out

def runNode(weights,data):
    #will get past a list of weights
    #will get past a list of data
    #will return hactivation
    pass
    


def backprop(weights,trainData,learning_rate):
    pass




def trainNet(nodes,learning_rate,seed,threshold,trainData,validData):
    ncol=len(trainData[0])
    hidden,out=buildNet(ncol,nodes,seed)
    print(ncol)
    hActivations=np.array([0.0 for x in range(nodes)])

    exponent=0.0
    yhat=0.0
    yhatprime=0.0
    answer=0.0
    #print (out)
    print (hidden[0][18:22])
    #print(trainData.shape)
    for i in range (500):
        for instance in trainData:
            
           # print(instance[18:22])
            #calculate hidden hactivations
            #could be done as a function, but that would be slower
            for j in range(nodes):
                exponent=hidden[j][0]
                for x in range (1,ncol):
                    #calculate exponent
                    exponent+=hidden[j][x]*instance[x]
                #print("j",j)
                #print("e:", exponent)
                #print("v:", (1/(1+(e**(-1*exponent)))))
                #print("h:",hActivations[j])
                hActivations[j]=1/(1+(e**(-1*exponent)))
                #hActivations[j]=5
                #print("h:",hActivations[j])

            #calculate output activation
            #print(hActivations)
            #print(answer)
            exponent=out[0]
            for j in range (nodes):
                exponent+=(out[j+1]*hActivations[j])
            answer=1/(1+(e**(-1*exponent)))
            
            #update output weight
            error=instance[0]-answer
            #print("error:",error)
            #if (answer !=0.0 and answer!=1.0):
             #   print("answer:",answer)
            activation=answer*(1-answer)
            deltaO=error*activation
            delta=(-1)*deltaO
            out[0]=out[0]-(learning_rate*delta)

            for j in range (nodes):
                delta=(-1)*(hActivations[j])*deltaO
                out[j+1]=out[j+1]-(learning_rate*delta)
            #print(hActivations)
            #print(out)



            #update hidden weights
            for j in range (nodes):
                activation=hActivations[j]*(1-hActivations[j])
                deltak=activation*deltaO*out[j+1]
                delta=(-1)*deltak
                hidden[j][0]=hidden[j][0]-(learning_rate*delta)
                for x in range (1,ncol):
                    delta=(-1)*instance[x]*deltak
                    hidden[j][x]=hidden[j][x]-(learning_rate*delta)


                """
                deltak=hActivations[j]*(1-hActivations[j])
                delta=(-1)*activation*error
                hidden[j][0]=hidden[j][0]-(learning_rate*delta)
                #print("delta0:",delta)
                for k in range (1,ncol):
                    delta=instance[k]*activation*error
                    #if k==18 or k==19:
                     #   print("delta:",delta, k)
                    hidden[j][k]=hidden[j][k]-(learning_rate*delta)
                    #print(k)
                """
            #print(hActivations)
            #print(hidden[0][18:22])
            #exit()
        #calculate accuracy
        #print("out:",out)
        #print("hidden:",hidden[0][18:22])
        accuracy=0.0
        summ=0.0
        mmax=0.0
        for instance in validData:
            c=instance[0]
            #calculate hidden hactivations
            for j in range(nodes):
                exponent=hidden[j][0]
                for x in range (1,ncol):
                    #calculate exponent
                    exponent+=hidden[j][x]*instance[x]
                hActivations[j]=1/(1+(e**(-1*exponent)))

            #calculate output hactivation    
            exponent=out[0]
            for j in range (nodes):
                exponent+=(out[j+1]*hActivations[j])
            answer=1/(1+(e**(-1*exponent)))


            #if answer>mmax:
            #    mmax=answer
            #if (answer>=0.5):
             #   print("alpha")
              #  exit()
            #print(answer)
            if answer>=threshold:
                answer=1
           #     summ+=1
            else:
                answer=0

            if answer==instance[0]:
                accuracy+=1
        #print("answer, real:",w,c)
        #print(hActivations)
        #print("summ:",summ/len(validData))
       # print("mmax:",mmax)
        accuracy=accuracy/len(validData)
        print(accuracy, i)
        #print(out)
        if accuracy>=.99:
            print("victory!!!!!!!!")
            break
        if i>=15:
            break
        #print(hActivations)
    #print(hidden)
    return 
            



