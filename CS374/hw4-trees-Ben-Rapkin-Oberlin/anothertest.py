
import numpy as np
import math
import pandas as pd

global current
current=[100,'N/a']


def numericEntropyGain(col,labels):
    global current
    #calculate entropy gain
    #currently taking in a numpy 1d array col and np 1d array labels 
    colName=col[0]
    col=col[1:]
    labeltypes=np.unique(labels)
    if type(col[0])!=str: # this column is numeric
            colSize=len(col)
            sumEntropy=0
            labeltypes=np.unique(labels) 
            values=np.unique(col) #returns sorted array of values
            print(values)
            for i in range(len(values)-1):
                sumEntropy=0
                threshold=(values[i]+values[i+1])/2

                smallValues=np.where(col<=threshold)[0] #list of indices 
                attCount=len(smallValues) #number of values in this attribute, used to cauculate p(l,s)
                attLabels=np.array([labels[x+1] for x in smallValues] )#get the labels for the attribute
                count=[np.count_nonzero(attLabels==x) for x in labeltypes[:]] #count the number of each label, not one cuase index one says this is labels column
                percents=[x/attCount for x in count] #get the percent of each label  
                ents=[x*math.log(x,2) if x!=0 else 0 for x in percents] #calculate entropy
                attEnt=-1*sum(ents)
                temp=attEnt*attCount/colSize
                sumEntropy+=temp
                



                bigValues=np.where(col>threshold)[0] #list of indices 
                attCount=len(bigValues)
                attLabels=np.array([labels[x+1] for x in bigValues] )#get the labels for the attribute
                count=[np.count_nonzero(attLabels==x) for x in labeltypes[:]] #count the number of each label, not one cuase index one says this is labels column
                percents=[x/attCount for x in count] #get the percent of each label  
                ents=[x*math.log(x,2) if x!=0 else 0 for x in percents] #calculate entropy
                attEnt=-1*sum(ents)
                temp=attEnt*attCount/colSize
                sumEntropy+=temp

                #print(threshold,temp)


                print(threshold,sumEntropy)

                if sumEntropy<current[0]:
                    current=[sumEntropy,threshold]



df=pd.read_csv("exampleNumeric.csv")
print(df[:])
data=df.iloc[:,2]
labels=df.iloc[:,0].to_numpy()
data=data.to_numpy()

#data=np.array([-11111,40,48,60,72,80,90],dtype=int)
#labels=np.array(["Play","No","No","Yes", "Yes","Yes", "No"])


numericEntropyGain(data,labels)
#np.apply_along_axis(lambda col: numericEntropyGain(col,labels), 1, data)
print(current)

