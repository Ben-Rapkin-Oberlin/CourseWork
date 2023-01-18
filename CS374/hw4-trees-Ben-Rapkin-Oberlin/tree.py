#Ben Rapkin
import sys
import treeClass
import time
from pptree import *



path=sys.argv[1]
percent=float(sys.argv[2]) # no need for validation set, just training/test 
seed=float(sys.argv[3])
numericBool=("True"==str(sys.argv[4])) # True for numeric, False for nominal
#do not need to one hot encode, can just use regular values



#Entropy=-Sum[p(S,l)log2[p(S,l)]]
#p(S,l)=# of examples in S with label l/# of examples in S

#Gain(S,A)=Entropy(S)-Sum[# of examples in S with value v/# of examples in S]*Entropy(Sv)

st=time.process_time()
Cleo=treeClass.Cleo(path, percent, seed, numericBool) #create tree
st=time.process_time()-st
print("Time to build Cleo: "+str(st))
Cleo.buildTree(Cleo.tree, Cleo.trainData) #build tree
st=time.process_time()-st
print("Time to build tree: "+str(st))
#print_tree(Cleo.tree,"children", "attribute",horizontal=True)
#print_tree(Cleo.tree,"children", "discriminator",horizontal=True)
#print_tree(Cleo.tree,"children", "label",horizontal=True)
Cleo.predict(Cleo.tree) #predict
st=time.process_time()-st
print("Time to predict: "+str(st))

#Cleo.printTree(Cleo.tree)
#Cleo.basicprint(Cleo.tree)