import pandas as pd
import math
import time
import numpy as np



def entropyC(self,df):
        #given a dataframe with 1 attribute and n labels for that attribute 
        #find entropy H(S) for attribute/table
        labels=df.iloc[:,0].unique()
        totalSize=len(df)
        percents=[]

        for label in labels:
            percents.append(len(df[df.iloc[:,0]==label])/totalSize) #this is p(S,l) for a given label l
        ents=[x*math.log2(x) for x in percents]
        entTotal=-1*sum(ents)
        return entTotal

    def entropyGain(self, df):
        #calculate entropy gain
        #all=[]
        if self.numeric:
            pass
    
        else:
            maxlabel=(100,"abitrary")
            allLabels=df.columns[1:]

            for col in allLabels:
                sumEntropy=0
                totalSize=df[col].count()
                for attribute in df[col].unique():
                    temp=pd.concat([df.iloc[:,0],df[col]],axis=1)
                    fin=temp[temp[col]==attribute]
                    attributeSize=len(fin)
                    sumEntropy+=((attributeSize/totalSize)*self.entropyC(fin))
                #a=.9403-sumEntropy
                #all.append((col,a))
                if sumEntropy<maxlabel[0]:
                    maxlabel=(sumEntropy, col)
        return maxlabel[1]
        



    def buildTree(self, tree, df):
        #this is the training method
        #print(df, len(df))
        if len(df.columns)<=1:
            tree.label='leaf'
            #tree.add_child('answer',df.iloc[:,0].mode()[0])
            #print(tree.children)
            #print("leaf")
           # exit()
            tree.default=df.iloc[:,0].mode()[0]
            return
        #until all examples are pure ie only one label
        bestLabel=self.entropyGain(df)

        tree.label=bestLabel
        tree.default=df.iloc[:,0].mode()[0]
        attributes=df[bestLabel].unique()
        #print(attributes)
        #print(bestLabel)
        

        if not self.numeric: #if classifier task
            subsets=[(df[df[bestLabel]==x].reset_index(drop=True).drop(bestLabel,axis=1)) for x in attributes] #split data into subsets by attribute, drops old label
            for i in range (len(attributes)):
                tree.add_child('null',attributes[i]) #adds label/attribute to tree as children
                self.buildTree(tree.children[attributes[i]],subsets[i]) #recursively builds tree for each child df with only rows with attribute i and bestLabel col dropped



numeric=False

datafram = pd.read_csv('monks1.csv')
print(datafram[0])
exit
datafram.head()
times=[]
while len(datafram.columns)>1:
    start=time.time()
    l=entropyGain(datafram)
    datafram=datafram.drop(l,axis=1)
    end=time.time()
    times.append(end-start)
    print(l)
print(times)
#df= pd.read_csv("monks1.csv")
#print(df)
#print(df.Outlook.count())

#print(entropyGain(df))
"""
for col in df.columns:
    print(col)
    print(df[col].unique())
    """