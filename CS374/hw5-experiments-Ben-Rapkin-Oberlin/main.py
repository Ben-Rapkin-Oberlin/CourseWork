
import sys
import pandas
import time
from read import readData
from DecisionTree import DT
from NeuralNet import NN
from RandForest import RF
from Bayesian import NB
from eval import eval

#read in the seed
    #seed = sys.argv[1]

#for each of the 4 data sets
# one-hot encode the data
# split into training and testing

# train the model
# test the model

# save confusion matrix
    # results-<Approach>-<DataSet>_<Seed>.csv 
# calculate the accuracy and recall
# calculate the CI


seed=int(sys.argv[1])
#datafiles=['hypothyroid.csv','monks1.csv','votes.csv','mnist_1000.csv']
datafiles=['mnist_1000.csv']
times=[[],[],[],[]]

st=time.process_time()
for file in datafiles:
    #print("-----------------------",file,"-----------------------")
    tt=time.process_time()
    #read in the data and one-hot encode
    df=readData(file)
    df = df.sample(frac=1, random_state=seed).reset_index(drop=True)
    
    #split into training and testing using x=80%
    training=df[:int(len(df)*0.8)]
    testing=df[int(len(df)*0.8):]
    

    predictionsNN=NN(training,testing,seed) #Tested and working 
    #predictionsDT=DT(training,testing,seed) #Tested and working
    predictionsRF=RF(training,testing,seed) #Tested and working
    #predictionsBN=NB(training,testing) #Tested and working,but not sure if it's working correctly, it is scoring very low on hypothyroid and mnist_1000
   
    #get accuracy,confusion matrix, and CI
    #CI and accuracy are via stdout
    eval(df,predictionsNN,testing,"NN",file,seed)
    #eval(df,predictionsDT,testing,"DT",file,seed)
    eval(df,predictionsRF,testing,"RF",file,seed)
    #eval(df,predictionsBN,testing,"BN",file,seed)