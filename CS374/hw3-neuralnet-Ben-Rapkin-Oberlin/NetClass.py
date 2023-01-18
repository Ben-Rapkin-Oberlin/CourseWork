
import math
import random
import numpy as np
import pandas as pd
import getData
import csv

def get_float_list(num):
        #produces a list of random floats between 0 and 1
        return np.array([random.uniform(-.1,.1) for x in range(num)])

def sigmoid(x):
        #sigmoid function
        return 1/(1+math.exp(-x))
    

class Ann:
    def __init__(self, learning_rate, num_hidden,round,seed,num_layers=1):
        #initilize variables
        self.lr = learning_rate
        self.round = round
        self.num_hidden = num_hidden
        self.seed = seed
        self.num_layers = num_layers
        self.layer={} #list (bias list, weights list); looks like {0:t0, 1:t1,...,n:tn}
        self.activation = {}
       
    
    def openData(self,path,trainpercent):
        #open data using getData
        self.path=path
        self.trainpercent=trainpercent
        self.df=getData.readData(path)
        self.df = self.df.sample(frac=1, random_state=int(self.seed)).reset_index(drop=True)
        a=int(len(self.df)*trainpercent)
        b=a+int(len(self.df)*(1-trainpercent)/2)
        self.df=self.df.to_numpy()
        self.trainData=self.df[:a]
        self.validData=self.df[a:b]
        self.testData=self.df[b:]
        return
        
    def initilize_weights(self):
        #initilize weights and bias
        random.seed(self.seed)
        data_features=len(self.trainData[0])-1
        #initilize weights

        #0th layer is diffrent
        layer_nodes=[] 
        bias=get_float_list(self.num_hidden)
        for i in range (self.num_hidden):
           layer_nodes.append(get_float_list(data_features))
        self.layer[0]=[bias,np.array(layer_nodes,dtype=object)]

        #initilize weights for hidden layers and out (0,out]
        for i in range (1,self.num_layers):
            bias=get_float_list(self.num_hidden)
            layer_nodes=[]
            for j in range (self.num_hidden):
                layer_nodes.append(get_float_list(self.num_hidden))
            self.layer[i]=[bias,np.array(layer_nodes,dtype=object)]

        #initilize weights for output layer [out]
        layer_nodes=[]
        bias=get_float_list(1)
        layer_nodes.append(get_float_list(self.num_hidden))
        self.layer[self.num_layers]=[bias,np.array(layer_nodes,dtype=object)]

    def upProp(self, input):
        #input is np.array(instance[1:])
        #calculate activation for each node
        #0th layer uses input instead of activation
        self.activation[-1]=np.array(input)
        for i in range (0,self.num_layers+1):
            exp=[]
           
            w=self.layer[i][1] #weights for node j in layer i
               
            b=self.layer[i][0] #bias for node j in layer i
        
            try:  
                exp=np.array([np.dot(self.activation[i-1],node)+off for node,off in zip(w,b)])
                
            except Exception as e:
                print("error 85",e)           
            try:
                self.activation[i]=np.array([sigmoid(x) for x in exp])
            except Exception  as e:
                print("error",e)
        return
            
    def backProp(self, error):

        # find all dw, then update all weights
        self.parital = {}
                
        #self.layer[self.num_layers][1] is list of weights for final node only one node however
        #self.activation[self.num_layers-1] is list of inputs for final node
       
        #do=activation'*error=activation*(1-activation)*error'

        do=self.activation[self.num_layers]*(1-self.activation[self.num_layers])*error

        #Can go ahead and update bias as nothing is dependent on it
        self.layer[self.num_layers][0][0]+=self.lr*do

        self.parital[self.num_layers]=np.array(do)
        #partial is now a 2-d array

        #dw=w-(lr*Po*-input)

        #find all partials
        for L in range (self.num_layers-1,-1,-1):
            #loop through layers
            for node in range(self.num_hidden):
                #loop through nodes in layer
                dw=0
                for prior in range (len(self.parital[L+1])):
                    #loop through nodes in past layer and multiply by weights
                    #the current value of dw increased by the past node's dw times it's corrosponding weight
                    try:
                        dw+=self.parital[L+1][prior]*self.layer[L+1][1][prior][node]
                    except Exception as inst:
                        dw+=self.parital[L+1][prior]*self.layer[L+1][1][prior]
        
                #get partial for current node
                dw=self.activation[L][node]*(1-self.activation[L][node])*dw

                #store partial for current node
                if L in self.parital:
                    self.parital[L]=np.append(self.parital[L],dw)
                else:
                    self.parital[L]=np.array([dw])

                #update bias
                self.layer[L][0][node]+=self.lr*dw

        #update weights, bias was done in first pass
        self.layer[self.num_layers][1]=np.array([w-self.lr*(-i)*do for w,i in zip(self.layer[self.num_layers][1], self.activation[self.num_layers-1])])
        for L in range (self.num_layers-1,-1,-1):
            for node in range(self.num_hidden):
                #update weights of prior layer as no longer need it's old weights
                for weight in range(0,len(self.layer[L][1][node])):
                    try:
                        a=self.layer[L][1][node][weight]
                        self.layer[L][1][node][weight]-=(self.lr*self.parital[L][node]*(-1*self.activation[L-1][weight]))
                    except Exception as e:
                        print("error 192",e)
                        exit()
        
    def train(self):
        #initilize weights
        self.initilize_weights() #[0] is label
        #train
        for i in range(500):
            errorsum=0
            #print("epoch",i)
            correct=0
            trainCorrect=0
            for instance in self.trainData:
                #upProp
                #print("instance",instance.shape)
                self.upProp(np.array(instance[1:]))

                #cost
                temp=self.activation[self.num_layers][0]
                error=instance[0]-temp
                if temp>=0.5:
                    temp=1
                else:
                    temp=0
                if temp==instance[0]:
                    trainCorrect+=1
                errorsum+=abs(error)
                

                #backProp/update weights
                self.backProp(error)
                
            #print ((trainCorrect/len(self.trainData)), end = " ")
            if i%20==0:
                for instance in self.validData:
                    self.upProp(np.array(instance[1:]))
                    out=self.activation[self.num_layers]
                    if out>=self.round:
                        out=1
                    else:
                        out=0
                    if out==instance[0]:
                        correct+=1
                if correct/len(self.validData)>=.99:
                    print("############CONVERGED############")
                    break
                print("Epoch: ",i," Accuracy: ",correct/len(self.validData))
                print("error",errorsum)
            #print(correct/len(self.validData))
                #print(self.layer[0][0])
                #print(self.layer[0][1])
        return


    def testnetwork(self):
        #makes sure everything was initilized correctly
        self.initilize_weights()
        print("node num:", self.num_hidden)
        print("layer:",len(self.layer))
        print(self.layer.keys())
        for j in range(len(self.layer)):
            print("layer",j)
            print(self.layer[j][0].shape)
            print(self.layer[j][1].shape)
            print("-----------------")

        #print("outWeights", self.layer[self.num_layers][1])
        return
    
    def test(self):
        #test accuracy on test data
        sout=0
        san=0
        print(self.round)
        correct=0
        for instance in self.testData:
                
                self.upProp(np.array(instance[1:]))
                out=self.activation[self.num_layers][0]
                #print("out",out)
                #exit()
                sout+=out
                san+=instance[0]
                if out>=self.round:
                    out=1
                else:
                    out=0
                if out==instance[0]:
                    correct+=1

        print("Accuracy: ",correct/len(self.testData))
        print("Avg out",sout/len(self.testData))
        print("Avg actual",san/len(self.testData))

    def writeConfusion(self,results):
        #write confusion matrix to file
        labels=['Yes','No']
        pathName="results_"+str(self.path[:-4])+"_"+str(self.num_hidden)+"n_"+str(self.lr)+"r_"+str(self.round)+"t_"+str(self.trainpercent)+"p_"+str(self.seed)
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

    def makeConfusionMatrix(self):
        #make confusion matrix
        #calculate accuracy
        accuracy=0.0
        confusionMatrix=[0.0,0.0,0.0,0.0] #(0,0), (0,1), (1,0), (1,1)
        for instance in self.testData:
            self.upProp(np.array(instance[1:]))
            out=self.activation[self.num_layers][0]
                #print("out",out)
                #exit()
               
            if out>=self.round:
                out=1
            else:
                out=0
            
            if out==instance[0]:
                #yes-yes (0,0)->[0]
                #no-no (1,1)->[3]
                accuracy+=1
                if out==0:
                    confusionMatrix[0]+=1
                else:
                    confusionMatrix[3]+=1

                    #top is actual label
                    #side is predicted label

            else:
                #yes-no (0,1)->[1]
                #no-yes (1,0)->[2]
                if out==0:
                    confusionMatrix[1]+=1
                else:
                    confusionMatrix[2]+=1
        accuracy=accuracy/len(self.testData)
        print(confusionMatrix)
        #print("done----------------")
        #print ("Accuracy: ",accuracy,"%")
        #print(accuracy, end=" ")
        self.writeConfusion(confusionMatrix)




        