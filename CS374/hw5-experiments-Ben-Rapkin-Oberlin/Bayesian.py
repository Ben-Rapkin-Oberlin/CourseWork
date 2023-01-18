from sklearn.naive_bayes import GaussianNB
import time


def NB(data,test):
    #data is a pandas dataframe
    #col 0 is labels
    #print("#####Naive Bayes#####")
    x=data.iloc[:,1:]
    y=data.iloc[:,0]
    test=test.iloc[:,1:]
    Jackie= GaussianNB()

    st=time.process_time()
    Jackie.fit(x,y)
    print(time.process_time()-st)
    
    st=time.process_time()
    predictions=Jackie.predict(test) #an array of predictions, of shape 1xinstances, retains order
    print(time.process_time()-st)
    return predictions

