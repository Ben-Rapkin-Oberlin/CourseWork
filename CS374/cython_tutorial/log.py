

import pandas as pd
import numpy as np
import sys
import math
import random
import time
import csv
import train




def readData():
    #figure out which rows are continuous and which are nominal
    #copy nominal data to new list
    #copy continuous data to new list
    #hot encode nominal data note not enough to drop one column, must make sure it can be represented by the other columns
    #normalize continuous data
    #recombine data
    #currently dropping first, this is more than he asked for need to check in
    data = pd.read_csv(sys.argv[1])
    label=data.columns.to_numpy()
    datatype=[]
    for x in data.loc[0]:
        try: #data will be numeric
            a=float(x)
            datatype.append("continuous")
        except: #data will be nominal
            datatype.append("nominal")
    nomdf = pd.DataFrame()
    condf = pd.DataFrame()
    labelnom=[]
    labelcon=[]
    for i in range(len(datatype)):
        if datatype[i]=="nominal":
            nomdf[nomdf.columns.to_numpy().size]=data[label[i]]
            labelnom.append(label[i])
        else:
            condf[condf.columns.to_numpy().size]=data[label[i]].astype(float)
            labelcon.append(label[i])
    nomdf.columns=labelnom
    condf.columns=labelcon
    try:
        nomdf = pd.get_dummies(nomdf, drop_first=True).astype(float)
    except:
        pass
    #normalize continuous data
    for i in range(len(labelcon)):
        big=condf[labelcon[i]].max()
        small=condf[labelcon[i]].min()
        if big== 0.0 and small==0.0:
            a=labelcon[i]
            condf=condf.assign(a=lambda x: 0.0) 
        else:
            condf[labelcon[i]]=(condf[labelcon[i]]-small)/(big-small)
    try:
        df=pd.concat([condf,nomdf],axis=1)
        return df
    except:
        if nomdf.empty:
            return condf
        else:
            return nomdf
   # print(df.loc[240:245])
    return df




def writeConfusion(results):
    labels=['Yes','No']
    pathName="results_"+str(sys.argv[1])+"_"+str(sys.argv[2])+"r_"+str(sys.argv[5])+".csv"
    #print(pathName)
    with open(pathName, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        labels.append('')
        writer.writerow(labels)
        labels=labels[:-1]
        rowYes=[results[0],results[1],'Yes']
        rowNo=[results[2],results[3],'No']
        writer.writerow(rowYes)
        writer.writerow(rowNo)
def makeConfusionMatrix(testData,weights):
    #calculate accuracy
    accuracy=0.0
    confusionMatrix=[0.0,0.0,0.0,0.0] #(0,0), (0,1), (1,0), (1,1)
    for instance in testData:
        yhat=0.0
        exponent=0.0
        for x in range (1,len(weights)):
            #calculate exponent
            exponent+=weights[x]*instance[x]
        exponent+=weights[0]
        if exponent>=0:
            yhat=1
        else:
            yhat=0
        if yhat==instance[0]:
            #yes-yes (0,0)->[0]
            #no-no (1,1)->[3]
            accuracy+=1
            if yhat==0:
                confusionMatrix[0]+=1
            else:
                confusionMatrix[3]+=1

        else:
            #yes-no (0,1)->[1]
            #no-yes (1,0)->[2]
            if yhat==0:
                confusionMatrix[1]+=1
            else:
                confusionMatrix[2]+=1
    accuracy=accuracy/len(testData)
    #print("done----------------")
    #print ("Accuracy: ",accuracy,"%")
    #print(accuracy, end=" ")
    return confusionMatrix


np.seterr(all='raise')


print("-"*100)
print("-"*100)
st=time.process_time()
datafram=readData()
#shuffle data

datafram = datafram.sample(frac=1, random_state=int(sys.argv[5])).reset_index(drop=True)
l=len(datafram)
t=math.floor(l*float(sys.argv[3]))
v=math.floor(l*float(sys.argv[4]))+t
#convert to numpy array as looping through rows is slow with pandas
data=datafram.to_numpy()
#print(datafram.loc[0:2])
#print(data[0:2])
#print(data[10])
trainData=data[0:t]
#print(trainData[0:2])

valid=data[t+1:v]
test=data[v+1:l]
#print(test[12])

random.seed(sys.argv[5])
ncol=len(trainData[0])
weights = [random.uniform(-.1,.1) for x in range(ncol)]
learning_rate=float(sys.argv[2])

weights=train.train(trainData,valid,weights,learning_rate,math.exp(1))
confusionMatrix=makeConfusionMatrix(test,weights)
writeConfusion(confusionMatrix)

print(time.process_time()-st)