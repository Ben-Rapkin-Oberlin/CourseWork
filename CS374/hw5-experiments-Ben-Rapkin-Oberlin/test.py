
import sys
import pandas
from read import readData
from NeuralNet import NN
from DecisionTree import DT
from RandForest import RF
from Bayesian import NB
import sys
from eval import eval


#file='hypothyroid.csv'
#file='monks1.csv'
#file='votes.csv'
#file='mnist_1000.csv'
#file='mnist_5v8.csv'
seeds=[0,1,2,3,4]
#seeds=[0]



# This file is designed to calculate recall for each model, for each dataset for each sead,
datafiles=['hypothyroid.csv','monks1.csv','votes.csv','mnist_1000.csv']
#datafiles=['monks1.csv']

for file in datafiles:
    print(file)
    recallNN=[]
    index=[]
    df=readData(file)
    labels=df.iloc[:,0].unique()
    for seed in seeds:
        #print(seed)

        df=readData(file)
       
        df = df.sample(frac=1, random_state=seed).reset_index(drop=True)
        training=df[:int(len(df)*0.8)]
        testing=df[int(len(df)*0.8):]

        predictionsNN=NB(training,testing)
        temp=eval(df,predictionsNN,testing,'NN',file,seed)

        #if recallNN is !empty, this is for datasets 1-3
        if recallNN:
            for i in range(len(recallNN)):
                if temp[i]!='N/A':
                    try:
                        recallNN[i]+=temp[i]
                    except:
                        print("error0")
                        print(temp[i]=='N/A')
                        print(recallNN[i])
                        exit()

                else:
                    index.append(i)
        #if recallNN is empty, this is for dataset 0       
        else:
            for i in range(len(temp)):
                if temp[i]!='N/A':
                    recallNN.append(temp[i])
                else:
                    recallNN.append(0)
                    index.append(i)
    

    #find the average recall for each file
    for i in range(len(recallNN)):
        #print(recallNN)
        #print(index)
        if i not in index:
            try:
                recallNN[i]=recallNN[i]/(len(seeds))
            except:
                print('error')
                print(recallNN[i])
                print(recallNN)
                exit()
        else:
            try:
                recallNN[i]=recallNN[i]/((len(seeds))-index.count(i))
            except:
                recallNN[i]='N/A'
        print(labels[i],recallNN[i])
        

        