
import getData
import NetClass
import sys
print("\n"*10)

# Get data
#(self, learning_rate, num_hidden,round,seed,num_layers=1):
path=str(sys.argv[1])
num_hidden=int(sys.argv[2])
learning_rate=float(sys.argv[3])
percent=float(sys.argv[4])
seed=int(sys.argv[5])
round=float(sys.argv[6])
num_layers=int(sys.argv[7])

Ann=NetClass.Ann(learning_rate, num_hidden, round, seed, num_layers)




Ann.openData(path, percent)
Ann.testnetwork()
#Ann.test()
Ann.train()


Ann.test()
Ann.makeConfusionMatrix()
