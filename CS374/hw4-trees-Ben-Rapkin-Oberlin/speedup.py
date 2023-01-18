import numpy as np
import math

best_entropy=1000

class Tree:
    def __init__(self, attribute='root',label='root',father=None, children=[]):
        self.attribute = attribute #which attribute is used to split the data on this branch
        #self.father=father
        self.label=label
        self.children=[]
        if father:
            father.children.append(self)



def entropyGain(self, col,labels):
        #calculate entropy gain
        #currently taking in a numpy 1d array col and np 1d array labels 
        colName=col[0]
        col=col[1:]
        if self.numeric:
            pass
    
        else:
            colSize=len(col)
            sumEntropy=0
            labeltypes=labels.unique()
            attributes=col.unique()
            for attribute in attributes:
                attInd=np.where(col==attribute) #returns an arrat of indices
                attCount=len(attInd)
                attLabels=np.array([labels[x] for x in attInd] )#get the labels for the attribute
                count=[np.count_nonzero(attLabels==x) for x in labeltypes] #count the number of each label
                percents=[x/attCount for x in count] #get the percent of each label
                ents=[x*math.log2(x) for x in percents]
                attEnt=-1*sum(ents)
                sumEntropy+=attEnt*attCount/colSize
        if sumEntropy<self.current[0]:
            self.current=[sumEntropy,colName]
                
    
def buildTree(self, tree, matrix):
        #this is the training method
        #row 0 is column names
        self.current=[10000,'N/a'] #current best entropy, column name

        if len(matrix)<=1: #to get column number
            tree.label='leaf'
            a=np.bincount(matrix[:,0]).argmax() #most common label to use as guess
            if type(a) == list: #if there is a tie, argmax returns a list, so just pick the first one
                a=a[0]
            tree.default=a #most common label
            return
        labels=matrix[:,0]
        np.apply_along_axis(lambda col: entropyGain(col,labels), 1, matrix) # I believe this apply the function to each column of the matrix
        tree.label=self.current[1]
        if type(a) == list: #if there is a tie, argmax returns a list, so just pick the first one
            a=a[0]
        tree.default=np.bincount(matrix[:,0]).argmax() #most common label to use as guess in case of forced leaf
        
        labelindex=np.where(matrix[0]==self.current[1])[0] #find the index of the column name, returns an array?
        attributes=matrix[:,labelindex].unique()

        if self.numeric:
            pass
        else:
            for attribute in attributes:
                temp=Tree(attribute,'placeHolder',tree)
                self.buildTree(temp,np.delete(matrix, labelindex, 1)) #drop most recent column for next recursion
                
                










           




#read in df
#get column names [1:] as numpy array
#convert df to numpy array