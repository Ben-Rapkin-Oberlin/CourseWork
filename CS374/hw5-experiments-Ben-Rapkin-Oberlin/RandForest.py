from sklearn.ensemble import RandomForestClassifier
import time

def RF(data,test,seed):
    #data is a pandas dataframe
    #col 0 is labels
    #print("#####Random Forest#####")
    x=data.iloc[:,1:]
    y=data.iloc[:,0]
    test=test.iloc[:,1:]
    ron = RandomForestClassifier(random_state = seed)
    
    st=time.process_time()
    ron.fit(x,y)
    print(time.process_time()-st)
    st=time.process_time()

    st=time.process_time()
    predictions=ron.predict(test) #an array of predictions, of shape 1xinstances, retains order
    print(time.process_time()-st)
    return predictions

