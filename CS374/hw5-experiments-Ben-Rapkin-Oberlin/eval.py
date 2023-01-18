
import csv
import numpy as np

def writeConfusion(labels,confusionMatrix,approach,dataset,answers, seed):
        #write confusion matrix to file
        # results-<Approach>-<DataSet>_<Seed>.csv
        pathName="results"+str(approach)+"-"+str(dataset[:-3])+"-"+str(seed)+"csv" #[:-3] removes the .csv from the end of the file name
        #print(pathName)
        with open(pathName, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            labels.append('')
            writer.writerow(labels)
            labels=labels[:-1]
            for i in range(len(confusionMatrix)):

                temp=confusionMatrix[i]
                try:
                    temp.append(labels[i])
                except:
                    print("Error2")
                    print(i)
                    print(labels)
                    exit()
                writer.writerow(temp)


def printRecall(confusionMatrix,labels):
    #find recall
    #not used in normal runing
    #please see test.py to see how it was used

    info=[]
    for i in range (len(confusionMatrix)):
        predicted=confusionMatrix[i][i]
        actual=sum([x[i] for x in confusionMatrix])
        if actual==0:
            info.append('N/A')
            #info.append([labels[i],"N/A"])
            #print(labels[i],", ",predicted,"/",actual)
        else:
            info.append(predicted/actual)
            #info.append([labels[i],predicted/actual])
            #print(labels[i],", ",predicted/actual)
    return info


def eval(df,predictions, answers, approach, dataset, seed):
    #find accuracy and confusion   

    labels=df.iloc[:,0].unique()
    confusionMatrix=[[0 for x in range(len(labels))] for y in range(len(labels))]

    #initialize confusion matrix
    for i in range(len(predictions)):
        confusionMatrix[np.where(labels==predictions[i])[0][0]][np.where(labels==answers.iloc[i,0])[0][0]]+=1 

    writeConfusion(labels.tolist(),confusionMatrix,approach,dataset,answers, seed)
    
    accuracy=sum(predictions==answers.iloc[:,0])/len(predictions)

    CI=2.39*(accuracy*(1-accuracy)/len(predictions))**0.5
    a=[accuracy-CI,accuracy+CI]
    print(dataset,approach, accuracy, a)
    #print(confusionMatrix)
    #return printRecall(confusionMatrix,labels)
    
    
    #find recall
    #find CI
    #find confusion matrix






