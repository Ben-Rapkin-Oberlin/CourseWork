def train(trainData,validData,initalWeights,learning_rate):
    #test is data used to alter weights
    #validation is the test at the end of each epoch to test accuracy
    #test is the final test to test accuracy after training is done either via 99% or 500 epochs
    
    ncol=len(trainData[0])
    weights=initalWeights #we use the full distance as 21 wi and one offest w0
    #print (len(weights))
    fail=0
    for i in range(500):
        #print("wieght0=",weights[0])
        for instance in trainData:
            #calculate yhat
            yhat=0.0
            exponent=0.0
            for x in range (1,ncol):
                #calculate exponent
                exponent+=weights[x]*instance[x]
            exponent+=weights[0]
            #calculate w0
            try:
                yhat=1/(1+(e**(-1*exponent)))
                yhatprime=yhat*(1-yhat)
                temp=(-1)*yhatprime*(instance[0]-yhat)
                weights[0]=weights[0]-(learning_rate*temp)
            except:
                yhat=0.0
                yhatprime=0.0
            for j in range(1,ncol):
                try:
                    #y^j is instance[0] as that is the label
                    #x_i^j is instance[j] as that is the specific attribute of instance
                    deltaw=(-1*instance[j])*yhatprime*(instance[0]-yhat)
                    weights[j]=weights[j]-(learning_rate*deltaw)
                except:
                    fail+=1
        #calculate accuracy
        accuracy=0.0
        for instance in validData:
            yhat=0.0
            exponent=0.0
            for x in range (1,ncol):
                #calculate exponent
                exponent+=weights[x]*instance[x]
            exponent+=weights[0]
            if exponent>=0:
                yhat=1
            else:
                yhat=0
            if yhat==instance[0]:
                accuracy+=1
        accuracy=accuracy/len(validData)
        if accuracy>=.99:
            break
        #if i>50:
         #break
        #print ("Epoch: ",i," Accuracy: ",accuracy,"%")
        #print(accuracy)
    return weights