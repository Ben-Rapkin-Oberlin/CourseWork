from sklearn import tree
import time
def DT(data,test,seed):
    #data is a pandas dataframe
    #col 0 is labels
    #print("#####Decision Tree#####")
    x=data.iloc[:,1:]
    y=data.iloc[:,0]
    test=test.iloc[:,1:]
    iris = tree.DecisionTreeClassifier(random_state=seed)

    st=time.process_time()
    iris.fit(x,y)
    #print(time.process_time()-st)

    st=time.process_time()
    predictions=iris.predict(test) #an array of predictions, of shape 1xinstances, retains order
    #print(time.process_time()-st)
    return predictions

