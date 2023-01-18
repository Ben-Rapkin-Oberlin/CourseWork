from sklearn.neural_network import MLPClassifier

from warnings import simplefilter
from sklearn.exceptions import ConvergenceWarning
simplefilter("ignore", category=ConvergenceWarning)
import time

def NN(data,test,seed):
    #data is a pandas dataframe
    #col 0 is labels
    #print("#####Neural Network#####")
    x=data.iloc[:,1:]
    y=data.iloc[:,0]
    test=test.iloc[:,1:]

    Diego = MLPClassifier(random_state=seed)
    
    #MLPClassifier(solver='lbfgs', alpha=1e-5,
             #            hidden_layer_sizes=(50,), random_state=1,max_iter=100)

    st=time.process_time()
    Diego.fit(x,y)
    print(time.process_time()-st)

    st=time.process_time()
    predictions=Diego.predict(test) #an array of predictions, of shape 1xinstances, retains order
    print(time.process_time()-st)
    return predictions
