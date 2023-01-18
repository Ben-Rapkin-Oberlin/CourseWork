
#Ben Rapkin
import getData
import NetClass
import sys
import time
print("\n"*10)

# Get data
#(path, num_hidden, learning_rate,split,seed,round,num_layers=1):
path=str(sys.argv[1])
num_hidden=int(sys.argv[2])
learning_rate=float(sys.argv[3])
percent=float(sys.argv[4])
seed=int(sys.argv[5])
round=float(sys.argv[6])
num_layers=int(sys.argv[7])

#instantiate neural net
Ann=NetClass.Ann(learning_rate, num_hidden, round, seed, num_layers)



#read data
Ann.openData(path, percent)
#Ann.testnetwork()
#Ann.test()
st=time.time()
Ann.train()
et=time.time()
print("Time:",et-st)

#get accuracies
Ann.test()
#produce output
Ann.makeConfusionMatrix()
