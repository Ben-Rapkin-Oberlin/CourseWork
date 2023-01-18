import numpy as np

def backProp(self, error):
        #print("call back")
        self.parital = {}
        
        //print(self.activation)
        #error is scalar
        #update weights for all layers

        #self.layer[self.num_layers][1] is list of weights for final node only one node however
        #self.activation[self.num_layers-1] is list of inputs for final node
        
        #do=activation'*error=activation*(1-activation)*error'
        do=self.activation[self.num_layers]*(1-self.activation[self.num_layers])*error

        self.layer[self.num_layers][1]=np.array([w-self.lr*(-i)*do for w,i in zip(self.layer[self.num_layers][1], self.activation[self.num_layers-1])])
        self.layer[self.num_layers][0][0]=self.layer[self.num_layers][0][0]-self.lr*do
        

        self.parital[self.num_layers]=np.array(do)
        #partial is now a 2-d array

        #dw=w-(lr*Po*-input)

        #For every layer, multiply the next layer's partial by their connecting weights by out*(1-out), to get the partial for current node.
        #Take current node partial, add it to partial, then find dw and db where dw=w-(lr*Po*-input) 
        #let a be list of weights

        for L in range (self.num_layers-1,-1,-1):
            #loop through layers
            for node in range(self.num_hidden):
                #loop through nodes in layer
                dw=0
                for prior in range (len(self.parital[L+1])):
                    #loop through nodes in past layer and multiply by weights
                    #the current value of dw increased by the past node's dw times it's corrosponding weight
                    try:
                       # print(self.parital[L+1][prior])
                        #print(self.layer[L+1][1][prior][node])
                        
                        dw+=self.parital[L+1][prior]*self.layer[L+1][1][prior][node]
                    except Exception as inst:

                        print(self.parital[L+2])
                        print(self.parital[L+1])
                        print("error 158")
                        print("L",L)
                        print("node",node)
                        print("prior",prior)
                        print(self.parital[L+1][prior])
                        print(self.layer[L+1][1].shape)
                        print(self.layer[L+1][1].shape)
                        dw+=self.parital[L+1][prior]*self.layer[L+1][1][prior]
                        
                    
                #get partial for current node

                dw=self.activation[L][node]*(1-self.activation[L][node])*dw

                #store partial for current node
                if L in self.parital:
                    #print("a",self.parital[L])
                    self.parital[L]=np.append(self.parital[L],dw)
                    #print(L,self.parital[L])
                    #exit()
                else:
                    self.parital[L]=np.array([dw])

                #update bias
                try:
                    self.layer[L][0][node][0]-=self.lr*dw
                except Exception as inst:
                 #   print("except 182")
                    #print("layer: ",self.layer[L][0][node])
                    #print(self.lr*dw)
                    self.layer[L][0][node]-=(self.lr*dw)
     
                    #exit()
                #update weights
                for weight in range(1,len(self.layer[L][1][node])):
                    print("dw",dw)
                    print("input",self.activation[L-1][weight])
                    print(self.layer[L][1][node][weight])
                    self.layer[L][1][node][weight]-=self.lr*dw*-self.activation[L-1][weight]
                    print(self.layer[L][1][node][weight])
                    exit()

        
