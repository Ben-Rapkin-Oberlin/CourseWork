#Ben Rapkin
import math
import pandas as pd
import numpy as np
import random
import csv


class Tree:

    def __init__(self, attribute='root',label='root',father=None, children=[],default='null',discriminator='null'):
        #this is the tree class
        self.label=label #which column to look at
        self.attribute = attribute #which attribute is used to split the data
        self.children = []
        self.default = default #the most popular label at that node, used for prediction if attribute is not found
        self.discriminator = discriminator #the value of the attribute that is used to split the data
        if father:
            father.children.append(self)

    
    def __str__(self):
        #this is so the pptree will print the tree correctly
        return self.function

class Cleo:

    def __init__(self, path, split,seed,numeric):
        #initialize decision tree
        self.path=path
        self.data=pd.read_csv(path)
        a=self.data.iloc[:,0].to_numpy()
        self.allLabels=list(np.unique(self.data.iloc[:,0].to_numpy()))
        self.seed=seed
        self.numeric=numeric
        if not self.numeric:
            self.data=self.data.astype('str')
        random.seed(seed)
        col=np.array(self.data.columns)
        self.data=self.data.sample(frac=1, random_state=int(seed)).reset_index(drop=True).to_numpy()
        threshold=int(len(self.data)*split)
        self.trainData=np.vstack((col, self.data[:threshold]))
        self.testData=np.vstack((col, self.data[threshold:]))
        #self.testData=np.vstack((col, self.data[:threshold]))
        self.confusionMatrix=[]
        for i in range(len(self.allLabels)):
            temp=[]
            for j in range (len(self.allLabels)):
                temp.append(0)
            self.confusionMatrix.append(temp)
                

        self.tree=Tree()
        self.correct=0
        self.discriminantor=None
        
    def entropyGain(self, col,labels):
        #calculate entropy gain for each col, records the best col to split on for a given matrix
        #currently taking in a numpy 1d array col and np 1d array labels 
        colName=col[0]
        col=col[1:]
        colSize=len(col)
        try:    
            labeltypes=np.unique(labels[1:])
        except:
            print(col)
            print(labels)
            exit()
        if type(col[0])!=str: # this column is numeric          
            
            values=np.unique(col) #returns sorted array of values
           # print("colName: ", colName, "vals:",values)
            for i in range(len(values)-1):
                sumEntropy=0
                threshold=(values[i]+values[i+1])/2
              #  print(threshold)
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

                if sumEntropy<self.current[0] and len(values)>1:
                   # print("here")
                    self.current=[sumEntropy,colName]
                    self.discriminantor=threshold
                #    print(threshold)
    
        else:
            sumEntropy=0
            attributes=np.unique(col)
            for attribute in attributes:
                attInd=np.where(col==attribute)[0] #returns an array of indices
                attCount=len(attInd)
                attLabels=np.array([labels[x+1] for x in attInd] )#get the labels for the attribute
                count=[np.count_nonzero(attLabels==x) for x in labeltypes[:]] #count the number of each label, not one cuase index one says this is labels column
                percents=[x/attCount for x in count] #get the percent of each label  
                ents=[x*math.log(x,2) if x!=0 else 0 for x in percents] #calculate entropy
                attEnt=-1*sum(ents)
                temp=attEnt*attCount/colSize
                sumEntropy+=temp
            if sumEntropy<self.current[0]:
                self.current=[sumEntropy,colName]
        

    def mostCommon(self,col):
        #from https://stackoverflow.com/questions/19909167/how-to-find-most-frequent-string-element-in-numpy-ndarray
        unique,pos = np.unique(col,return_inverse=True) #Finds all unique elements and their positions
        counts = np.bincount(pos)                     #Count the number of each unique element
        maxpos = counts.argmax()                      #Find the position of the most frequent element
        return unique[maxpos]

    
    def buildTree(self, tree, matrix):
       # print("#"*20, "new lvl")
        #this is the training method
        #row 0 is column names
        self.current=[100,'N/a'] #current best entropy, column name
        self.discriminantor=None #not sure this line is even needed as anytime 
        if len(matrix[0])<=1: #to get column number
           
            tree.label='leaf'
            a=self.mostCommon(matrix[1:,0]) #most common label to use as guess

            if type(a) == list: #if there is a tie, argmax returns a list, so just pick the second one to avoid any col names from being chosen
                a=a[0]
            tree.default=a #most common label
            #tree.attribute=str(tree.attribute)+str(a) #to see output/test
            #tree.attribute=a
            return
        try:
            if len(np.unique(matrix[1:,0]))==1: #if all labels are the same
                    tree.label='leaf'
                    tree.default=matrix[1,0]
                    #tree.attribute=str(tree.attribute) + "->" + str(matrix[1,0]) #again to test
                    #tree.attribute=matrix[1,0]
                    return
        except:
            print('error')
            print(matrix)
            print(matrix[:,0])
           # print(np.unique(matrix[:,0]))
            exit()
        try:
            labels=matrix[:,0]
        except IndexError:
            print(matrix)
            exit()

        np.apply_along_axis(lambda col: self.entropyGain(col,labels), 0, matrix[:,1:]) # I believe this apply the function to each column of the matrix
        tree.label=self.current[1]
        tree.discriminator=self.discriminantor #we can do this for all becuase the prediction method will only check this if the column is numeric

       
        a=self.mostCommon(matrix[1:,0]) #most common label to use as guess
        if type(a) == list: #if there is a tie, argmax returns a list, so just pick the first one
            a=a[0] #a[0] is col name, not actual label
        tree.default=a #most common label to use as guess in case of forced leaf
        
        try:
            colNameindex=np.where(matrix[0]==self.current[1])[0][0]#find the index of the column name, returns an array?
        except:
            print(self.current)
            exit()
        
        tree.label=matrix[0,colNameindex]

        attributes=np.unique(matrix[:,colNameindex][1:]) #get the unique attributes
        #attributes=[x if x!=y else None for x in attributes for y in matrix[0]]
        #print("attributes",attributes)
        if self.numeric and type(matrix[1,colNameindex])!=str: #if the column is numeric
            #two children, less than and >= to threshold
            temp1= Tree("Less",'placeHolder',tree)
            temp2= Tree("Greater",'placeHolder',tree)
            try:
                rows1=np.where(matrix[:,colNameindex][1:]<self.discriminantor) #get the rows that are less than the threshold
            except:
                
                print(matrix[:,1])
                print(matrix[:,2])
                print(matrix[:,3])
                print(self.current)
                print(matrix[:,colNameindex][1:])
                print(self.discriminantor)
                print("$$$$$"*10)
                exit()
            rows2=np.where(matrix[:,colNameindex][1:]>=self.discriminantor) #get the rows that are greater than the threshold
            fin1=matrix[0]
            fin2=matrix[0]
            #print("rows1",rows1)
            #print("rows2",rows2)
            for row in rows1: #the plus one is becuase all indexes are off by one due to the labels column
                fin1=np.vstack((fin1,matrix[row+1]))
            for row in rows2:
                fin2=np.vstack((fin2,matrix[row+1]))
            fin1=np.delete(fin1, colNameindex, 1)
            fin2=np.delete(fin2, colNameindex, 1)
            #print("label",tree.label)
            #print("threshold",self.discriminantor)
            #print("matrix",matrix[:10])
            #print("fin1",fin1[:5])
            #print("fin2",fin2[:5])
            #exit()
            self.buildTree(temp1,fin1)
            self.buildTree(temp2,fin2)
           
        else:
            for attribute in attributes:
              
                temp=Tree(attribute,'placeHolder',tree)

                rows=np.where(matrix[:,colNameindex]==attribute)
               
                fin=matrix[0]
                
                for i in rows:
                    fin=np.vstack((fin,matrix[i]))
                
                fin=np.delete(fin, colNameindex, 1)
     
                self.buildTree(temp,fin) #drop most recent column for next recursion
                
    
    def predictHelper(self,tree, row, colNames):
        #given a row, predict a value and increment the correct correct counter
        
        col=tree.label
        #print(col)
       
        if col=='leaf':
                
                prediction=tree.default
                if prediction==row[0]:
                    self.correct+=1
                x=self.allLabels.index(row[0])
                y=self.allLabels.index(prediction)
                self.confusionMatrix[x][y]+=1
                return 

        else:

            index=np.where(colNames==col)[0][0]
            this=row[index]

            if type(this)==str: #if the column is categorical
                index=np.where(colNames==col)[0][0]
                thisAttribute=row[index]
                
                
                for child in tree.children:
                    if child.attribute==thisAttribute:
                        self.predictHelper(child,row,colNames)
                        return
    
                if tree.default==row[0]:
                    self.correct+=1
                x=self.allLabels.index(row[0])
                y=self.allLabels.index(tree.default)
                self.confusionMatrix[x][y]+=1
                return 
            
            else: #if the column is numeric
                if this<tree.discriminator:
                    self.predictHelper(tree.children[0],row,colNames)
                    return
                else:
                    self.predictHelper(tree.children[1],row,colNames)
                    return
            




    def predict(self,tree):
        #this is the testing method
        self.correct=0
        np.apply_along_axis(lambda row: self.predictHelper(tree,row,self.testData[0]),1,self.testData[1:]) #this provides the tree, each row, and the column names
        print("correct",self.correct)
        print("total",len(self.testData[1:]))
        print(self.correct/len(self.testData[1:]))
        self.writeConfusion()

    def writeConfusion(self):
        #write confusion matrix to file
        labels=self.allLabels
        pathName="results-tree"+str(self.path)+"-"+str(self.numeric)+"-"+str(self.seed)+"csv"
        #print(pathName)
        with open(pathName, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            labels.append('')
            writer.writerow(labels)
            labels=labels[:-1]
            for i in range(len(self.confusionMatrix)):
                temp=self.confusionMatrix[i]
                temp.append(labels[i])
                writer.writerow(temp)