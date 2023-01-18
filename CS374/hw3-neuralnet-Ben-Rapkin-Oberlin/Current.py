import numpy as np
import pandas as pd
import random
import math

#TODO
    #Build net (done)
    #Up prop (done)
    #Error 
    #Back prop
    #Trianing 


#all: array of layers and output node

#layers: all nodes repective normal weights in the form: (potientially ragged)
    #[[node 0 weights],[node 1 weights],...]

#offsets: a potientially ragged array
    #[[layer 1's offset],[layer 2 offsets],...]
    #[[all[0]'s offsets], [all[1]'s offset],...]



#build net
def buildNet(layersNum,nodes,inputs,seed):
    # TODO throw error for l=0
    random.seed(seed)
    #add one for activation layer (layerNum is number of hidden layers)
    all=[]
    offset=[]
    for i in range(layersNum):
        offset.append([random.uniform(-0.1,0.1) for x in range(nodes)])
    offset.append(random.uniform(-0.1,0.1))
        

    random.seed(seed)

    #first layer has inputs=weightNum, all others have nodes=weightNum
    layerOne=[]
    #we will use each row to repesent wieght numbers so we get
    #|w11 w21 w31|
    #|w21 w22 w32| 
    #|w31 w23 w33|
    # thus layerone[1:] will produce 
    for i in range (nodes):
        node =[random.uniform(-0.1,0.1) for x in range(inputs)]
        layerOne.append(node)
    all.append(layerOne)
    for i in range (layersNum-1): #minus one as the fist layer is completed
        layerCurrent=[]
        for j in range(nodes):
            node=[random.uniform(-0.1,0.1) for x in range(nodes)]
            layerCurrent.append(node)
        all.append(layerCurrent)
    all.append([random.uniform(-0.1,0.1) for x in range(nodes)])
    
    return all,offset



def upProp(input,layer,offset):
    #first layer 1 agianst the inputs
    #let offset be at index 0
    
    print("\n",layer,input, "layer, input")
    expNot=np.matmul(layer,input) #no offset yet
        #        (3x3) x (3x1)  = (3x1)
        #|w11 w21 w31|   |i1|    |exp'1|
        #|w12 w22 w32| * |i2|  = |exp'2|
        #|w13 w23 w33|   |i3|    |exp'3|
    #print(expNot, "a")
    exp=np.add(expNot,offset)
    print(exp,"b")
        #|exp1|
        #|exp2|
        #|exp3|
    #print(exp,"c")
    try:
        act=[(1/(1+math.e**(-x))) for x in exp]    
    except:
        act=[(1/(1+math.e**(-exp)))]
    return act


"""
#all=np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

input=np.array([2,2,2])
#temp=upProp(input,all,[1,1,1])
#print(temp)
tt=upProp([2,2,2],[4,7,12],[1])
print(tt)

print(np.matmul([4,7,12],[2,2,2]))

#upProp(input,all,[])
"""

all,offsets=buildNet(2,3,2,10)
instance=[2,2]
print(all)
print(len(offsets))
for i in range (len(all)):
    instance=upProp(instance,all[i],offsets[i])
    print("instance",instance)

    
def trainNet(all, offsets, trainData, vailData):
    size=len(all)
    for i in range (500):
        for instance in trainData:
            answer=instance[0]
            input=instance[1:]
            for i in range(size):
                input=upProp(input,all[i],offsets[i])
            error=answer-input
            
            

            






        

    





  




#frontProp

#Error 

#backProp

#Access






